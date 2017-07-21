from pyramid.config import Configurator
from pyramid.events import NewRequest

def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, X-Requested-With',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.include('.models')
    config.include('.routes')
    config.include('.security')
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)
    # config.add_static_view(name='static', path='static')
    # config.add_static_view("static", "static")
    config.scan()
    return config.make_wsgi_app()
