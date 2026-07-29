from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.database import get_db

from app.models.incident import Incident
from app.models.employee import Employee
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/employee/{employee_id}")
def employee_dashboard(
    employee_id: int,
    db: Session = Depends(get_db)
):

    # Total scans done by employee
    total_scans = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).count()


    # Count blocked files (case-insensitive)
    blocked_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.lower(Incident.status) == "blocked"
    ).count()


    # Count safe files (case-insensitive)
    safe_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.lower(Incident.status) == "safe"
    ).count()


    # Calculate risk percentage
    risk_score = 0

    if total_scans > 0:
        risk_score = round(
            (blocked_files / total_scans) * 100
        )


    return {
        "total_scans": total_scans,
        "safe_files": safe_files,
        "blocked_files": blocked_files,
        "risk_score": risk_score
    }

@router.get("/employee/{employee_id}/recent")
def recent_activity(
    employee_id: int,
    db: Session = Depends(get_db)
):

    incidents = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).order_by(
        Incident.created_at.desc()
    ).limit(2).all()


    return [
        {
            "Date": incident.created_at,
            "Receiver": incident.receiver_email,
            "Risk": incident.risk_level,
            "Status": incident.status
        }
        for incident in incidents
    ]
@router.get("/employee/{employee_id}/history")
def employee_history(
    employee_id: int,
    db: Session = Depends(get_db)
):

    incidents = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).order_by(
        Incident.created_at.desc()
    ).all()


    return [
        {
            "Date": incident.created_at,
            "Receiver": incident.receiver_email,
            "Risk": incident.risk_level,
            "Status": incident.status
        }
        for incident in incidents
    ]
@router.get("/admin")
def admin_dashboard(
    db: Session = Depends(get_db)
):

    # Total employees
    total_employees = db.query(Employee).count()


    # Active users
    active_users = db.query(Employee).filter(
        Employee.role == "user"
    ).count()


    # Total scans
    total_scans = db.query(Incident).count()


    # Blocked attempts
    blocked_attempts = db.query(Incident).filter(
        func.lower(Incident.status) == "blocked"
    ).count()


    # Critical alerts
    critical_alerts = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "critical"
    ).count()



    # Today's incidents

    today_incidents = db.query(Incident).filter(
        func.date(Incident.created_at) == date.today()
    ).count()



    return {

        "employees": total_employees,

        "active_users": active_users,

        "total_scans": total_scans,

        "blocked": blocked_attempts,

        "alerts": critical_alerts,

        "today_incidents": today_incidents

    }
@router.get("/admin/risk")
def admin_risk_analytics(
    db: Session = Depends(get_db)
):

    low = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "low"
    ).count()


    medium = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "medium"
    ).count()


    high = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "high"
    ).count()


    critical = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "critical"
    ).count()


    safe = db.query(Incident).filter(
        func.lower(Incident.risk_level) == "safe"
    ).count()


    return {

        "low": low,

        "medium": medium,

        "high": high,

        "critical": critical,

        "safe": safe

    }
@router.get("/admin/logs")
def admin_system_logs(
    db: Session = Depends(get_db)
):

    logs = db.query(Incident).order_by(
        Incident.created_at.desc()
    ).limit(20).all()


    return [

        {
            "Date": log.created_at,
            "Employee ID": log.employee_id,
            "Receiver": log.receiver_email,
            "Risk": log.risk_level,
            "Status": log.status
        }

        for log in logs

    ]