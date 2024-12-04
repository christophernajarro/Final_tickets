from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
from database import SessionLocal, engine
import models
from schemas import TicketCreate, Ticket
import crud
import logging
from datetime import datetime

# Configure logging
log_filename = datetime.now().strftime("log_%d_%m_%Y.log")
logging.basicConfig(
    filename=f"/app/logs/{log_filename}",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Disable create_all since Alembic handles migrations
# models.Base.metadata.create_all(bind=engine)
print("Tables will be created via Alembic migrations.")

app = FastAPI()

@app.post("/tickets/", response_model=Ticket)
def create_ticket(ticket: TicketCreate):
    try:
        db = SessionLocal()
        db_ticket = crud.create_ticket(db=db, ticket=ticket)
        db.close()
        logging.info("Éxito en Ejecución")
        return db_ticket
    except Exception as e:
        logging.error(f"Error en Ejecución: {e}")
        raise HTTPException(status_code=500, detail=str(e))

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

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
