from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore" )
    DB_CONNECTION: str = "default_connection_string"
    SECRET_KEY : str
    ALGORITHM : str
    EXP_TIME : int

setting = Settings()
print(setting.DB_CONNECTION)