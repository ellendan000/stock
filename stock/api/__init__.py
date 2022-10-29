from sanic import Blueprint
from .root_apis import bp_root

api = Blueprint.group(bp_root, url_prefix='/api')