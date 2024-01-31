from datetime import datetime
from unittest.mock import patch

import pytest
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db.models.signals import pre_save
from django.test import TestCase as DjangoTestCase
from django_comments_ink import get_form, get_model
from django_comments_ink.models import (
    BlackListedDomain,
    InkComment,
    MaxThreadLevelExceededException,
    publish_or_withhold_on_pre_save,
)
from django_comments_ink.moderation import SpamModerator, moderator
from django_comments_ink.tests.models import Article, Diary, MyComment
from django_comments_ink.tests.test_views import post_article_comment


class ArticleBaseTestCase(DjangoTestCase):
    def setUp(self):
        self.article_1 = Article.objects.create(
            title="September", slug="september", body="During September..."
        )
        self.article_2 = Article.objects.create(
            title="October", slug="october", body="What I did on October..."
        )


class InkCommentManagerTestCase(ArticleBaseTestCase):
    def setUp(self):
        super(InkCommentManagerTestCase, self).setUp()
        self.article_ct = ContentType.objects.get(
            app_label="tests", model="article"
        )
        self.site1 = Site.objects.get(pk=1)
        self.site2 = Site.objects.create(domain="site2.com", name="site2.com")

    def post_comment_1(self):
        InkComment.objects.create(
            content_type=self.article_ct,
            object_pk=self.article_1.id,
            content_object=self.article_1,
            site=self.site1,
            comment="just a testing comment",
            submit_date=datetime.now(),
        )

    def post_comment_2(self):
        InkComment.objects.create(
            content_type=self.article_ct,
            object_pk=self.article_2.id,
            content_object=self.article_2,
            site=self.site1,
            comment="yet another comment",
            submit_date=datetime.now(),
        )

    def post_comment_3(self):
        InkComment.objects.create(
            content_type=self.article_ct,
            object_pk=self.article_2.id,
            content_object=self.article_2,
            site=self.site1,
            comment="and another one",
            submit_date=datetime.now(),
        )

    def post_comment_4(self):
        InkComment.objects.create(
            content_type=self.article_ct,
            object_pk=self.article_1.id,
            content_object=self.article_1,
            site=self.site2,
            comment="just a testing comment in site2",
            submit_date=datetime.now(),
        )

    def test_for_app_models(self):
        # there is no comment posted yet to article_1 nor article_2
        count = InkComment.objects.for_app_models("tests.article").count()
        self.assertEqual(count, 0)
        self.post_comment_1()
        count = InkComment.objects.for_app_models("tests.article").count()
        self.assertEqual(count, 1)
        self.post_comment_2()
        count = InkComment.objects.for_app_models("tests.article").count()
        self.assertEqual(count, 2)
        self.post_comment_3()
        count = InkComment.objects.for_app_models("tests.article").count()
        self.assertEqual(count, 3)
        self.post_comment_4()
        count = InkComment.objects.for_app_models("tests.article").count()
        self.assertEqual(count, 4)

    def test_multi_site_for_app_models(self):
        self.post_comment_1()  # To site1.
        self.post_comment_4()  # To site2.
        count_site1 = InkComment.objects.for_app_models(
            "tests.article", site=self.site1
        ).count()
        self.assertEqual(count_site1, 1)
        count_site2 = InkComment.objects.for_app_models(
            "tests.article", site=self.site2
        ).count()
        self.assertEqual(count_site2, 1)


# In order to test 'save' and '_calculate_thread_data' methods, simulate the
# following threads, in order of arrival:
#
# testcase cmt.id   parent level-0  level-1  level-2  level-3
#  step1     1        -      c1                               <-           c1
#  step1     2        -      c2                               <-           c2
#  step2     3        1      --       c3                      <-        c3.c1
#  step2     4        1      --       c4                      <-        c4.c1
#  step3     5        2      --       c5                      <-        c5.c2
#  step4     6        5      --       --        c6            <-     c6.c5.c2
#  step4     7        4      --       --        c7            <-     c7.c4.c1
#  step5     8        3      --       --        c8            <-     c8.c3.c1
#  step5     9        -      c9                               <-           c9
#  step6    10        7                                 c10   <- c10.c7.c4.c1
#  step6    11        8                                 c11   <- c11.c8.c3.c1


