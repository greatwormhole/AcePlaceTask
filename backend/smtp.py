from fastapi import BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from conf import smtp_config

conf = ConnectionConfig(**smtp_config)

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )
    fm = FastMail(conf)
    background_tasks.add_task(
       fm.send_message,
       message,
       template_name='email.html'
    )