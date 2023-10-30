from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from datamodels import POSTRead, POSTCreate

app = FastAPI()

@app.post('/create/')
async def post_create(item: POSTCreate):
    return JSONResponse(
        contetn={
            'success': True
        },
        status_code=201,
    )

@app.get('/list/')
async def get_list(req: Request, user_id: str, skip: int, limit: int):
    data = {
        'success': True,
        'data': {
            'elements': -1,
            'new': -1,
            'request': dict(req.query_params),
            'list': [
                
            ]
        }
    }
    return JSONResponse(
        content=data,
        status_code=200,
    )

@app.post('/read/')
async def post_read(query: POSTRead):
    return JSONResponse(
        content={
            'success': True
        },
        status_code=200,
    )
