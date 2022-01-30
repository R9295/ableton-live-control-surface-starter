from ableton.v2.control_surface import ControlSurface
from .log import log
from .debug import DebugServer

class MyControlSurface(ControlSurface, DebugServer):
    def __init__(self, c_instance):
        self.log = log
        super().__init__(c_instance)
        with self.component_guard():
            self.begin_debug_process()
            self.log('Initializing app ...')

    def disconnect(self):
        self.log('Disconnecting ...')
        super().disconnect()
        self.end_debug_process()
