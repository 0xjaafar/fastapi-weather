from optparse import Option
import fastapi 
from fastapi import Depends
from typing import Optional
from models.location import Location

from services.openweather_service import get_report

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    report = await get_report(city = loc.city,
                        state = loc.state,
                        country= loc.country,
                        units= units)
    return report