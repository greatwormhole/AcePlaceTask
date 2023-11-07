import fastapi

from app import app

@app.exception_handler(ValueError)
async def value_error_handler(req: fastapi.Request, exc: ValueError):
    return fastapi.responses.JSONResponse(
        content={
            'request': dict(req),
            'message': str(exc),
        },
        status_code=400,
    )