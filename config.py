import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///studyhub.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AI_API_KEY = os.environ.get("AI_API_KEY", "")
    AI_API_URL = os.environ.get("AI_API_URL", "")