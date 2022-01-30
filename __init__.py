from .main import Algorave
from .log import clear_log

def create_instance(c_instance):
    clear_log()
    return Algorave(c_instance)
