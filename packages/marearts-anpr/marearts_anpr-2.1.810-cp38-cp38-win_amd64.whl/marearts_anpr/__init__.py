
#__init__.py
from .version import __version__
from .marearts_anpr import marearts_anpr as MareArtsAnprClass
def MareArtsAnpr(nation="kr", id="", key="", display_license_info=False):
    return MareArtsAnprClass(nation, id, key, display_license_info)


