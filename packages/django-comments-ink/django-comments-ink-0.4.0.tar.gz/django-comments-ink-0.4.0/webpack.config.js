"use strict";

const path = require('path');
const webpack = require('webpack');

const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

const package_json = require("./package.json");
const ver = package_json.version;

const devMode = process.env.NODE_ENV !== 'production';

const PRJ_PATH = path.resolve(
    __dirname, 'django_comments_ink', 'static', 'django_comments_ink'
);


const plugins = [
    new webpack.ProgressPlugin(),
    new CleanWebpackPlugin({
        cleanOnceBeforeBuildPatterns: [
            `!*${ver}*.js`
        ]
    }),
];

module.exports = {
    mode: devMode ? 'development' : 'production',
    context: __dirname,
    devtool: 'source-map',

    entry: {
        dci: path.resolve(PRJ_PATH, "js/index.js")
    },

    output: {
        path: path.resolve(PRJ_PATH, "dist"),
        filename: devMode ? `[name]-${ver}.js` : `[name]-${ver}.min.js`
    },

    optimization: {
        minimize: !devMode,
        minimizer: [
            new TerserPlugin({
                terserOptions: {
                    parse: {
                        ecma: 8
                    },
                    compress: {
                        ecma: 5,
                        warnings: false,
                        comparisons: false,
                        inline: 2,
                        drop_debugger: !devMode
                    },
                    mangle: {
                        safari10: true
                    },
                    keep_classnames: !devMode,
                    keep_fnames: !devMode,
                    output: {
                        ecma: 5,
                        comments: false,
                        ascii_only: true
                    }
                }
            }),
        ]
    },

    plugins: plugins,
};
