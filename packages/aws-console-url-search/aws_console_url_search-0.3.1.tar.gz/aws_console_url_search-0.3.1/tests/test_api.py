# -*- coding: utf-8 -*-

import aws_console_url_search.api as api


def test():
    _ = api


if __name__ == "__main__":
    from aws_console_url_search.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url_search.api", preview=False)
