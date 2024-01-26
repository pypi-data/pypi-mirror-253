from __future__ import annotations

import os.path
from collections import defaultdict
from contextlib import asynccontextmanager
from contextvars import ContextVar
from functools import wraps
from typing import Any, Optional

import jinja2
import uvicorn
from hx_markup import Element
from markupsafe import Markup
from ormspace import functions
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Mount, Route, Router
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.datastructures import FormData
from ormspace.settings import Settings

from spacestar.model import SpaceModel

response_contextvar = ContextVar("response_contextvar", default={})

def app_context(request: Request) -> dict[str, Any]:
    return {'app': request.app}

@asynccontextmanager
async def response_context(request: Request, **kwargs):
    response_token = response_contextvar.set(kwargs)
    try:
        yield request.app.response(request, **response_contextvar.get())
    finally:
        response_contextvar.reset(response_token)



class SpaceStar(Starlette):
    """SpaceStar class is a mix of Starlette and Uvicorn for faster run of HTTP server configured for Deta Space.
    Parameters:
    module - A string with the module name running the application. Defaults to "main".
    app_name - A string with the SpaceStar instance name. Defaults to "app".
    lang - Language of the application. Defaults to "en".
    title - The title for home page. Defaults to "SpaceStar".
    static_directory - A string indicating the location of static folder, relative to working directory.
    templates_directory - A string indicating the location of jinja2 templates_directory.
    index_template - index template as a string.
    debug - Boolean indicating if debug tracebacks should be returned on errors.
    routes - A list of routes to serve incoming HTTP and WebSocket requests.
    middleware - A list of middleware to run for every request. A starlette application will always automatically include two middleware classes. ServerErrorMiddleware is added as the very outermost middleware, to handle any uncaught errors occurring anywhere in the entire stack. ExceptionMiddleware is added as the very innermost middleware, to deal with handled exception cases occurring in the routing or endpoints.
    exception_handlers - A mapping of either integer status codes, or exception class types onto callables which handle the exceptions. Exception handler callables should be of the form handler(request, exc) -> response and may be either standard functions, or async functions.
    on_startup - A list of callables to run on application startup. Startup handler callables do not take any arguments, and may be either standard functions, or async functions.
    on_shutdown - A list of callables to run on application shutdown. Shutdown handler callables do not take any arguments, and may be either standard functions, or async functions.
    lifespan - A lifespan context function, which can be used to perform startup and shutdown tasks. This is a newer style_path that replaces the on_startup and on_shutdown handlers. Use one or the other, not both.
    """
    def __init__(self, **kwargs):
        self.settings = Settings()
        middleware = kwargs.pop('middleware', [])
        middleware.insert(0, Middleware(SessionMiddleware, secret_key=self.settings.session_secret))
        self.module: str = kwargs.pop('module', 'main')
        self.app_name: str = kwargs.pop('app_name', 'app')
        self.lang: str = kwargs.pop('lang', 'en')
        self.title: str = kwargs.pop('title', 'SpaceStar')
        self.static_directory: Optional[str] = kwargs.pop('static_directory', None)
        self.templates_directory: Optional[str] = kwargs.pop('templates_directory', None)
        self.index_template: Optional[str] = kwargs.pop('index_template', None)
        self._page_content = None
        self._page_title = None
        if self.templates_directory:
            self.templates = Jinja2Templates(
                    directory=os.path.join(os.getcwd(), self.templates_directory),context_processors=[app_context])
        else:
            self.templates = Jinja2Templates(
                    env=jinja2.Environment(), context_processors=[app_context])
            
        if all([self.templates_directory is None, self.index_template is None]):
            raise ValueError('SpaceStar requires either templates_directory or index_template')

        super().__init__(middleware=middleware, **kwargs)
        if self.static_directory:
            self.routes.insert(1, Mount(
                    '/static',
                    app=StaticFiles(directory=os.path.join(os.getcwd(), self.static_directory)),
                    name='static'))
    
    def set_global(self, name, value):
        self.templates.env.globals[name] = value
        
    @property
    def page_content(self):
        try:
            return self._page_content
        finally:
            self._page_content = ''
    
    @page_content.setter
    def page_content(self, value: Markup):
        self._page_content = value
    
    @property
    def page_title(self):
        try:
            return self._page_title
        finally:
            self._page_title = ''
    
    @page_title.setter
    def page_title(self, value: Markup):
        self._page_title = value
        
    
    def from_string(self, source: str):
        return self.templates.env.from_string(source=source, globals=self.globals)
    
    @property
    def globals(self):
        return self.templates.env.globals
    
    @property
    def index_from_string(self):
        return self.from_string(self.index_template)

    @property
    def index(self) -> jinja2.Template:
        if self.templates_directory:
            return self.templates.get_template('index.html')
        return self.index_from_string

    @staticmethod
    def element(tag, *args, **kwargs):
        return Element(tag, *args, **kwargs)

    def render(self, request, / , template: str = None, source: str = None, **kwargs) -> str:
        kwargs['app'] = request.app
        kwargs['request'] = request
        kwargs['id'] = functions.random_id(4)
        if template:
            return self.templates.get_template(template).render(**kwargs)
        elif source:
            return self.from_string(source=source).render(**kwargs)
        return self.index.render(**kwargs)

    def response(self, request: Request, *, template: str = None, source: str = None, **kwargs) -> HTMLResponse:
        return HTMLResponse(self.render(request, template=template, source=source, **kwargs))

    def run(self, *args, **kwargs):
        if args:
            string = ':'.join(args)
        else:
            string = f'{self.module}:{self.app_name}'
        port = kwargs.pop('port', self.settings.port)
        uvicorn.run(string, port=port, **kwargs)
        
    @staticmethod
    def write_query(data: dict) -> str:
        return functions.write_query(data)
    
    @staticmethod
    def markup_detail(instance: SpaceModel):
        return Markup(instance.element_detail())
    
    @staticmethod
    def markup_list_item(instance: SpaceModel):
        return Markup(instance.element_list_group_item())
    
    @staticmethod
    def markup_item_link(instance: SpaceModel, href: str):
        return Markup(instance.element_list_group_item_action(href=href))
    
    @staticmethod
    def markup_htmx_action(instance: SpaceModel, href: str, target: str, indicator: str):
        return Markup(instance.element_list_group_item_htmx_action(href=href, target=target, indicator=indicator))

    def create_route(self, path: str, *, name: str = None, methods: list[str] = None):
        def decorator(endpoint):
            @wraps(endpoint)
            def wrapper():
                self.append(Route(path=path, endpoint=endpoint, name=name, methods=methods or ['GET']))
                return self
            return wrapper()
        return decorator

    def append(self, app: Route | Mount | Router) -> None:
        self.routes.append(app)

    def prepend(self, app: Route | Mount | Router) -> None:
        self.routes.insert(0, app)
        
    def insert(self, index: int, app: Route | Mount) -> None:
        self.routes.insert(index, app)
        
    @staticmethod
    async def process_form_data(request: Request) -> dict:
        form_data: FormData = await request.form()
        data, result = defaultdict(list), {}
        for key, value in form_data.items():
            data[key].append(value)
        for key in data:
            if not key == 'search':
                value = data[key]
                if len(value) == 0:
                    result[key] = None
                elif len(value) == 1:
                    result[key] = value[0]
                else:
                    result[key] = value
        return result
        
    @property
    def E(self):
        return Element


