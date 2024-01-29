from midpoint_cli.client import MidpointCommunicationObserver


class ConsoleDisplay(MidpointCommunicationObserver):
    def __init__(self):
        self._waiting = False

    def on_http_error(self):
        if self._waiting:
            print('.', end='', flush=True)
        else:
            print('Waiting for http service...', end='', flush=True)
            self._waiting = True

    def on_http_success(self):
        if self._waiting:
            print('', flush=True)
            self._waiting = False

    def on_http_call(self):
        pass
