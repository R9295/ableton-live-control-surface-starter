from .main import MyControlSurface
from .log import clear_log


def create_instance(c_instance):
    clear_log()
    return MyControlSurface(c_instance)
