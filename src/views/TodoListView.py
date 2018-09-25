from json import dumps
from logging import getLogger

from aiohttp.web import Response, View, json_response

from src.models import Task

logger = getLogger(__name__)


class TodoListView(View):
    async def get(self):
        return json_response(Task.all_objects())

    async def post(self):
        content = await self.request.json()
        return json_response(
            Task.create_object(content, self.request.app.router['todo'].url_for)
        )

    async def delete(self):
        Task.delete_all_objects()
        return Response()