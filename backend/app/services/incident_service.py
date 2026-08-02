from sqlalchemy.orm import Session

from app.models.incident import Incident

from app.services.admin_alert import send_admin_alert


def create_incident(db: Session, incident_data,data):

    incident=Incident(

    employee_id=data.employee_id,

    file_name=data.file_name,

    receiver_email=data.receiver_email,

    risk_level=data.risk_level,

    status=data.status,

    detected_data=data.detected_data,

    llm_prediction=data.llm_prediction,

    confidence=data.confidence,

    confidentiality=data.confidentiality

)

    db.add(incident)

    db.commit()

    db.refresh(incident)

    if incident_data.status == "BLOCKED":

        send_admin_alert(

            employee_id=incident_data.employee_id,

            sender_email=incident_data.sender_email,

            receiver_email=incident_data.receiver_email,

            risk_level=incident_data.risk_level,

            detected_data=incident_data.detected_data,

            ml_prediction=data.ml_prediction,
            
            confidence=data.confidence,
            
            filename=data.filename,
            

            message=incident_data.message

        )

    return incident