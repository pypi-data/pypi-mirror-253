# -*- coding: utf-8 -*-

from aws_console_url_search.model import (
    load_data,
)


def test_load_data():
    service_list = load_data()
    service_mapper = {srv.id: srv for srv in service_list}
    assert "s3" in service_mapper


if __name__ == "__main__":
    from aws_console_url_search.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url_search.model", preview=False)
