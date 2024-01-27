from datetime import datetime
from beanie import Document
from pydantic import Field


class InternalBaseModel(Document):
    create_time: datetime = Field(default_factory=datetime.utcnow)
    update_time: datetime = Field(default_factory=datetime.utcnow)
