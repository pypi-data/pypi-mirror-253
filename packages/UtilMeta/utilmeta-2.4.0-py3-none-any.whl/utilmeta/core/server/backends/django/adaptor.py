import inspect
# import re

import django
import sys
from functools import update_wrapper
from django.http.response import HttpResponseBase
from django.core.management import execute_from_command_line
from django.utils.deprecation import MiddlewareMixin
from django.urls import re_path

from utilmeta import UtilMeta
from utilmeta.core.orm.backends.django.database import DjangoDatabaseAdaptor
from utilmeta.core.request.backends.django import DjangoRequestAdaptor
from utilmeta.core.response.backends.django import DjangoResponseAdaptor
from utilmeta.core.api import API
from utilmeta.utils import Header, localhost, pop
from utilmeta.core.response import Response
from utilmeta.core.server.backends.base import ServerAdaptor
from .settings import DjangoSettings


class DebugCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response: HttpResponseBase):
        origin = request.headers.get(Header.ORIGIN)
        if origin and localhost(origin):
            for key in response.cookies.keys():
                cookie = response.cookies[key]
                pop(cookie, 'domain')
                if not localhost(request.get_host()):
                    cookie['samesite'] = 'None'
        return response


class DjangoServerAdaptor(ServerAdaptor):
    backend = django
    request_adaptor_cls = DjangoRequestAdaptor
    response_adaptor_cls = DjangoResponseAdaptor
    sync_db_adaptor_cls = DjangoDatabaseAdaptor
    default_asynchronous = False
    URLPATTERNS = 'urlpatterns'
    DEFAULT_PORT = 8000
    DEFAULT_HOST = '127.0.0.1'

    def __init__(self, config: UtilMeta):
        super().__init__(config)
        self._ready = False
        self.settings = config.get_config(DjangoSettings) or DjangoSettings()
        self.app = None

    def setup(self):
        if self._ready:
            return
        self.settings.setup(self.config)
        self.add_api(
            self.config.resolve(),
            route='(.*)',
            asynchronous=self.asynchronous
        )
        self._ready = True

    def adapt(self, api: 'API', route: str, asynchronous: bool = None):
        if asynchronous is None:
            asynchronous = self.default_asynchronous
        func = self._get_api(api, asynchronous=asynchronous)
        path = f'{route.strip("/")}/(.*)' if route.strip('/') else '(.*)'
        return re_path(path, func)

    def add_api(self, utilmeta_api_class, route: str = '', asynchronous: bool = False):
        api = self._get_api(utilmeta_api_class, asynchronous=asynchronous)
        api_path = re_path(route, api)
        urls = getattr(self.settings.url_conf, self.URLPATTERNS, [])
        if api_path not in urls:
            urls.append(api_path)
        setattr(self.settings.url_conf, self.URLPATTERNS, urls)

    def _get_api(self, utilmeta_api_class, asynchronous: bool = False):
        """
        Mount a API class
        make sure it is called after all your fastapi route is set
        """
        from utilmeta.core.api.base import API
        if not issubclass(utilmeta_api_class, API):
            raise TypeError(f'Invalid api class: {utilmeta_api_class}')

        if asynchronous:
            async def f(request, route: str = '', *args, **kwargs):
                try:
                    req = self.request_adaptor_cls(request, self.load_route(route), *args, **kwargs)
                    root = utilmeta_api_class(req)
                    resp = await root()
                except Exception as e:
                    resp = getattr(utilmeta_api_class, 'response', Response)(error=e)
                return self.response_adaptor_cls.reconstruct(resp)
        else:
            def f(request, route: str = '', *args, **kwargs):
                try:
                    req = self.request_adaptor_cls(request, self.load_route(route), *args, **kwargs)
                    root = utilmeta_api_class(req)
                    resp = root()
                except Exception as e:
                    resp = getattr(utilmeta_api_class, 'response', Response)(error=e)
                return self.response_adaptor_cls.reconstruct(resp)

        update_wrapper(f, utilmeta_api_class, updated=())
        f.csrf_exempt = True  # noqa
        # as this f() of RootAPI is the only callable return to set url
        # csrf_exempt must set to True or every result without token will be blocked
        return f

    def application(self):
        self.setup()
        if self.app:
            return self.app
        if self.asynchronous:
            from django.core.handlers.asgi import ASGIHandler
            self.app = ASGIHandler()
        else:
            from django.core.handlers.wsgi import WSGIHandler
            self.app = WSGIHandler()
        # return self.app
        return self.app

    def run(self):
        self.setup()
        if not self.background:
            self.config.startup()
            if self.asynchronous:
                try:
                    from daphne.server import Server
                except ModuleNotFoundError:
                    pass
                else:
                    print('using [daphne] as asgi server')
                    try:
                        Server(
                            application=self.application(),
                            endpoints=[self.daphne_endpoint],
                            server_name=self.config.name,
                        ).run()
                    finally:
                        self.config.shutdown()
                    return

                try:
                    import uvicorn
                except ModuleNotFoundError:
                    pass
                else:
                    print('using [uvicorn] as asgi server')
                    try:
                        uvicorn.run(
                            self.application(),
                            host=self.config.host or self.DEFAULT_HOST,
                            port=self.config.port or self.DEFAULT_PORT,
                        )
                    finally:
                        self.config.shutdown()
                        return

            if self.config.production:
                server = 'asgi (like uvicorn/daphne)' if self.asynchronous else 'wsgi (like uwsgi/gunicorn)'
                raise ValueError(f'django in production cannot use service.run(), please use an {server} server')
            else:
                if self.asynchronous:
                    raise ValueError(f'django debug runserver does not support asgi, please use an asgi server')
                try:
                    self.runserver()
                finally:
                    self.config.shutdown()
                    return
        else:
            pass

    @property
    def location(self):
        return f'{self.config.host or self.DEFAULT_HOST}:{self.config.port or self.DEFAULT_PORT}'

    @property
    def daphne_endpoint(self):
        return f"tcp:{self.config.port or self.DEFAULT_PORT}:interface={self.config.host or self.DEFAULT_HOST}"

    def runserver(self):
        # debug server
        argv = [sys.argv[0], 'runserver', self.location] if len(sys.argv) == 1 else sys.argv
        if 'runserver' in argv:
            if not self.config.auto_reload:
                argv.append('--noreload')

        execute_from_command_line(argv)
