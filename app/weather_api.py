from optparse import Option
import fastapi 
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
from models.location import Location


router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    return f'{loc.city}, {loc.state}, {loc.country} in {units}'