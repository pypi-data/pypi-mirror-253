from __future__ import annotations


from hx_markup.element import NodeText
from markdown import markdown
from ormspace import model as md


from hx_markup import Element
from typing_extensions import Self

from spacestar import detail_url_template_var, htmx_indicator_template_var, htmx_target_template_var, \
    htmx_url_template_var


class SpaceModel(md.Model):
    
    async def setup_instance(self):
        await self.set_instance_dependencies()

    
    def element_detail(self) -> Element:
        container: Element = Element('div', id=self.tablekey)
        container.children.append(Element('h3', children=str(self)))
        for k, v in self.model_fields.items():
            if value:= getattr(self, k):
                container.children.append(f"""
                ##### {v.title or k}
                {markdown(value)}
                """)
        # container.children.append(Element('ul', '.list-group', children=[Element('li','.list-group-item', children=f'{markdown(f"""# {k}""")}') for k, v in dict(self).items() if v]))
        return container
    
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