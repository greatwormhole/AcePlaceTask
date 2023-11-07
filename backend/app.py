from fastapi import FastAPI, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
import json

from datamodels.request_datamodels import (
    POSTRequestRead,
    POSTRequestCreate,
    GETRequestList,
)
from datamodels.response_datamodels import (
    GETResponseList
)
from datamodels.object_datamodels import Users, Notification
from json_encoders import UUIDEncoder
from db.database import db
from service import (
    find_user_by_id,
    handle_notification_type,
    read_notification
)
from conf import NOTIFICATIONS_LIMIT

app = FastAPI()

@app.post('/create/')
async def post_create(query: POSTRequestCreate, background_tasks: BackgroundTasks):
    
    users = Users(**await db.command('usersInfo'))
    user = find_user_by_id(query.user_id, users)
    
    if user is None:
        return JSONResponse(
            content={
                'success': False,
                'msg': 'User not found',
            },
            status_code=404
        )
        
    if len(user.custom_data.notifications) >= NOTIFICATIONS_LIMIT:
        return JSONResponse(
            content={
                'success': False,
                'msg': 'Notification quantity exceeded'
            },
            status_code=403
        )
    
    return handle_notification_type(query.key, user, Notification(**query.model_dump()), background_tasks)

@app.get('/list/')
async def get_list(req: GETRequestList = Depends()):
    
    users = Users(**await db.command('usersInfo'))
        
    req_user = find_user_by_id(req.user_id, users)
    
    if req_user is None:
        return JSONResponse(
            content={
                'success': False,
                'msg': 'User not found',
            },
            status_code=404
        )
        
    notifications = req_user.custom_data.notifications
    
    content = {
        'success': True,
        'data': {
            'elements': len(notifications),
            'new': len([*filter(lambda ntf: ntf.is_new, notifications)]),
            'request': req.model_dump(),
            'list': notifications[req.skip:req.skip + req.limit]
        }
    }
    return JSONResponse(
        content=json.dumps(GETResponseList(**content).model_dump(), cls=UUIDEncoder),
        status_code=200,
    )

@app.post('/read/')
async def post_read(query: POSTRequestRead):
    
    users = Users(**await db.command('usersInfo'))
    user = find_user_by_id(query.user_id, users)
    
    if user is None:
        return JSONResponse(
            content={
                'success': False,
                'msg': 'User not found',
            },
            status_code=404
        )
    
    result = read_notification(user, query.notification_id)
    
    if not result:
        return JSONResponse(
            content={
                'success': False,
                'msg': "Notification with given id wasn't found or it's already read"
            },
            status_code=404
        )
    
    return JSONResponse(
        content={
            'success': True
        },
        status_code=200,
    )