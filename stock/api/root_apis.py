from sanic import Blueprint, Sanic
from sanic.log import logger
from sanic.response import json

# logger = logging.getLogger(__name__)

bp_root = Blueprint('root', url_prefix='')

@bp_root.get('/hello')
async def hello(request):
    username = request.json
    return json({"result": "successful"}, status=200)