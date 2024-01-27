from __future__ import annotations

from abc import ABC, abstractmethod

from hx_markup import Element, functions
from hx_markup.element import Div, NodeText
from jinja2 import Template
from lxml import etree
from lxml.builder import E
from markupsafe import Markup
from ormspace.alias import QUERIES
from ormspace.model import getmodel
from starlette.requests import Request
from starlette.responses import HTMLResponse

from spacestar.app import SpaceStar



class ResponseEngine(ABC):
    def __init__(self, request: Request, template_path: str = None, source: str = None):
        self.request = request
        self.app: SpaceStar = self.request.app
        self.template_path = template_path
        self.source = source
        
    @property
    def engine(self) -> Template:
        if self.template_path and self.app.templates_directory:
            return self.app.templates.get_template(self.template_path)
        elif self.source:
            return self.app.from_string(self.source)
        return self.app.index
    
    @abstractmethod
    async def template_data(self) -> dict:
        raise NotImplementedError
    
    async def run(self):
        return self.engine.render(request=self.request, **await self.template_data())

        
class ModelResponse(ResponseEngine):
    def __init__(self, request: Request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.model = getmodel(self.request.path_params.get('item_name'))

    async def update_dependencies(self, lazy=False, queries: QUERIES | None = None):
        await self.model.update_dependencies_context(queries=queries, lazy=lazy)
    
    @property
    def fields(self):
        return self.model.model_fields.values()
    
    @property
    def query(self):
        result = self.model.query_from_request(request=self.request)
        return result
    
    @property
    def path(self):
        return self.request.url.path
    
    @property
    def field_names(self):
        return self.model.model_fields.keys()
    
    async def instances(self, lazy=False):
        return await self.model.sorted_instances_list(query=self.query, lazy=lazy)

    async def run(self):
        if self.template_path:
            return HTMLResponse(self.app.render(self.request, template=self.template_path, **await self.template_data()))
        elif self.source:
            return HTMLResponse(self.app.templates.from_string(self.source).render(request=self.request, **await self.template_data()))
        return self.app.response(self.request, **await self.template_data())

    
    async def template_data(self) -> dict:
        return {'model': self.model}
    

    
class ListResponse(ModelResponse):
    
    async def template_data(self) -> dict:
        return {
                'header': Element('header', Div('.container-fluid', Element('h1', NodeText(self.app.title)))),
                'content': Markup(etree.tounicode(
                        E.div(
                                E.h2(f'lista de {self.model.plural()}'),
                                E.ul(*[E.li(f'{i.key} {i}', {'class': 'list-group-item text-white'}) for i in
                                       await self.instances()],
                                     {'class': 'list-group', 'style': 'overflow-y: auto; max-height: 80%;'})
                        
                        ))
                        
                ),
                'footer': etree.tounicode(E.footer(f'resultados para {functions.write_args(self.query.values())}', id='footer'))
        }
        

class SearchResponse(ModelResponse):
    async def element(self):
        page = E.div(
                E.h4('resultado de pesquisa de {}'.format(self.model).title()),
        )
        return page
    

