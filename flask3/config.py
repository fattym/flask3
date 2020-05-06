import os


class Config:
    SECRET_KEY = 'c26d6bde3e77e96c634e8a88fd857560'
    SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')