from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.database import get_db
from app.models.incident import Incident


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


# ==========================
# EMPLOYEE DASHBOARD
# ==========================

@router.get("/employee/{employee_id}")
def employee_dashboard(
    employee_id: int,
    db: Session = Depends(get_db)
):

    # Total scans

    total_scans = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).count()


    # Safe files

    safe_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.upper(Incident.status) == "SAFE"
    ).count()



    # Blocked files

    blocked_files = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.upper(Incident.status) == "BLOCKED"
    ).count()



    # High + Critical files

    high_risk = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.upper(Incident.risk_level).in_(
            [
                "HIGH",
                "CRITICAL"
            ]
        )
    ).count()



    # Critical only

    critical_risk = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.upper(Incident.risk_level) == "CRITICAL"
    ).count()



    # Risk percentage

    risk_score = 0

    if total_scans > 0:

        risk_score = round(
            (high_risk / total_scans) * 100
        )



    # Latest scan

    latest = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).order_by(
        Incident.created_at.desc()
    ).first()



    last_file = (
        latest.file_name
        if latest
        else "No File"
    )



    last_scan = (
        latest.created_at
        if latest
        else None
    )



    # Today scans

    today_scans = db.query(Incident).filter(
        Incident.employee_id == employee_id,
        func.date(Incident.created_at)
        == date.today()
    ).count()



    return {


        "total_scans": total_scans,


        "safe_files": safe_files,


        "blocked_files": blocked_files,


        "risk_score": risk_score,


        "high_risk": high_risk,


        "critical_risk": critical_risk,


        "today_scans": today_scans,


        "last_file": last_file,


        "last_scan": last_scan

    }
# ==========================
# EMPLOYEE RECENT ACTIVITY
# ==========================

@router.get("/employee/{employee_id}/recent")
def recent_activity(
    employee_id:int,
    db:Session = Depends(get_db)
):

    incidents = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).order_by(
        Incident.created_at.desc()
    ).limit(2).all()


    return [

        {
            "Date": incident.created_at,
            "File": incident.file_name,
            "Receiver": incident.receiver_email,
            "Action": incident.action

        }

        for incident in incidents

    ]
# ==========================
# EMPLOYEE HISTORY
# ==========================

@router.get("/employee/{employee_id}/history")
def employee_history(
    employee_id:int,
    db:Session = Depends(get_db)
):

    incidents = db.query(Incident).filter(
        Incident.employee_id == employee_id
    ).order_by(
        Incident.created_at.desc()
    ).all()


    return [

        {
            "Date": incident.created_at,
            "File Name": incident.file_name,
            "Receiver Email": incident.receiver_email,
             "Action": incident.action

        }

        for incident in incidents

    ]
# ==========================
# ADMIN RISK ANALYTICS
# ==========================


@router.get("/admin/risk")
def admin_risk_analytics(
    db:Session = Depends(get_db)
):


    low = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "LOW"
    ).count()



    medium = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "MEDIUM"
    ).count()



    high = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "HIGH"
    ).count()



    critical = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "CRITICAL"
    ).count()



    safe = db.query(Incident).filter(
        func.upper(Incident.status)
        == "SAFE"
    ).count()



    blocked = db.query(Incident).filter(
        func.upper(Incident.status)
        == "BLOCKED"
    ).count()



    bypassed = db.query(Incident).filter(
        func.upper(Incident.status)
        == "BYPASSED"
    ).count()



    total = db.query(Incident).count()



    risk_score = 0


    if total > 0:

        risk_score = round(
            ((high + critical) / total)
            * 100
        )



    return {


        "low":low,


        "medium":medium,


        "high":high,


        "critical":critical,


        "safe":safe,


        "blocked":blocked,


        "bypassed":bypassed,


        "risk_score":risk_score

    }





# ==========================
# ADMIN LOGS
# ==========================


@router.get("/admin/logs")
def admin_system_logs(
    db:Session = Depends(get_db)
):


    logs = db.query(Incident).order_by(
        Incident.created_at.desc()
    ).limit(20).all()



    return [

        {


        "Date":
        log.created_at,


        "Employee ID":
        log.employee_id,


        "Receiver":
        log.receiver_email,


        "Risk":
        log.risk_level,


        "Status":
        log.status,


        "Action":
        log.action


        }


        for log in logs

    ]
# ==========================
# ADMIN RISK ANALYTICS
# ==========================


@router.get("/admin/risk")
def admin_risk_analytics(
    db:Session = Depends(get_db)
):


    low = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "LOW"
    ).count()



    medium = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "MEDIUM"
    ).count()



    high = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "HIGH"
    ).count()



    critical = db.query(Incident).filter(
        func.upper(Incident.risk_level)
        == "CRITICAL"
    ).count()



    safe = db.query(Incident).filter(
        func.upper(Incident.status)
        == "SAFE"
    ).count()



    blocked = db.query(Incident).filter(
        func.upper(Incident.status)
        == "BLOCKED"
    ).count()



    bypassed = db.query(Incident).filter(
        func.upper(Incident.status)
        == "BYPASSED"
    ).count()



    total = db.query(Incident).count()



    risk_score = 0


    if total > 0:

        risk_score = round(
            ((high + critical) / total)
            * 100
        )



    return {


        "low":low,


        "medium":medium,


        "high":high,


        "critical":critical,


        "safe":safe,


        "blocked":blocked,


        "bypassed":bypassed,


        "risk_score":risk_score

    }





# ==========================
# ADMIN LOGS
# ==========================


@router.get("/admin/logs")
def admin_system_logs(
    db:Session = Depends(get_db)
):


    logs = db.query(Incident).order_by(
        Incident.created_at.desc()
    ).limit(20).all()



    return [

        {


        "Date":
        log.created_at,


        "Employee ID":
        log.employee_id,


        "Receiver":
        log.receiver_email,


        "Risk":
        log.risk_level,


        "Status":
        log.status,


        "Action":
        log.action


        }


        for log in logs

    ]
# ==========================
# ADMIN DASHBOARD SUMMARY
# ==========================

from app.models.employee import Employee


@router.get("/admin")
def admin_dashboard(
    db: Session = Depends(get_db)
):

    # Total employees

    employees = db.query(Employee).count()


    # Active users
    # assuming all employees are active

    active_users = db.query(Employee).filter(
    Employee.status.isnot(None),
    func.upper(Employee.status) == "ACTIVE"
).count()



    # Total scans

    total_scans = db.query(Incident).count()



    # Blocked files

    blocked = db.query(Incident).filter(
        func.upper(Incident.status) == "BLOCKED"
    ).count()



    # Alerts
    # HIGH + CRITICAL incidents

    alerts = db.query(Incident).filter(
        func.upper(Incident.risk_level).in_(
            [
                "HIGH",
                "CRITICAL"
            ]
        )
    ).count()



    # Today's incidents

    today_incidents = db.query(Incident).filter(
        func.date(Incident.created_at)
        == date.today()
    ).count()



    return {

        "employees": employees,

        "active_users": active_users,

        "total_scans": total_scans,

        "blocked": blocked,

        "alerts": alerts,

        "today_incidents": today_incidents

    }