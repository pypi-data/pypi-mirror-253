# -*- coding: utf-8 -*-

"""
[CN] maintainer guide

这个模块是用来每次人类修改了 ``aws_console_url_search/code/console-urls.json``
之后, 对其进行标准化, 以及将其拷贝到搜索程序所使用的 ``aws_console_url_search/data.json`` 处.
"""

import typing as T
import json

from ..paths import (
    path_console_urls_json,
    path_data_json,
)
from ..constants import MAX_SERVICE_RANK, MAX_MENU_RANK


def load_console_url_data() -> dict:
    content = path_console_urls_json.read_text()
    # human may copy and paste when doing data entry, so we need to fix
    # common mistakes.
    content = content.replace("https://us-east-1.console.aws.amazon.com", "")
    content = content.replace("region=us-east-1", "{region}")
    return json.loads(content)


def dump_console_url_data(console_url_data: dict):
    content = json.dumps(console_url_data, indent=4, ensure_ascii=False)
    path_console_urls_json.write_text(content)
    path_data_json.write_text(content)


def get_sort_key(id: str, rank: int) -> str:
    """
    Max rank value would be 10001000, when service rank is 10000 and menu rank is 1000.
    We sort by rank first, then sort by id (alphabetically).
    """
    return f"{str(rank).zfill(8)}-{str(id).zfill(50)}"


def normalize_console_url_data(console_url_data: dict) -> dict:
    """
    .. note::

        This function try to remove and ``None`` field, and sort the
        service and menu by :func:`sort key <get_sort_key>`.

    :return: normalized console url data
    """

    def normalize_dict(dct: dict, fields: T.List[str]) -> dict:
        new_dct = dict()
        for k in fields:
            v = dct.get(k)
            if v is not None:
                new_dct[k] = v
        return new_dct

    def slugify(s: str, chars: str, sep: str = "_") -> str:
        for c in chars:
            s = s.replace(c, sep)
        return s

    service_fields = [
        "name",
        "url",
        "description",
        "globally",
        "terms",
        "emoji",
        "rank",
        "menus",
    ]
    menu_fields = [
        "name",
        "url",
        "description",
        "terms",
        "rank",
    ]

    service_list = list()
    for service_id, service_data in console_url_data.items():
        # do not change service_data
        service_sort_key = get_sort_key(
            id=service_id,
            rank=service_data.get("rank", MAX_SERVICE_RANK),
        )

        menu_list = list()
        for menu_id, menu_data in service_data.get("menus", {}).items():
            # do not change menu_data (except for id field)
            # validate menu_id
            if not menu_id.startswith(f"{service_id}-"):
                raise ValueError(
                    f"menu id {menu_id!r} does not start with service id {service_id!r}!"
                )
            # sometime human entered crapy id copied from AWS console text,
            # we need to normalize it.
            second_part_id = menu_id.split("-", 1)[1]
            menu_id = service_id + "-" + slugify(second_part_id.lower(), " -.", sep="_")
            menu_sort_key = get_sort_key(
                id=menu_id,
                rank=menu_data.get("rank", MAX_MENU_RANK),
            )
            menu_data = normalize_dict(menu_data, menu_fields)
            menu_list.append((menu_sort_key, menu_id, menu_data))

        service_data["menus"] = {
            menu_id: menu_data
            for _, menu_id, menu_data in sorted(
                menu_list,
                key=lambda x: x[0],
            )
        }
        service_data = normalize_dict(service_data, service_fields)
        service_list.append((service_sort_key, service_id, service_data))

    console_url_data = {
        service_id: service
        for _, service_id, service in sorted(
            service_list,
            key=lambda x: x[0],
        )
    }
    return console_url_data
