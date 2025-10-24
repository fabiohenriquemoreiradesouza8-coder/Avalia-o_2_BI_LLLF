from pydantic_settings import BaseSettings, SettingsConfigDict 
from typing import List 
 
class Settings(BaseSettings): 
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore") 
 
    DATABASE_URL: str 
    SECRET_KEY: str 
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 
 
    # Configuracoes do CORS 
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"] 
 
settings = Settings() 
