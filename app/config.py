import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://debian-sys-maint:E5PQ82UjVI9MAJQ7@hostname/hieu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False