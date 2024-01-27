from contextlib import contextmanager
from contextvars import ContextVar

detail_url_template_var = ContextVar('detail_url_template_var', default='/api/{}/{}')
htmx_url_template_var = ContextVar('htmx_url_template_var', default='/api/{}/{}')
htmx_target_template_var = ContextVar('htmx_target_template_var', default='#htmx-{}-container')
htmx_indicator_template_var = ContextVar('htmx_indicator_template_var', default='#htmx-{}-indicator')

@contextmanager
def detail_url_context(template: str):
    token = detail_url_template_var.set(template)
    try:
        yield
    finally:
        detail_url_template_var.reset(token)
        
@contextmanager
def htmx_url_context(template: str):
    token = htmx_url_template_var.set(template)
    try:
        yield
    finally:
        htmx_url_template_var.reset(token)


@contextmanager
def htmx_target_context(template: str):
    token = htmx_target_template_var.set(template)
    try:
        yield
    finally:
        htmx_target_template_var.reset(token)
        
@contextmanager
def htmx_indicator_context(template: str):
    token = htmx_indicator_template_var.set(template)
    try:
        yield
    finally:
        htmx_indicator_template_var.reset(token)


if __name__ == '__main__':
    with htmx_url_context('/doctor/{}/{}'):
        with htmx_target_context('#htmx-{}'):
            print(htmx_url_template_var.get().format('invoice', 'xdrerer'))
            print(htmx_target_template_var.get().format('invoice'))
    
