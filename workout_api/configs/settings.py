from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://workout:workout@localhost/workout"
    )

    class Config:
        env_file = ".env"   # permite carregar variáveis do arquivo .env


settings = Settings()
