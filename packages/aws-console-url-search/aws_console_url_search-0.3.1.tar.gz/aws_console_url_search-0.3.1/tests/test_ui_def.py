# -*- coding: utf-8 -*-

from aws_console_url_search.ui_def import (
    handler,
    UI,
)

ui = UI()


def test_search_service_handler():
    items = handler(query="ec2 inst", ui=ui, skip_ui=True)
    # items[0].enter_handler(ui)

    items = handler(query="ec2 inst!~", ui=ui, skip_ui=True)

    items = handler(query="abcdefghijklmn", ui=ui, skip_ui=True)
    assert len(items) == 1


def test_search_region_handler():
    assert ui.aws_region != "eu-west-1"
    items = handler(query="!@eu west 1", ui=ui, skip_ui=True)
    items[0].enter_handler(ui)
    assert ui.aws_region == "eu-west-1"

    items = handler(query="!@abcdefghijklmn", ui=ui, skip_ui=True)
    assert len(items) == 1


if __name__ == "__main__":
    from aws_console_url_search.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url_search.ui_def", preview=False)
