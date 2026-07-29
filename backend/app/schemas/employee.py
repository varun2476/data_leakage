from pydantic import BaseModel,EmailStr



class EmployeeRegister(BaseModel):

    name:str

    email:EmailStr

    password:str

    role:str="user"
    
    department:str



class EmployeeLogin(BaseModel):

    email:EmailStr

    password:str

    role:str