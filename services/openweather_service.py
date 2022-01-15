import httpx
from typing import Optional

api_key: Optional[str] = None


async def get_report(city, country: str, state: Optional[str], units: Optional[str]) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={q}&APPID={api_key}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
    data = resp.json()
    forecast = data['main']  
    return forecast