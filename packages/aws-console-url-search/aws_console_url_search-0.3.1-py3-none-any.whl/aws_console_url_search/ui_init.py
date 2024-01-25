# -*- coding: utf-8 -*-

import zelfred.api as zf

from .ui_def import UI
from .paths import path_current_region

# ------------------------------------------------------------------------------
# We use ${HOME}/.aws_console_url_search/current_region.txt file to store
# the current region. The empty file means no region is selected.
# ------------------------------------------------------------------------------
if path_current_region.exists():
    content = path_current_region.read_text().strip()
    aws_region = content if content else None
else:
    aws_region = None

ui = UI(aws_region=aws_region)


def run_ui():
    """
    Run the AWS console url search UI. This is the entry point of the CLI command.
    """
    zf.debugger.reset()
    zf.debugger.enable()
    ui.run()
