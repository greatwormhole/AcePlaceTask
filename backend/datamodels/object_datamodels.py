from pydantic import BaseModel, Field
from typing import Literal, Optional, List, Dict
from bson.objectid import ObjectId
from uuid import UUID
from bson.binary import Binary
from datetime import datetime

Keys = Literal['registration', 'new_message', 'new_post', 'new_login']

def generate_timestamp() -> int:
    return int(datetime.timestamp(datetime.now()))

class Notification(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId)
    timestamp: int = Field(default_factory=generate_timestamp)
    is_new: bool = Field(default=True)
    user_id: UUID
    key: Keys
    target_id: Optional[ObjectId]
    data: Optional[Dict]
    
    def model_dump(self, *args, **kwargs):
        try:
            self.user_id = Binary.from_uuid(self.user_id)
        except TypeError:
            pass
        return super().model_dump(*args, **kwargs)
    
    class Config:
        arbitrary_types_allowed=True

class CustomData(BaseModel):
    email: str
    notifications: List[Notification]
    
class Role(BaseModel):
    role: str
    db: str
    
class User(BaseModel):
    id: str = Field(alias='_id')
    user_id: UUID = Field(alias='userId')
    username: str = Field(alias='user')
    db: str
    custom_data: CustomData = Field(alias='customData')
    roles: List[Role]
    mechanisms: List[str]
    
    class Config:
        arbitrary_types_allowed=True
        
class Users(BaseModel):
    user_list: List[User] = Field(alias='users')