from .ankiaddonconfig import ConfigManager 
from . import colors 

conf = ConfigManager() 
colors.recolor_python()
colors.recolor_web()

from . import menu
from . import config
