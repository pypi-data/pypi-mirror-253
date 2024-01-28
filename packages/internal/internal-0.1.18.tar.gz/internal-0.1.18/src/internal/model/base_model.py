from datetime import datetime
from typing import List, Tuple

import pymongo
from fastapi import FastAPI
from beanie import Document
from pydantic import Field


class InternalBaseDocument(Document):
    create_time: datetime = Field(default_factory=datetime.utcnow)
    update_time: datetime = Field(default_factory=datetime.utcnow)

    @staticmethod
    async def get_pagination_list(model: Document, app: FastAPI, query: list = None, sort: List[Tuple] = None,
                                  page_size: int = 15, page_no: int = 1, ignore_cache: bool = False,
                                  fetch_links: bool = False):
        if not query:
            query = []

        if not sort:
            sort = [(model.id, pymongo.ASCENDING)]

        total_num = await model.find(*query, ignore_cache=ignore_cache, fetch_links=fetch_links).sort(*sort).count()
        if total_num == 0:
            page_data = []
        else:
            page_data = await model.find(*query, ignore_cache=ignore_cache, fetch_links=fetch_links).sort(*sort).limit(
                page_size).skip((page_no - 1) * page_size).to_list()

        return page_no, page_size, total_num, page_data
