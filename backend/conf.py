import os

uvicorn_config = {
    'host': os.environ.get('HOST'),
    'port': int(os.environ.get('PORT')),
    'reload': True
}

smtp_config = {
    'MAIL_USERNAME': os.environ.get('SMTP_LOGIN'),
    'MAIL_PASSWORD': os.environ.get('SMTP_PASSWORD'),
    'MAIL_FROM': os.environ.get('SMTP_EMAIL'),
    'MAIL_PORT': os.environ.get('SMTP_PORT'),
    'MAIL_SERVER': os.environ.get('SMTP_HOST'),
    'MAIL_FROM_NAME': os.environ.get('SMTP_NAME'),
    'MAIL_SSL_TLS': True,
    'MAIL_STARTTLS': False,
    'USE_CREDENTIALS': True,
    'TIMEOUT': 30
}

DEFAULT_LIMIT = 10
DEFAULT_SKIP = 0
NOTIFICATIONS_LIMIT = 100