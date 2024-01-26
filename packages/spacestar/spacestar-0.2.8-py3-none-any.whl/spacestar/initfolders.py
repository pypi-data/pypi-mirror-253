import os

import hx_markup
import spacestar


def create_templates_directory():
    os.makedirs(os.path.join(os.getcwd(), 'templates'), exist_ok=True)
    with open(os.path.join(os.getcwd(), 'templates', 'index_from_string.html'), 'w') as f:
        f.write('<!doctype html>')
        f.write(str(hx_markup.Element('html', children=[
                hx_markup.Element('head', children=[spacestar.META_CHARSET, spacestar.META_VIEWPORT,spacestar.BOOTSTRAP_LINK, spacestar.HEAD_STYLE_LINK, spacestar.HEAD_SCRIPT]),
                hx_markup.Element('body', 'body', children=[
                        hx_markup.Element('nav', 'nav'),
                        hx_markup.Element('main', 'main'),
                        hx_markup.Element('footer', 'footer'),
                        '<script type="text/javascript" src="/static/js/body.js"></script>'
                ])
        ])))

def create_static_directory():
    os.makedirs(os.path.join(os.getcwd(), 'static/css'), exist_ok=True)
    os.makedirs(os.path.join(os.getcwd(), 'static/js'), exist_ok=True)
    os.makedirs(os.path.join(os.getcwd(), 'static/img'), exist_ok=True)
    with open(os.path.join(os.getcwd(), 'static', 'css/main.css'), 'w') as f:
        f.write('html, body {padding: 0; margin: 0; box-sizing: border-box}')
    with open(os.path.join(os.getcwd(), 'static', 'js/main.js'), 'w') as f:
        f.write('const body = document.getElementById("body")')
        
        
def main():
    create_templates_directory()
    create_static_directory()
    
if __name__ == '__main__':
    main()
