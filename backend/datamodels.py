from pydantic import BaseModel

class POSTRead(BaseModel):
    user_id: str
    notification_id: str
    
class POSTCreate(BaseModel):
    user_id: str
    target_id: str | None = None
    key: str
    data: dict | None = None