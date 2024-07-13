from . import cp859, cp866i, romaji, viscii


def register_all():
    cp859.register()
    cp866i.register()
    romaji.register()
    viscii.register()
