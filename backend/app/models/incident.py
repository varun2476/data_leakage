from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, nullable=False)

    receiver_email = Column(String, nullable=False)

    sender_email = Column(String, nullable=True)

    risk_level = Column(String, nullable=False)

    detected_data = Column(Text)

    message = Column(Text)

    status = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)