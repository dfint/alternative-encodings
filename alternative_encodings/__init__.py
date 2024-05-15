import cp859
import cp866i
import romaji
import viscii


def register_all():
    cp859.register()
    cp866i.register()
    romaji.register()
    viscii.register()
