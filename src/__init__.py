from logging import getLogger, basicConfig, INFO
from os import getenv
from aiohttp import web
import aiohttp_cors
from aiohttp_swagger import setup_swagger


from .views.TodoListView import TodoListView
from .views.TodoTaskView import TodoTaskView

IP = getenv('IP', '0.0.0.0')
PORT = getenv('PORT', '8000')

basicConfig(level=INFO)
logger = getLogger(__name__)


async def init(loop):
    app = web.Application(loop=loop)

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })

    # Routes
    #app.router.add_route('*', '/', IndexView)
    #app.router.add_route('*', '/{uuid}', TodoView)
    # Explicitly add individual methods, see https://github.com/aio-libs/aiohttp-cors/issues/41
    cors.add(app.router.add_route('get', '/todos/', TodoListView))
    cors.add(app.router.add_route('post', '/todos/', TodoListView))
    cors.add(app.router.add_route('delete', '/todos/', TodoListView))
    cors.add(app.router.add_route('get', '/todos/{uuid}', TodoTaskView, name='todo'))
    cors.add(app.router.add_route('patch', '/todos/{uuid}', TodoTaskView))
    cors.add(app.router.add_route('delete', '/todos/{uuid}', TodoTaskView))

    # Config
    setup_swagger(app, swagger_url="/api/v1/doc", swagger_from_file="swagger.yaml")
    logger.info("Starting server at %s:%s", IP, PORT)
    srv = await loop.create_server(app.make_handler(), IP, PORT)
    return srv