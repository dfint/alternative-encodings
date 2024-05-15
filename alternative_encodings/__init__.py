from . import cp859
from . import cp866i
from . import romaji
from . import viscii


def register_all():
    cp859.register()
    cp866i.register()
    romaji.register()
    viscii.register()
