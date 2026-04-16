from aqt import mw
from aqt.utils import openLink
from aqt.qt import QMenu, QAction

from .config import conf


def get_anking_menu() -> QMenu:
    """Return AnKing menu. If it doesn't exist, create one. Make sure its submenus are up to date."""
    menu_name = "Theme"
    menubar = mw.form.menubar
    for a in menubar.actions():
        if menu_name == a.text():
            menu = a.parent()
            break
    else:
        menu = menubar.addMenu(menu_name)
    return menu


########################################


def setupMenu() -> None:
    menu = get_anking_menu()
    a = QAction("ReColor", menu)
    a.triggered.connect(conf.open_config)
    menu.addAction(a)


setupMenu()
