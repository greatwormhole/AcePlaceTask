from pydantic import BaseModel, Field
from typing import Optional, List
from typing_extensions import TypedDict

from .request_datamodels import GETRequestList
from .object_datamodels import Notification

class GETResponseList(BaseModel):
    
    class Data(TypedDict):
        elements: int
        new: int
        request: GETRequestList
        list: List[Notification]
    
    success: bool = True
    data: Data