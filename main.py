from ableton.v2.control_surface import ControlSurface
from .log import log


class Algorave(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance)
        with self.component_guard():
            self.log = log
            self.log('Starting ...')
