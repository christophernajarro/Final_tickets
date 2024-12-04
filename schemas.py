from pydantic import BaseModel
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    available = 'available'
    reserved = 'reserved'
    purchased = 'purchased'

class TicketBase(BaseModel):
    concert_name: str
    user_name: Optional[str] = None
    status: StatusEnum

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        from_attributes = True