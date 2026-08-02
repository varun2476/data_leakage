from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import get_db


from app.models.employee import Employee


from app.schemas.employee import (
    EmployeeRegister,
    EmployeeLogin
)


from app.services.employee_service import (
    create_employee,
    get_employee_by_email
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



# ==========================
# REGISTER
# ==========================

@router.post("/register")
def register(
    employee: EmployeeRegister,
    db: Session = Depends(get_db)
):

    user = get_employee_by_email(
        db,
        employee.email
    )


    if user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    

    new_user = create_employee(
    db,
    employee
)


    return {

        "message": "Registration successful",

        "employee_id": new_user.id

    }



# ==========================
# LOGIN
# ==========================
@router.post("/login")
def login(
    login_data: EmployeeLogin,
    db: Session = Depends(get_db)
):


    # Find employee by email

    employee = db.query(Employee).filter(
        Employee.email == login_data.email
    ).first()



    if employee is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )



    # Password check

    if employee.password != login_data.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )



    # Role check

    if employee.role.lower() != login_data.role.lower():

        raise HTTPException(
            status_code=403,
            detail="Invalid role selected"
        )



    return {

        "message": "Login successful",

        "user_id": employee.id,

        "role": employee.role,

        "email": employee.email,

        "department": employee.department,

    

    }