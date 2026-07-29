from sqlalchemy.orm import Session

from app.models.employee import Employee

from app.security import hash_password



def create_employee(db, employee):


    new_employee = Employee(

        name=employee.name,

        email=employee.email,

        password=employee.password,

        role=employee.role

    )


    try:

        db.add(new_employee)

        db.commit()

        db.refresh(new_employee)


        return new_employee


    except Exception as e:

        db.rollback()

        raise e




def get_employee_by_email(
    db,
    email
):

    return db.query(Employee).filter(
        Employee.email==email
    ).first()
