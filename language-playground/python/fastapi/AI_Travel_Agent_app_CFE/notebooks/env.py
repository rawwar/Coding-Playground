import pathlib
from decouple import Config, RepositoryEnv

BASE_DIR = pathlib.Path(__file__).parent.parent

MY_ENV_FILE =  BASE_DIR / ".env"


def get_config():
    if MY_ENV_FILE.exists():
        return Config(RepositoryEnv(MY_ENV_FILE))
    from decouple import config as _decouple_config
    return _decouple_config

config = get_config()