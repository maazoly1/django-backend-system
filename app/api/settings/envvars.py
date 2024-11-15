from core.utils.collections import deep_update
from core.utils.settings import get_settings_by_environment

# globals() store the dictionary in a global variable
deep_update(globals(), get_settings_by_environment(ENVVAR_SETTINGS_PREFIX)) # type: ignore