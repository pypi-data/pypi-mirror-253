from unittest.mock import patch

import django_comments
from django.test import TestCase
from django_comments_ink.forms import InkCommentForm
from django_comments_ink.models import TmpInkComment
from django_comments_ink.tests.models import Article


class GetFormTestCase(TestCase):
    def test_get_form(self):
        # check function django_comments_ink.get_form retrieves the due class
        self.assertTrue(django_comments.get_form() == InkCommentForm)


class InkCommentFormTestCase(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="September",
            slug="september",
            body="What I did on September...",
        )
        self.form = django_comments.get_form()(self.article)

    def test_get_comment_model(self):
        # check get_comment_model retrieves the due model class
        self.assertTrue(self.form.get_comment_model() == TmpInkComment)

    def test_get_comment_create_data(self):
        # as it's used in django_comments.views.comments
        data = {
            "name": "Daniela",
            "email": "danirus@eml.cc",
            "followup": True,
            "reply_to": 0,
            "level": 1,
            "order": 1,
            "comment": "Es war einmal iene kleine...",
        }
        data.update(self.form.initial)
        form = django_comments.get_form()(self.article, data)
        self.assertTrue(self.form.security_errors() == {})
        self.assertTrue(self.form.errors == {})
        comment = form.get_comment_object()

        # it does have the new field 'followup'
        self.assertTrue("followup" in comment)

    @patch.multiple(
        "django_comments_ink.conf.settings", COMMENTS_INK_DEFAULT_FOLLOWUP=False
    )
    def test_followup_prechecked(self):
        # Have to update form object to re-initialize 'followup' checkbox
        # with settings.
        self.form = django_comments.get_form()(self.article)
        self.assertEqual(self.form.fields["followup"].initial, False)

    @patch.multiple(
        "django_comments_ink.conf.settings", COMMENTS_INK_DEFAULT_FOLLOWUP=True
    )
    def test_followup_preunchecked(self):
        # Have to update form object to re-initialize 'followup' checkbox
        # with settings.
        self.form = django_comments.get_form()(self.article)
        self.assertEqual(self.form.fields["followup"].initial, True)
