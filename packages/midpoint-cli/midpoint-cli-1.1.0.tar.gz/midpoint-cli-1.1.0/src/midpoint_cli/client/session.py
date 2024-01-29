import typing

from requests.adapters import HTTPAdapter
from urllib3 import Retry

from midpoint_cli.client import MidpointCommunicationObserver


class CustomRetryManager(Retry):

    def __init__(self, observer: MidpointCommunicationObserver = None, **kwargs):
        self._observer = observer
        super(CustomRetryManager, self).__init__(**kwargs)

    def get_backoff_time(self):
        return 2

    def new(self, **kw: typing.Any) -> Retry:
        result = super(CustomRetryManager, self).new(**kw)
        result._observer = self._observer
        return result

    def increment(self, *args, **kwargs) -> Retry:
        self._observer.on_http_error()
        return super(CustomRetryManager, self).increment(*args, **kwargs)


class CustomHTTPAdapter(HTTPAdapter):

    def __init__(self, observer: MidpointCommunicationObserver, **kwargs):
        super(CustomHTTPAdapter, self).__init__(**kwargs)
        self._observer = observer

    def send(self, request, **kwargs):
        self._observer.on_http_call()
        response = super(CustomHTTPAdapter, self).send(request, **kwargs)
        self._observer.on_http_success()
        return response
