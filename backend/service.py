from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse
from typing import Optional
from uuid import UUID
import json
from bson import ObjectId

from smtp import send_email_background
from datamodels.object_datamodels import Keys
from datamodels.object_datamodels import Users, User, Notification
from db.database import db
from json_encoders import UUIDEncoder

def find_user_by_id(user_id: UUID, user_database: Users) -> Optional[User]:
    try:
        return next(filter(lambda user: user.user_id == UUID(user_id), user_database.user_list))
    except StopIteration:
        return None
    
def insert_notification(user: User, notification: Notification) -> bool:
    try:
        db.command(
            {
                'updateUser': user.username,
                'customData': {
                    'email': user.custom_data.email,
                    'notifications': [*map(lambda el: el.model_dump(), user.custom_data.notifications + [notification])]
                }
            } 
        )
    except:
        return False
    
    return True
    
def handle_notification_type(
    type: Keys, user: User,
    notification: Notification,
    background_tasks: BackgroundTasks
):
    match type:
        case 'registration':
            send_email_background(
                background_tasks,
                subject=notification.key.upper(),
                email_to=user.custom_data.email,
                body=json.dumps(notification.model_dump(), cls=UUIDEncoder)
            )
            
            return JSONResponse(
                content={
                    'success': True
                },
                status_code=201,
            )
        case 'new_login':
            result = insert_notification(user, notification)
            
            if not result:
                return JSONResponse(
                    content={
                        'success': False,
                        'msg': 'Something went wrong',
                    },
                    status_code=500
                )
            
            send_email_background(
                background_tasks,
                subject=notification.key.upper(),
                email_to=user.custom_data.email,
                body=json.dumps(notification.model_dump(), cls=UUIDEncoder)
            )
            
            return JSONResponse(
                content={
                    'success': True
                },
                status_code=201,
            )
            
        case _:
            result = insert_notification(user, notification)
            
            if not result:
                return JSONResponse(
                    content={
                        'success': False,
                        'msg': 'Something went wrong',
                    },
                    status_code=500
                )
                
            return JSONResponse(
                content={
                    'success': True
                },
                status_code=201,
            )
            
def read_notification(user: User, notification_id: str) -> bool:
    notifications = user.custom_data.notifications
    
    try:
        req_ntf = next(filter(lambda ntf: ntf.id == ObjectId(notification_id), notifications))
    except StopIteration:
        return False
    
    if not req_ntf.is_new:
        return False
    
    req_ntf.is_new = False
    notifications.remove(req_ntf)
    
    try:
        db.command(
            {
                'updateUser': user.username,
                'customData': {
                    'email': user.custom_data.email,
                    'notifications': [*map(lambda el: el.model_dump(), notifications + [req_ntf])]
                }
            } 
        )
    except:
        return False
    
    return True