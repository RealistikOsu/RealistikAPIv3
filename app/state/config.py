from pydantic import (
    BaseSettings,
    RedisDsn,
    Field,
)

class Config(BaseSettings):
    """The RealistikAPI v3 env var config."""

    sql_user: str = Field(..., env= "ROSU_SQL_USER")
    sql_password: str = Field(..., env= "ROSU_SQL_PASSWORD")
    sql_db: str = Field("rosu", env= "ROSU_SQL_DB")

    redis_dsn: RedisDsn = Field("redis://localhost", env= "ROSU_REDIS_DSN")

    server_port: int = Field(4356, env= "ROSU_API_PORT")

config = Config()
