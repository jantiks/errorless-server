from pydantic import BaseModel
from typing import Optional

class BaseRequestModel(BaseModel):
    date: str

class DumpModel(BaseRequestModel):
    name: str
    body: Optional[str] = None

class EventModel(BaseRequestModel):
    name: str
    body: Optional[str] = None

class NotificationModel(BaseRequestModel):
    title: Optional[str]
    subtitle: Optional[str]