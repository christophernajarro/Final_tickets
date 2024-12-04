from pydantic import BaseModel

class TicketBase(BaseModel):
    concert_name: str
    user_name: str = None
    status: str

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True
