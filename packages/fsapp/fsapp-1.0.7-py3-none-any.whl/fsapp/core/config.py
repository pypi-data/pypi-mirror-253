"""Класс настроек приложения API"""
import toml

from dynaconf import Dynaconf
from pathlib import Path

SETTINGS = {
    "required": {
        "instance": 'Default_Project'
    },
    "optional": {
    }
}

SECRETS = {
    "auth": {
        "username": "user",
        "password": "202cb962ac59075b964b07152d234b70",
    }
}

SETTINGS_PATH = Path('settings.toml')
SECRET_PATH = Path('.secrets.toml')


def create_settings_files():
    if SETTINGS_PATH.exists() and SECRET_PATH.exists():
        return None
    else:
        with SETTINGS_PATH.open('wt') as f:
            toml.dump(SETTINGS, f)
        with SECRET_PATH.open('wt') as f:
            toml.dump(SECRETS, f)
        print("INFO: Созданы файлы настроек settigns.toml и .secrets.toml\n"
              "Заполните их перед запуском приложения!\n\n"
              "Добавленные вами настройки доступны из объекта settings")
        raise SystemExit


settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[SETTINGS_PATH, SECRET_PATH]
)
