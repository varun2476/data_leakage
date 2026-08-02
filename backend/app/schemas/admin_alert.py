from pydantic import BaseModel
from typing import Any

class AlertRequest(BaseModel):

    employee_id: int

    file_name: str

    risk_level: str

    detected_data: Any

    sender_email: str

    receiver_email: str

    file_content: str