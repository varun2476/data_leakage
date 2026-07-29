from sqlalchemy import Column, Integer, String

from app.database import Base

class Employee(Base):

    __tablename__ = "employees"


    id = Column(
        Integer,
        primary_key=True,
        index=True
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
        String
    )


    role = Column(
        String,
        default="employee"
    )