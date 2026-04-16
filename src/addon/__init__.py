from .ankiaddonconfig import ConfigManager
from .migrate import maybe_migrate_config

conf = ConfigManager()

from . import colors
from . import menu
from . import config
