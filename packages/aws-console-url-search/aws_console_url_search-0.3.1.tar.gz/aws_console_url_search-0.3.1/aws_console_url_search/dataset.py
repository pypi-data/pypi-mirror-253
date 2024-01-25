# -*- coding: utf-8 -*-

"""
[CN] maintainer guide

这个模块定义了所有要用到的 ``sayt.DataSet``.
"""

import typing as T
import csv
import dataclasses

import sayt.api as sayt

from .paths import (
    dir_index,
    dir_cache,
    path_region_json,
)
from .model import Service, Menu, load_data
from .constants import MAX_SERVICE_RANK, MAX_MENU_RANK


def preprocess_query(query: T.Optional[str]) -> str:  # pragma: no cover
    """
    Preprocess query, automatically add fuzzy search term if applicable.
    """
    delimiter = ".-_@+"
    if query:
        for char in delimiter:
            query = query.replace(char, " ")
        words = list()
        for word in query.split():
            if word.strip():
                word = word.strip()
                if len(word) == 1:
                    if word == "*":
                        words.append(word)
                else:
                    # for fuzzy search, the first two characters must be matched
                    try:
                        if word[-2] != "~" and not word.endswith("!~"):
                            word = f"{word}~1/2"
                    except IndexError:
                        word = f"{word}~1/2"
                    words.append(word)
        if words:
            return " ".join(words)
        else:
            return "*"
    else:
        return "*"


# ------------------------------------------------------------------------------
# AWS Service and Menu
# ------------------------------------------------------------------------------
# fmt: off
fields = [
    sayt.IdField(name="id", stored=True, field_boost=10.0),
    sayt.TextField(name="id_text", stored=True, field_boost=10.0),
    sayt.StoredField(name="srv_name"),
    sayt.StoredField(name="menu_name"),
    sayt.StoredField(name="url"),
    sayt.StoredField(name="desc"),
    sayt.StoredField(name="globally"), # global is a python reserved keyword, so we have to use globally
    sayt.StoredField(name="emoji"),
    sayt.TextField(name="srv_text", stored=True, field_boost=7.5),
    sayt.NgramWordsField(name="srv_ngram", stored=True, minsize=2, maxsize=6, field_boost=5.0),
    sayt.TextField(name="menu_text", stored=True, field_boost=2.0),
    sayt.NgramWordsField(name="menu_ngram", stored=True, minsize=2, maxsize=6, field_boost=1.0),
    sayt.NumericField(name="rank", stored=True, sortable=True, ascending=True),
]
# fmt: on


@dataclasses.dataclass
class ServiceDocument:
    # fmt: off
    id: str = dataclasses.field()
    id_text: str = dataclasses.field()
    srv_name: str = dataclasses.field()
    menu_name: T.Optional[str] = dataclasses.field()
    url: str = dataclasses.field()
    desc: str = dataclasses.field()
    globally: bool = dataclasses.field() # global is a python reserved keyword, so we have to use globally
    emoji: T.Optional[str] = dataclasses.field()
    rank: int = dataclasses.field()
    srv_text: str = dataclasses.field()
    srv_ngram: str = dataclasses.field()
    menu_text: T.Optional[str] = dataclasses.field()
    menu_ngram: T.Optional[str] = dataclasses.field()
    # fmt: on

    @classmethod
    def from_service(cls, service: Service):
        service_rank = service.rank if service.rank else MAX_SERVICE_RANK
        if service.terms:
            srv_text = f"{service.name} {service.terms}"
        else:
            srv_text = service.name
        return cls(
            id=service.id,
            id_text=service.id,
            srv_name=service.name,
            menu_name=None,
            url=service.url,
            desc=service.description,
            globally=service.globally,
            emoji=service.emoji,
            rank=0 - (MAX_SERVICE_RANK - service_rank),
            srv_text=srv_text,
            srv_ngram=srv_text,
            menu_text=None,
            menu_ngram=None,
        )

    @classmethod
    def from_menu(cls, service: Service, menu: Menu):
        service_rank = service.rank if service.rank else MAX_SERVICE_RANK
        menu_rank = menu.rank if menu.rank else MAX_MENU_RANK
        if service.terms:
            srv_text = f"{service.name} {service.terms}"
        else:
            srv_text = service.name
        if menu.terms:
            menu_text = f"{menu.name} {menu.terms}"
        else:
            menu_text = menu.name
        return cls(
            id=menu.id,
            id_text=menu.id,
            srv_name=service.name,
            menu_name=menu.name,
            url=menu.url,
            desc=menu.description,
            globally=service.globally,
            emoji=service.emoji,
            rank=service_rank * MAX_MENU_RANK + menu_rank,
            srv_text=srv_text,
            srv_ngram=srv_text,
            menu_text=menu_text,
            menu_ngram=menu_text,
        )

    @classmethod
    def from_result(cls, doc: sayt.T_DOCUMENT):
        doc.setdefault("menu_name", None)
        doc.setdefault("emoji", None)
        doc.setdefault("menu_text", None)
        doc.setdefault("menu_ngram", None)
        return cls(**doc)


def service_downloader() -> T.List[sayt.T_DOCUMENT]:
    """
    Read data from ``path_data_json`` file.
    """
    docs = list()
    service_list = load_data()
    for service in service_list:
        docs.append(ServiceDocument.from_service(service))
        for menu in service.menus:
            docs.append(ServiceDocument.from_menu(service, menu))
    return [dataclasses.asdict(doc) for doc in docs]


service_index_name = "services"
service_dataset = sayt.DataSet(
    dir_index=dir_index,
    index_name=service_index_name,
    fields=fields,
    dir_cache=dir_cache,
    cache_key=service_index_name,
    cache_tag=service_index_name,
    cache_expire=24 * 60 * 60,
    downloader=service_downloader,
)


# ------------------------------------------------------------------------------
# AWS Region
# ------------------------------------------------------------------------------
@dataclasses.dataclass
class RegionDocument:
    id: str = dataclasses.field()
    region: str = dataclasses.field()
    desc: str = dataclasses.field()


def region_downloader():
    docs = list()
    with path_region_json.open("r", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for region, desc in reader:
            docs.append(dict(id=region, region=region, desc=desc))
    return docs


region_index_name = "regions"
region_dataset = sayt.DataSet(
    dir_index=dir_index,
    index_name=region_index_name,
    fields=[
        sayt.IdField(name="id", stored=True),
        sayt.NgramWordsField(name="region", stored=True, minsize=2, maxsize=6),
        sayt.StoredField(name="desc"),
    ],
    dir_cache=dir_cache,
    cache_key=region_index_name,
    cache_tag=region_index_name,
    cache_expire=60,
    downloader=region_downloader,
)
