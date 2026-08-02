from fastapi import APIRouter
from datetime import datetime

from app.services.admin_alert import send_admin_alert
from app.schemas.admin_alert import AlertRequest

router = APIRouter(
    prefix="/admin",
    tags=["Admin Alert"]
)

@router.post("/alert")
def admin_alert(data: AlertRequest):

    print("==============================")
    print("🚨 ADMIN ALERT RECEIVED")
    print("==============================")
    print(f"👤 Employee ID      : {data.employee_id}")
    print(f"📄 File Name        : {data.file_name}")
    print(f"⚠️ Risk Level       : {data.risk_level}")
    print(f"🔍 Detected Data    : {data.detected_data}")
    print(f"📧 Sender Email     : {data.sender_email}")
    print(f"📨 Receiver Email   : {data.receiver_email}")
    print(f"📄 File Content:\n{data.file_content}")
    print("==============================")

    try:

        send_admin_alert(
            employee_id=data.employee_id,
            file_name=data.file_name,
            risk_level=data.risk_level,
            detected_data=data.detected_data,
            sender_email=data.sender_email,
            receiver_email=data.receiver_email,
            file_content=data.file_content
        )

        return {
            "status": True,
            "message": "Admin notified successfully",
            "alert_time": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        }

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }