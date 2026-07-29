from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.incident import IncidentCreate, IncidentResponse
from app.services.incident_service import create_incident

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.post("/process", response_model=IncidentResponse)
def process_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    return create_incident(db, incident)