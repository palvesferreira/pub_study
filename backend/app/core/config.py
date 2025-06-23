import os
import urllib.parse
from typing import Optional, List, Any
import secrets

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

SERVICE_NAME = 'Investment Tracker'
DESCRIPTION = 'Investment Tracker - Application'


class Settings(BaseSettings):
    # Auth settings
    SECRET_KEY: str = secrets.token_urlsafe(32)  # Gera uma chave nova a cada carga
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # FastAPI settings
    API_TITLE: Optional[str] = "LDAP API"
    API_VERSION: Optional[str] = "1.0.0"
    API_V1_STR: Optional[str] = "/api/v1"
    API_V1_DOCS: bool = False
    API_V1_REDOC: bool = False
    BACKEND_CORS_ORIGINS: List = ['*']  # : List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Investment Tracker"

    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_PORT: Optional[int] = 5432
    POSTGRES_DB: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_USER: Optional[str] = None

    DATABASE_URL: Optional[PostgresDsn] = None

    @field_validator("DATABASE_URL", mode='before')
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        # return PostgresDsn.build(
        #     scheme="postgresql",
        #     username=info.data.get("POSTGRES_USER") or "",
        #     password=urllib.parse.quote(info.data.get("POSTGRES_PASSWORD")) or "",
        #     host=info.data.get("POSTGRES_SERVER") or "localhost",
        #     port=int(info.data.get("POSTGRES_PORT") or 5432),
        #     path=f"/{info.data.get('POSTGRES_DB') or ''}",
        # )
        username = urllib.parse.quote_plus(info.data.get("POSTGRES_USER") or "postgres")
        password = urllib.parse.quote_plus(info.data.get("POSTGRES_PASSWORD") or "postgres")
        host = info.data.get("POSTGRES_SERVER") or "db"
        port = str(info.data.get("POSTGRES_PORT") or "5432")
        database = info.data.get("POSTGRES_DB") or "investment_tracker"

        return PostgresDsn(f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}")

    model_config = SettingsConfigDict(
        env_file=".env" if os.getenv("ENVIRONMENT") == "production" else "../.env.develop",
        env_file_encoding="utf-8"
    )    

    @staticmethod
    def num_version():
        return __version__

    @staticmethod
    def description():
        return DESCRIPTION

    def version(self):
        return f'{SERVICE_NAME} Version %s' % self.num_version()

settings = Settings()

__version__ = '0.1.0'