def thread_test_step_1(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)

    # post Comment 1 with parent_id 0
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c1",
        submit_date=datetime.now(),
        **kwargs,
    )

    # post Comment 2 with parent_id 0
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c2",
        submit_date=datetime.now(),
        **kwargs,
    )


def thread_test_step_2(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)
    if not "parent_id" in kwargs:
        kwargs["parent_id"] = 1

    # post Comment 3 to parent_id 1
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c3.c1",
        submit_date=datetime.now(),
        **kwargs,
    )

    # post Comment 4 to parent_id 1
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c4.c1",
        submit_date=datetime.now(),
        **kwargs,
    )


def thread_test_step_3(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)

    # post Comment 5 to parent_id 2
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="5.c2",
        submit_date=datetime.now(),
        parent_id=2,
        **kwargs,
    )


def thread_test_step_4(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)

    # post Comment 6 to parent_id 5
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c6.c5.c2",
        submit_date=datetime.now(),
        parent_id=5,
        **kwargs,
    )

    # post Comment 7 to parent_id 4
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c7.c4.c1",
        submit_date=datetime.now(),
        parent_id=4,
        **kwargs,
    )


def thread_test_step_5(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)

    # post Comment 8 to parent_id 3
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c8.c3.c1",
        submit_date=datetime.now(),
        parent_id=3,
        **kwargs,
    )

    # post Comment 9 with parent_id 0
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c3",
        submit_date=datetime.now(),
        **kwargs,
    )


def thread_test_step_6(article, model=get_model(), **kwargs):
    article_ct = ContentType.objects.get(app_label="tests", model="article")
    if not "site" in kwargs:
        kwargs["site"] = Site.objects.get(pk=1)

    # post Comment 10 to parent_id 7
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c10.c7.c4.c1",
        submit_date=datetime.now(),
        parent_id=7,
        **kwargs,
    )

    # post Comment 11 to parent_id 8
    model.objects.create(
        content_type=article_ct,
        object_pk=article.id,
        content_object=article,
        comment="c11.c8.c3.c1",
        submit_date=datetime.now(),
        parent_id=8,
        **kwargs,
    )


