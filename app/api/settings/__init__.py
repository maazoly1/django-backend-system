import os.path
from pathlib import Path
from split_settings.tools import include, optional
from app.general.utils.pytest import is_pytest_running

# Adjust the base directory to be two levels up from the current file (api/settings/__init__.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent # extra parent

ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS'

LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTINGS_PREFIX}_LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = f'local/settings{'.unittests' if is_pytest_running() else '.dev'}.py'

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str((BASE_DIR / LOCAL_SETTINGS_PATH).resolve())


include(
    'base.py',
    'logging.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envvars.py',
    'docker.py',
)

if not is_pytest_running():
    assert SECRET_KEY is not NotImplemented # type: ignore