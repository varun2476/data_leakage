from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class Employee(Base):

    __tablename__ = "employee"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )


    name = Column(
        String,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        nullable=False
    )


    password = Column(
        String,
        nullable=False
    )


    department = Column(
        String,
        nullable=True
    )


    role = Column(
        String,
        
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    status = Column(String)