from __future__ import annotations

from typing import Any

from hx_markup.element import NodeText
from markdown import markdown
from ormspace import model as md


from hx_markup import Element
from typing_extensions import Self

from spacestar import detail_url_template_var, htmx_indicator_template_var, htmx_target_template_var, \
    htmx_url_template_var


class SpaceModel(md.Model):
    
    async def setup_instance(self):
        pass
        
    @staticmethod
    def list_group_item(label: str, content: Any) -> Element:
        return Element('li', '.list-group-item', Element('span', '.text-darkorange', NodeText(f'{label}: ')), NodeText(str(content)))
    
    def children_elements(self) -> list[Element]:
        return [

        ]
    
    def container_element(self) -> Element:
        return Element('ul', '.list-group', children=self.children_elements())
    
    def element_detail(self) -> Element:
        return Element('div', f'#{self.tablekey} .card .bg-dark bg-opacity-50', children=[
                Element('div', '.card-header', NodeText(str(self))),
                Element('div', '.card-body', self.container_element()),
        ])

    
    def element_list_group_item(self) -> Element:
        return Element('li', '.list-group-item', NodeText(str(self)))
    
    def element_list_group_item_action(self):
        template = detail_url_template_var.get()
        return Element('li', '.list-group-item',
                       Element('a', '.list-group-item-action',
                               href=template.format(item_name=self.item_name(), item_key=self.key),
                               children=str(self)))

    def element_list_group_item_htmx_action(self):
        template = htmx_url_template_var.get()
        target = htmx_target_template_var.get()
        indicator = htmx_indicator_template_var.get()
        return Element('li', '.list-group-item', Element('a', '.list-group-item-action', htmx={
                'target': target.format(item_name=self.item_name()),
                'get': template.format(item_name=self.item_name(), item_key=self.key),
                'indicator': indicator.format(item_name=self.item_name())
        }, children=str(self)))
    
    @classmethod
    def element_list_group(cls, instances: list[Self]):
        return Element('ul', '.list-group', children=[
                item.element_list_group_item() for item in instances
        ])
    
    
class SpaceSearchModel(SpaceModel, md.SearchModel):
    pass