from fastapi import Query
from pydantic import BaseModel, Field
from typing import Optional

from conf import DEFAULT_LIMIT, DEFAULT_SKIP
from datamodels.object_datamodels import Keys

class POSTRequestRead(BaseModel):
    user_id: str
    notification_id: str
    
class POSTRequestCreate(BaseModel):
    user_id: str
    key: Keys
    target_id: Optional[str] = Field(None)
    data: dict = Field({})
    
class GETRequestList(BaseModel):
    user_id: str = Field(Query())
    skip: Optional[int] = Field(Query(DEFAULT_SKIP))
    limit: Optional[int] = Field(Query(DEFAULT_LIMIT))