# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import typing as T
import fire

from .._version import __version__


class AcsCli:
    """
    AWS Console Url Search CLI.
    """

    def __call__(self, version: T.Optional[bool] = None):
        """
        Serve for the ``acs`` command without any arguments.
        """
        from ..ui_init import ui, run_ui

        if version:
            print(__version__)
        else:
            run_ui()


def run():
    """
    The entry point of this CLI tool.
    """
    ars_cli = AcsCli()
    fire.Fire(ars_cli)
