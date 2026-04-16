from .ankiaddonconfig import ConfigManager 
from . import colors 
from colors import recolor_python, recolor_web 

conf = ConfigManager() 
colors.recolor_python()
colors.recolor_web()

from . import menu
from . import config
