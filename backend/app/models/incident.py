from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer)

    file_name = Column(String)

    receiver_email = Column(String)

    risk_level = Column(String)

    status = Column(String,
                   nullable=False, 
                    )


    detected_data = Column(Text)
    action = Column(
    String,
    nullable=True
)
    llm_prediction = Column(String)

    confidence = Column(String)

    confidentiality = Column(String)

    

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )