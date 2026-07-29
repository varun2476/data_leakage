from pydantic import BaseModel
from datetime import datetime


class IncidentCreate(BaseModel):

    employee_id: int

    receiver_email: str

    sender_email: str

    risk_level: str

    detected_data: str

    message: str

    status: str


class IncidentResponse(BaseModel):

    id: int

    employee_id: int

    receiver_email: str

    sender_email: str

    risk_level: str

    detected_data: str

    message: str

    status: str

    created_at: datetime

    

    class Config:
        from_attributes = True