class BaseThreadStep1TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(BaseThreadStep1TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        (  # content ->     cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->    1         1          1        0      1      0
            self.c2,  # ->    2         2          2        0      1      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_1_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 0)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 0)


class ThreadStep2TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(ThreadStep2TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        (  # content ->    cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->   1         1          1        0      1      2
            self.c3,  # ->   3         1          1        1      2      0
            self.c4,  # ->   4         1          1        1      3      0
            self.c2,  # ->   2         2          2        0      1      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_2_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 2)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 0)

    def test_threaded_comments_step_2_level_1(self):
        # comment 3
        self.assertTrue(self.c3.parent_id == 1 and self.c3.thread_id == 1)
        self.assertTrue(self.c3.level == 1 and self.c3.order == 2)
        self.assertEqual(self.c3.nested_count, 0)
        # comment 4
        self.assertTrue(self.c4.parent_id == 1 and self.c4.thread_id == 1)
        self.assertTrue(self.c4.level == 1 and self.c4.order == 3)
        self.assertEqual(self.c4.nested_count, 0)


class ThreadStep3TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(ThreadStep3TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        thread_test_step_3(self.article_1)

        (  # -> content:   cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->   1         1          1        0      1      2
            self.c3,  # ->   3         1          1        1      2      0
            self.c4,  # ->   4         1          1        1      3      0
            self.c2,  # ->   2         2          2        0      1      1
            self.c5,  # ->   5         2          2        1      2      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_3_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 2)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 1)

    def test_threaded_comments_step_3_level_1(self):
        # comment 3
        self.assertTrue(self.c3.parent_id == 1 and self.c3.thread_id == 1)
        self.assertTrue(self.c3.level == 1 and self.c3.order == 2)
        self.assertEqual(self.c3.nested_count, 0)
        # comment 4
        self.assertTrue(self.c4.parent_id == 1 and self.c4.thread_id == 1)
        self.assertTrue(self.c4.level == 1 and self.c4.order == 3)
        self.assertEqual(self.c4.nested_count, 0)
        # comment 5
        self.assertTrue(self.c5.parent_id == 2 and self.c5.thread_id == 2)
        self.assertTrue(self.c5.level == 1 and self.c5.order == 2)
        self.assertEqual(self.c5.nested_count, 0)


class ThreadStep4TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(ThreadStep4TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        thread_test_step_3(self.article_1)
        thread_test_step_4(self.article_1)

        (  # content ->    cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->   1         1          1        0      1      3
            self.c3,  # ->   3         1          1        1      2      0
            self.c4,  # ->   4         1          1        1      3      1
            self.c7,  # ->   7         1          4        2      4      0
            self.c2,  # ->   2         2          2        0      1      2
            self.c5,  # ->   5         2          2        1      2      1
            self.c6,  # ->   6         2          5        2      3      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_4_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 3)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 2)

    def test_threaded_comments_step_4_level_1(self):
        # comment 3
        self.assertTrue(self.c3.parent_id == 1 and self.c3.thread_id == 1)
        self.assertTrue(self.c3.level == 1 and self.c3.order == 2)
        self.assertEqual(self.c3.nested_count, 0)
        # comment 4
        self.assertTrue(self.c4.parent_id == 1 and self.c4.thread_id == 1)
        self.assertTrue(self.c4.level == 1 and self.c4.order == 3)
        self.assertEqual(self.c4.nested_count, 1)
        # comment 5
        self.assertTrue(self.c5.parent_id == 2 and self.c5.thread_id == 2)
        self.assertTrue(self.c5.level == 1 and self.c5.order == 2)
        self.assertEqual(self.c5.nested_count, 1)

    def test_threaded_comments_step_4_level_2(self):
        # comment 6
        self.assertTrue(self.c6.parent_id == 5 and self.c6.thread_id == 2)
        self.assertTrue(self.c6.level == 2 and self.c6.order == 3)
        self.assertEqual(self.c6.nested_count, 0)
        # comment 7
        self.assertTrue(self.c7.parent_id == 4 and self.c7.thread_id == 1)
        self.assertTrue(self.c7.level == 2 and self.c7.order == 4)
        self.assertEqual(self.c7.nested_count, 0)


class ThreadStep5TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(ThreadStep5TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        thread_test_step_3(self.article_1)
        thread_test_step_4(self.article_1)
        thread_test_step_5(self.article_1)

        (  # content ->    cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->   1         1          1        0      1      4
            self.c3,  # ->   |- 3      1          1        1      2      1
            self.c8,  # ->      |- 8   1          3        2      3      0
            self.c4,  # ->   |- 4      1          1        1      4      1
            self.c7,  # ->      |- 7   1          4        2      5      0
            self.c2,  # ->   2         2          2        0      1      2
            self.c5,  # ->   |- 5      2          2        1      2      1
            self.c6,  # ->      |- 6   2          5        2      3      0
            self.c9,  # ->   9         9          9        0      1      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_5_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 4)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 2)
        # comment 9
        self.assertTrue(self.c9.parent_id == 9 and self.c9.thread_id == 9)
        self.assertTrue(self.c9.level == 0 and self.c9.order == 1)
        self.assertEqual(self.c9.nested_count, 0)

    def test_threaded_comments_step_5_level_1(self):
        # comment 3
        self.assertTrue(self.c3.parent_id == 1 and self.c3.thread_id == 1)
        self.assertTrue(self.c3.level == 1 and self.c3.order == 2)
        self.assertEqual(self.c3.nested_count, 1)
        # comment 4
        self.assertTrue(self.c4.parent_id == 1 and self.c4.thread_id == 1)
        self.assertTrue(self.c4.level == 1 and self.c4.order == 4)  # changed
        self.assertEqual(self.c4.nested_count, 1)
        # comment 5
        self.assertTrue(self.c5.parent_id == 2 and self.c5.thread_id == 2)
        self.assertTrue(self.c5.level == 1 and self.c5.order == 2)
        self.assertEqual(self.c5.nested_count, 1)

    def test_threaded_comments_step_5_level_2(self):
        # comment 6
        self.assertTrue(self.c6.parent_id == 5 and self.c6.thread_id == 2)
        self.assertTrue(self.c6.level == 2 and self.c6.order == 3)
        self.assertEqual(self.c6.nested_count, 0)
        # comment 7
        self.assertTrue(self.c7.parent_id == 4 and self.c7.thread_id == 1)
        self.assertTrue(self.c7.level == 2 and self.c7.order == 5)  # changed
        self.assertEqual(self.c7.nested_count, 0)
        # comment 8
        self.assertTrue(self.c8.parent_id == 3 and self.c8.thread_id == 1)
        self.assertTrue(self.c8.level == 2 and self.c8.order == 3)
        self.assertEqual(self.c8.nested_count, 0)

    @patch.multiple(
        "django_comments_ink.conf.settings", COMMENTS_INK_MAX_THREAD_LEVEL=2
    )
    def test_exceed_max_thread_level_raises_exception(self):
        article_ct = ContentType.objects.get(app_label="tests", model="article")
        site = Site.objects.get(pk=1)
        with self.assertRaises(MaxThreadLevelExceededException):
            InkComment.objects.create(
                content_type=article_ct,
                object_pk=self.article_1.id,
                content_object=self.article_1,
                site=site,
                comment="cmt 1 to cmt 2 to cmt 1",
                submit_date=datetime.now(),
                parent_id=8,
            )  # already max thread level

    def test_removing_c4_withdraws_c7_and_updates_nested_count(self):
        cm4 = InkComment.objects.get(pk=4)
        self.assertEqual(cm4.nested_count, 1)
        cm1 = InkComment.objects.get(pk=1)
        self.assertEqual(cm1.nested_count, 4)
        # Remove comment 4, save, and check again.
        cm4.is_removed = True
        cm4.save()
        cm4 = InkComment.objects.get(pk=4)
        self.assertEqual(cm4.nested_count, 1)
        cm1 = InkComment.objects.get(pk=1)
        self.assertEqual(cm1.nested_count, 3)


class ThreadStep6TestCase(ArticleBaseTestCase):
    def setUp(self):
        super(ThreadStep6TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        thread_test_step_3(self.article_1)
        thread_test_step_4(self.article_1)
        thread_test_step_5(self.article_1)
        thread_test_step_6(self.article_1)

        (  # content ->    cmt.id  thread_id  parent_id  level  order  nested
            self.c1,  # ->   1         1          1        0      1      6
            self.c3,  # ->   3         1          1        1      2      2
            self.c8,  # ->   8         1          3        2      3      1
            self.c11,  # ->  11        1          8        3      4      0
            self.c4,  # ->   4         1          1        1      5      2
            self.c7,  # ->   7         1          4        2      6      1
            self.c10,  # ->  10        1          7        3      7      0
            self.c2,  # ->   2         2          2        0      1      2
            self.c5,  # ->   5         2          2        1      2      1
            self.c6,  # ->   6         2          5        2      3      0
            self.c9,  # ->   9         9          9        0      1      0
        ) = InkComment.objects.all()

    def test_threaded_comments_step_6_level_0(self):
        # comment 1
        self.assertTrue(self.c1.parent_id == 1 and self.c1.thread_id == 1)
        self.assertTrue(self.c1.level == 0 and self.c1.order == 1)
        self.assertEqual(self.c1.nested_count, 6)
        # comment 2
        self.assertTrue(self.c2.parent_id == 2 and self.c2.thread_id == 2)
        self.assertTrue(self.c2.level == 0 and self.c2.order == 1)
        self.assertEqual(self.c2.nested_count, 2)
        # comment 9
        self.assertTrue(self.c9.parent_id == 9 and self.c9.thread_id == 9)
        self.assertTrue(self.c9.level == 0 and self.c9.order == 1)
        self.assertEqual(self.c9.nested_count, 0)

    def test_threaded_comments_step_6_level_1(self):
        # comment 3
        self.assertTrue(self.c3.parent_id == 1 and self.c3.thread_id == 1)
        self.assertTrue(self.c3.level == 1 and self.c3.order == 2)
        self.assertEqual(self.c3.nested_count, 2)
        # comment 4
        self.assertTrue(self.c4.parent_id == 1 and self.c4.thread_id == 1)
        self.assertTrue(self.c4.level == 1 and self.c4.order == 5)
        self.assertEqual(self.c4.nested_count, 2)
        # comment 5
        self.assertTrue(self.c5.parent_id == 2 and self.c5.thread_id == 2)
        self.assertTrue(self.c5.level == 1 and self.c5.order == 2)
        self.assertEqual(self.c5.nested_count, 1)

    def test_threaded_comments_step_6_level_2(self):
        # comment 8
        self.assertTrue(self.c8.parent_id == 3 and self.c8.thread_id == 1)
        self.assertTrue(self.c8.level == 2 and self.c8.order == 3)
        self.assertEqual(self.c8.nested_count, 1)
        # comment 7
        self.assertTrue(self.c7.parent_id == 4 and self.c7.thread_id == 1)
        self.assertTrue(self.c7.level == 2 and self.c7.order == 6)
        self.assertEqual(self.c7.nested_count, 1)
        # comment 6
        self.assertTrue(self.c6.parent_id == 5 and self.c6.thread_id == 2)
        self.assertTrue(self.c6.level == 2 and self.c6.order == 3)
        self.assertEqual(self.c6.nested_count, 0)

    def test_threaded_comments_step_6_level_3(self):
        # comment 10
        self.assertTrue(self.c10.parent_id == 7 and self.c10.thread_id == 1)
        self.assertTrue(self.c10.level == 3 and self.c10.order == 7)
        self.assertEqual(self.c10.nested_count, 0)
        # comment 11
        self.assertTrue(self.c11.parent_id == 8 and self.c11.thread_id == 1)
        self.assertTrue(self.c11.level == 3 and self.c11.order == 4)
        self.assertEqual(self.c11.nested_count, 0)


def add_comment_to_diary_entry(diary_entry):
    diary_ct = ContentType.objects.get(app_label="tests", model="diary")
    site = Site.objects.get(pk=1)
    get_model().objects.create(
        content_type=diary_ct,
        object_pk=diary_entry.id,
        content_object=diary_entry,
        site=site,
        comment="cmt to day in diary",
        submit_date=datetime.now(),
    )


class DiaryBaseTestCase(DjangoTestCase):
    def setUp(self):
        self.day_in_diary = Diary.objects.create(body="About Today...")
        add_comment_to_diary_entry(self.day_in_diary)

    def test_max_thread_level_by_app_model(self):
        diary_ct = ContentType.objects.get(app_label="tests", model="diary")
        site = Site.objects.get(pk=1)
        with self.assertRaises(MaxThreadLevelExceededException):
            InkComment.objects.create(
                content_type=diary_ct,
                object_pk=self.day_in_diary.id,
                content_object=self.day_in_diary,
                site=site,
                comment="cmt to cmt to day in diary",
                submit_date=datetime.now(),
                parent_id=1,
            )  # already max thread level


class PublishOrWithholdNestedComments_1_TestCase(ArticleBaseTestCase):
    # Add a threaded comment structure (c1, c2, c3) and verify that
    # removing c1 withholds c3.

    def setUp(self):
        super(PublishOrWithholdNestedComments_1_TestCase, self).setUp()
        thread_test_step_1(self.article_1)
        thread_test_step_2(self.article_1)
        #
        # These two lines create the following comments:
        #
        # (  # content ->    cmt.id  thread_id  parent_id  level  order  nested
        #     cm1,   # ->     1         1          1        0      1       2
        #     cm3,   # ->     3         1          1        1      2       0
        #     cm4,   # ->     4         1          1        1      3       0
        #     cm2,   # ->     2         2          2        0      1       0
        # ) = InkComment.objects.all()

    def test_all_comments_are_public_and_have_not_been_removed(self):
        for cm in InkComment.objects.all():
            self.assertTrue(cm.is_public)
            self.assertFalse(cm.is_removed)

    def test_removing_c1_withholds_c3_and_c4(self):
        cm1 = InkComment.objects.get(pk=1)
        self.assertEqual(cm1.nested_count, 2)  # nested_count should be 2.

        cm1.is_removed = True
        cm1.save()
        cm1 = InkComment.objects.get(pk=1)
        self.assertTrue(cm1.is_public)
        self.assertTrue(cm1.is_removed)
        # Is still public, so the nested_count doesn't change.
        self.assertEqual(cm1.nested_count, 2)

        cm3 = InkComment.objects.get(pk=3)
        self.assertFalse(cm3.is_public)
        self.assertFalse(cm3.is_removed)

        cm4 = InkComment.objects.get(pk=4)
        self.assertFalse(cm4.is_public)
        self.assertFalse(cm4.is_removed)


_ink_model = "django_comments_ink.tests.models.MyComment"


class PublishOrWithholdNestedComments_2_TestCase(ArticleBaseTestCase):
    # Then mock the settings so that the project uses a customized
    # comment model (django_comments_ink.tests.models.MyComment), and repeat
    # the logic adding MyComment instances. Then remove c1 and be sure
    # that c3 gets withheld.

    def setUp(self):
        super(PublishOrWithholdNestedComments_2_TestCase, self).setUp()
        thread_test_step_1(
            self.article_1, model=MyComment, title="Can't be empty 1"
        )
        thread_test_step_2(
            self.article_1, model=MyComment, title="Can't be empty 2"
        )
        #
        # These two lines create the following comments:
        #
        # (  # content ->    cmt.id thread_id parent_id level order nested
        #     cm1,   # ->     1        1         1        0     1      2
        #     cm3,   # ->     3        1         1        1     2      0
        #     cm4,   # ->     4        1         1        1     3      0
        #     cm2,   # ->     2        2         2        0     1      0
        # ) = MyComment.objects.all()

    def test_all_comments_are_public_and_have_not_been_removed(self):
        for cm in MyComment.objects.all():
            self.assertTrue(cm.is_public)
            self.assertFalse(cm.is_removed)

    @patch.multiple(
        "django_comments_ink.conf.settings", COMMENTS_INK_MODEL=_ink_model
    )
    def test_removing_c1_withholds_c3_and_c4(self):
        # Register the receiver again. It was registered in apps.py, but we
        # have patched the COMMENTS_INK_MODEL, however we won't fake the
        # ready. It's easier to just register again the receiver, to test
        # only what depends on django-comments-ink.
        model_app_label = get_model()._meta.label
        pre_save.connect(
            publish_or_withhold_on_pre_save, sender=model_app_label
        )

        cm1 = MyComment.objects.get(pk=1)
        cm1.is_removed = True
        cm1.save()
        self.assertTrue(cm1.is_public)
        self.assertTrue(cm1.is_removed)

        cm3 = MyComment.objects.get(pk=3)
        self.assertFalse(cm3.is_public)
        self.assertFalse(cm3.is_removed)

        cm4 = MyComment.objects.get(pk=4)
        self.assertFalse(cm4.is_public)
        self.assertFalse(cm4.is_removed)


@pytest.mark.django_db
def test_get_reply_url(an_articles_comment):
    reply_url = an_articles_comment.get_reply_url()
    assert reply_url == f"/comments/reply/{an_articles_comment.pk}/"


@pytest.mark.django_db
def test_get_queryset_returns_none():
    qs = InkComment.get_queryset(
        content_type=None, object_pk=None, content_object=None
    )
    assert qs is None


@pytest.mark.django_db
def test_get_queryset_with_content_object(an_article, an_articles_comment):
    qs = InkComment.get_queryset(content_object=an_article)
    assert qs[0] == an_articles_comment


# ---------------------------------------------------------------------
# Test BlackListedDomain.


class ArticleCommentModerator(SpamModerator):
    pass


@pytest.mark.django_db
def test_blacklisted_domain_is_blocked(an_article, an_user):
    domain = BlackListedDomain.objects.create(domain="example.com")
    moderator.register(Article, ArticleCommentModerator)
    form = get_form()(an_article)
    data = {
        "name": "Joe",
        "email": f"joe@{domain}",
        "followup": True,
        "reply_to": 0,
        "level": 1,
        "order": 1,
        "comment": "Es war einmal eine kleine...",
    }
    data.update(form.initial)
    response = post_article_comment(data, an_article, auth_user=an_user)
    assert response.status_code == 400  # It would be 302 otherwise.
    moderator.unregister(Article)
    assert InkComment.objects.count() == 0


@pytest.mark.django_db
def test_non_blacklisted_domain_pass(an_article, an_user):
    moderator.register(Article, ArticleCommentModerator)
    form = get_form()(an_article)
    data = {
        "name": "Joe",
        "email": f"joe@example.com",
        "followup": True,
        "reply_to": 0,
        "level": 1,
        "order": 1,
        "comment": "Es war einmal eine kleine...",
    }
    data.update(form.initial)
    response = post_article_comment(data, an_article, auth_user=an_user)
    assert response.status_code == 302
    moderator.unregister(Article)
    assert InkComment.objects.count() == 1


# ---------------------------------------------------------------------
# Test django.db.models.signals.post_delete signal.


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_1(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm1 = InkComment.norel_objects.get(pk=1)
    cm1.delete()

    # It should remove comments 1, 3, 8, 11, 4, 7 and 10.
    # As the comment deleted was at level 0, there is no nested_count
    # record to modify.

    for cid in [1, 3, 8, 11, 4, 7, 10]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_2(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm2 = InkComment.norel_objects.get(pk=2)
    cm2.delete()

    # It should remove comments 2, 5 and 6.
    # As the comment deleted was at level 0, there is no nested_count
    # record to modify.

    for cid in [2, 5, 6]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_3(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm3 = InkComment.norel_objects.get(pk=3)
    cm3.delete()

    # It should remove comments 3, 8 and 11, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      3

    for cid in [3, 8, 11]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)

    c1 = InkComment.norel_objects.get(pk=1)
    assert c1.nested_count == 3


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_4(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm4 = InkComment.norel_objects.get(pk=4)
    cm4.delete()

    # It should remove comments 4, 7 and 10, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      3

    for cid in [4, 7, 10]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)

    c1 = InkComment.norel_objects.get(pk=1)
    assert c1.nested_count == 3


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_5(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm5 = InkComment.norel_objects.get(pk=5)
    cm5.delete()

    # It should remove comments 5 and 6, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c2   # ->    2         2          2        0      1      0

    for cid in [5, 6]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)

    c2 = InkComment.norel_objects.get(pk=2)
    assert c2.nested_count == 0


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_6(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm6 = InkComment.norel_objects.get(pk=6)
    cm6.delete()

    # It should remove comment 6, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c2   # ->    2         2          2        0      1      1
    #  c5   # ->    5         2          2        1      2      0

    with pytest.raises(InkComment.DoesNotExist):
        InkComment.objects.get(pk=6)

    c2 = InkComment.norel_objects.get(pk=2)
    assert c2.nested_count == 1

    c5 = InkComment.norel_objects.get(pk=5)
    assert c5.nested_count == 0


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_7(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm7 = InkComment.norel_objects.get(pk=7)
    cm7.delete()

    # It should remove comments 7 and 10, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      4
    #  c4   # ->    4         1          1        1      5      0

    for cid in [7, 10]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)

    c1 = InkComment.norel_objects.get(pk=1)
    assert c1.nested_count == 4

    c4 = InkComment.norel_objects.get(pk=4)
    assert c4.nested_count == 0


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_8(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm8 = InkComment.norel_objects.get(pk=8)
    cm8.delete()

    # It should remove comments 8 and 11, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      4
    #  c3   # ->    3         1          1        1      2      0

    for cid in [8, 11]:
        with pytest.raises(InkComment.DoesNotExist):
            InkComment.objects.get(pk=cid)

    c1 = InkComment.norel_objects.get(pk=1)
    assert c1.nested_count == 4

    c3 = InkComment.norel_objects.get(pk=3)
    assert c3.nested_count == 0


@pytest.mark.django_db
def test_nested_count_after_deleting_comment_10(an_article):
    thread_test_step_1(an_article)
    thread_test_step_2(an_article)
    thread_test_step_3(an_article)
    thread_test_step_4(an_article)
    thread_test_step_5(an_article)
    thread_test_step_6(an_article)

    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      6
    #  c3   # ->    3         1          1        1      2      2
    #  c8   # ->    8         1          3        2      3      1
    #  c11  # ->   11         1          8        3      4      0
    #  c4   # ->    4         1          1        1      5      2
    #  c7   # ->    7         1          4        2      6      1
    #  c10  # ->   10         1          7        3      7      0
    #  c2   # ->    2         2          2        0      1      2
    #  c5   # ->    5         2          2        1      2      1
    #  c6   # ->    6         2          5        2      3      0
    #  c9   # ->    9         9          9        0      1      0

    cm10 = InkComment.norel_objects.get(pk=10)
    cm10.delete()

    # It should remove comments 8 and 11, and leave the following changes:
    # content -> cmt.id  thread_id  parent_id  level  order  nested
    #  c1   # ->    1         1          1        0      1      5
    #  c4   # ->    4         1          1        1      5      1
    #  c7   # ->    7         1          4        2      6      0

    with pytest.raises(InkComment.DoesNotExist):
        InkComment.objects.get(pk=10)

    c1 = InkComment.norel_objects.get(pk=1)
    assert c1.nested_count == 5

    c4 = InkComment.norel_objects.get(pk=4)
    assert c4.nested_count == 1

    c7 = InkComment.norel_objects.get(pk=7)
    assert c7.nested_count == 0
