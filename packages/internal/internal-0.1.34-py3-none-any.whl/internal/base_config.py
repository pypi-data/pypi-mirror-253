from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    DEBUG: bool = False
    RUN_PORT: int = 5000
    TIME_ZONE: str = "Asia/Taipei"

    # Request
    REQUEST_VERIFY_SSL: bool = True
    REQUEST_PROXY: str = ''
    REQUEST_RETRY: int = 5
    REQUEST_CONN_TIMEOUT: float = 5
    REQUEST_READ_TIMEOUT: float = 5
    REQUEST_WRITE_TIMEOUT: float = 5
    REQUEST_POOL_TIMEOUT: float = 5

    # AWS
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_KEY: str = ""
    AWS_REGION: str = ""
    AWS_PARAMETER_PATH_PREFIX: str = ""
    AWS_LOGGROUP_NAME: str = ""

    # MongoDB
    DATABASE_URL: str = ""
    DATABASE_NAME: str = ""

    class Config:
        case_sensitive = False
