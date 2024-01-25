# -*- coding: utf-8 -*-

"""
[CN] maintainer guide

这个模块中定义的是 ``aws_console_url_search/data.json`` 中的数据结构.
"""

import typing as T
import json
import dataclasses

from .constants import MAX_SERVICE_RANK, MAX_MENU_RANK
from .paths import path_data_json


@dataclasses.dataclass
class BaseModel:
    @classmethod
    def from_dict(cls, data: T.Dict[str, T.Any]):
        return cls(**data)

    def to_dict(self) -> T.Dict[str, T.Any]:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Service:
    # fmt: off
    id: str = dataclasses.field()
    name: str = dataclasses.field()
    url: str = dataclasses.field()
    description: str = dataclasses.field()
    globally: bool = dataclasses.field()  # global is a python reserved keyword, so we have to use globally
    terms: T.Optional[str] = dataclasses.field()
    emoji: T.Optional[str] = dataclasses.field()
    rank: T.Optional[int] = dataclasses.field()
    menus: T.List["Menu"] = dataclasses.field(default_factory=list)
    # fmt: on

    @property
    def sort_key(self) -> str:
        return f"{str(self.rank).zfill(8)}-{str(self.id).zfill(50)}"


@dataclasses.dataclass
class Menu:
    id: str = dataclasses.field()
    name: str = dataclasses.field()
    url: str = dataclasses.field()
    description: str = dataclasses.field()
    terms: T.Optional[str] = dataclasses.field()
    rank: int = dataclasses.field()

    @property
    def sort_key(self) -> str:
        return f"{str(self.rank).zfill(8)}-{str(self.id).zfill(50)}"


def load_data() -> T.List[Service]:
    console_url_data = json.loads(path_data_json.read_text())
    service_list = list()
    for service_id, service_data in console_url_data.items():
        menus = list()
        for menu_id, menu_data in service_data.get("menus", {}).items():
            menu = Menu(
                id=menu_id,
                name=menu_data["name"],
                url=menu_data["url"],
                description=menu_data.get("description", menu_data["name"]),
                terms=menu_data.get("terms"),
                rank=menu_data.get("rank", MAX_MENU_RANK),
            )
            menus.append(menu)
        service = Service(
            id=service_id,
            name=service_data["name"],
            url=service_data["url"],
            description=service_data.get("description", service_data["name"]),
            globally=service_data.get("global", False),
            terms=service_data.get("terms"),
            emoji=service_data.get("emoji"),
            rank=service_data.get("rank", MAX_SERVICE_RANK),
            menus=menus,
        )
        service_list.append(service)
    return service_list
