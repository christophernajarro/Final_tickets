from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
from database import SessionLocal, engine
import models
from schemas import TicketCreate, Ticket
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tickets/", response_model=Ticket)
def create_ticket(ticket: TicketCreate):
    db = SessionLocal()
    db_ticket = crud.create_ticket(db=db, ticket=ticket)
    db.close()
    return db_ticket

@app.get("/tickets/", response_model=List[Ticket])
def read_tickets(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    tickets = crud.get_tickets(db, skip=skip, limit=limit)
    db.close()
    return tickets

@app.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket: TicketCreate):
    db = SessionLocal()
    db_ticket = crud.update_ticket(db=db, ticket_id=ticket_id, ticket=ticket)
    db.close()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    db = SessionLocal()
    result = crud.delete_ticket(db=db, ticket_id=ticket_id)
    db.close()
    if not result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"detail": "Ticket deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
