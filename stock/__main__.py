import jwt
from sanic import Sanic
from sanic.log import logger
from sanic.response import json
from .api import api
from .config import keyvault_cache

app = Sanic(name="StockAzureApp")
app.blueprint(api)

@app.on_request
async def run_before_handler(request):
    if request.token == None:
      return json({'result': 'abandon'}, 401)
    print(keyvault_cache.get('jwt-secret'))
    print(request.token)

    service_token = jwt.decode(request.token, keyvault_cache.get('jwt-secret'), algorithms=['HS256'])
    if service_token != { 'token': keyvault_cache.get('mock-account-token') }:
      return json({'result': 'abandon'}, 403)

@app.on_response
async def add_content_type_header(request, response):
    response.headers['Content-Type'] = 'application/json;charset=utf-8'

@app.route("/")
async def findGraph(request):
  return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, access_log=True)