from sqlalchemy.orm import Session

from app.models.incident import Incident

from app.services.admin_alert import send_admin_alert


def create_incident(db: Session, incident_data):

    incident = Incident(

        employee_id=incident_data.employee_id,

        receiver_email=incident_data.receiver_email,

        sender_email=incident_data.sender_email,

        risk_level=incident_data.risk_level,

        detected_data=incident_data.detected_data,

        message=incident_data.message,

        status=incident_data.status
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

            message=incident_data.message

        )

    return incident