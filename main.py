from urllib.request import Request
import fastapi
import uvicorn
from views import home
from app import weather_api
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles


api = fastapi.FastAPI()

def configure():
    configure_routing()

def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)





if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()