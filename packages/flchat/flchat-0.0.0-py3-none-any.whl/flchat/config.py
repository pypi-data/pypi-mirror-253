from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    FLASK_HOST: str = Field(default='0.0.0.0', env="FLASK_HOST") 
    FLASK_PORT: int = Field(default=5000, env="FLASK_PORT")
    FLASK_DEBUG: bool = Field(default=True, env="FLASK_DEBUG")

config = Config()
