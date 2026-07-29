from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.incident import Incident

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/employee/{employee_id}")
def employee_dashboard(employee_id: int, db: Session = Depends(get_db)):

    total_scans = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).count()

    blocked_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        Incident.status == "BLOCKED"
    ).count()

    safe_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        Incident.status == "SAFE"
    ).count()

    risk_score = 0

    if total_scans > 0:
        risk_score = round((blocked_files / total_scans) * 100)

    return {
        "total_scans": total_scans,
        "safe_files": safe_files,
        "blocked_files": blocked_files,
        "risk_score": risk_score
    }