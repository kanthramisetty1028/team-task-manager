import os

class Config:
    SECRET_KEY = "supersecretkey"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root123@localhost/task_manager"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt-secret-key"