
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
from os import path, environ


base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
load_dotenv(path.join(base_dir, ".env"))


@dataclass
class Config:
    
    """ Basic Configuration"""

    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):

    database = environ.get("DATABASE")
    username = environ.get("DB_USERNAME")
    password = environ.get("DB_PASSWORD")

 
    PROJ_RELOAD: bool = True
    DB_URL: str = f"postgresql+psycopg2://{username}:{password}@localhost:5432/{database}"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


def conf():

    """ Call Environment """

    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))