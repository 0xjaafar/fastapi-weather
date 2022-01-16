from xml.dom import ValidationErr
import httpx
from typing import Optional
from httpx import Response

from models.validation_error import ValidationError

api_key: Optional[str] = None


async def get_report(city, country: str, state: Optional[str], units: Optional[str]) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={q}&APPID={api_key}'
    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(error_msg= resp.text, status_code= resp.status_code)

    data = resp.json() 
    forecast = data['main']  
    return forecast