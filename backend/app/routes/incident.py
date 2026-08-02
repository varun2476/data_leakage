from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.incident import Incident
from pydantic import BaseModel


router = APIRouter(
    prefix="/incident",
    tags=["Incident"]
)



class IncidentCreate(BaseModel):

    employee_id: int

    file_name: str

    receiver_email: str

    risk_level: str

    status: str

    detected_data: str

    llm_prediction: str

    confidence: str

    confidentiality: str

    action: str



@router.post("/create")
def create_incident(
    data:IncidentCreate,
    db:Session=Depends(get_db)
):

    incident = Incident(

    employee_id=data.employee_id,

    file_name=data.file_name,

    receiver_email=data.receiver_email,

    risk_level=data.risk_level,

    status=data.status,

    detected_data=data.detected_data,

    llm_prediction=data.llm_prediction,

    confidence=data.confidence,

    confidentiality=data.confidentiality,

    action=data.action,

     )


    db.add(incident)

    db.commit()

    db.refresh(incident)


    return {
        "message":"Incident saved",
        "id":incident.id
    }