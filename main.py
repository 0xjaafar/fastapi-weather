import json
from shutil import ExecError
import fastapi
import uvicorn
from views import home
from app import weather_api
from fastapi.staticfiles import StaticFiles
from services   import openweather_service
from pathlib import Path
api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()

def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print('settings.json file not found, you cannot continue.')
        raise Exception('settings.json file not found, you cannot continue.')

    with open('settings.json') as f:
        settings = json.load(f)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()