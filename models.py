from sqlalchemy import Column, Integer, String
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    concert_name = Column(String, index=True)
    user_name = Column(String, index=True)
    status = Column(String, index=True)
