from email.mime import application
from optparse import Option
import fastapi 
from fastapi import Depends
from typing import Optional
from models.location import Location
from models.validation_error import ValidationError
from fastapi.responses import JSONResponse
from services.openweather_service import get_report

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await get_report(city = loc.city,
                        state = loc.state,
                        country= loc.country,
                        units= units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    