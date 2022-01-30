import socket
import errno


class DebugServer(object):
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setblocking(0)
        self._remote_debug_addr = ("127.0.0.1", 9001)
        self._local_addr = ("127.0.0.1", 9000)
        try:
            self._socket.bind(self._local_addr)
            self.log("DebugServer started")
        except Exception as e:
            self.log("DebugServer Error binding! %s" % e)

    def end_debug_process(self):
        self._socket.close()

    def begin_debug_process(self):
        try:
            while True:
                data, addr = self._socket.recvfrom(1024)
                result = eval(data)
                self._client.sendto(
                    str(result).encode("utf-8"), self._remote_debug_addr
                )
        except socket.error as e:
            if e.errno == errno.EAGAIN:
                pass
        except Exception as e:
            msg = "Error handling debug message %s" % e
            self._client.sendto(msg.encode("utf-8"), self._remote_debug_addr)
            self.log(msg)
        # calling itself again
        self.schedule_message(1, self.begin_debug_process)
