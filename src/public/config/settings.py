import os

from pydantic.v1 import BaseSettings


class Settings (BaseSettings):
    database_host: str
    database_port: int
    database_name: str
    database_username: str
    database_password: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        sensitive_case = True

    database_host = os.getenv("DATABASE_HOST")
    database_port = os.getenv("DATABASE_PORT")
    database_name = os.getenv("DATABASE_NAME")
    database_username = os.getenv("DATABASE_USERNAME")
    database_password = os.getenv("DATABASE_PASSWORD")
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")


settings = Settings()