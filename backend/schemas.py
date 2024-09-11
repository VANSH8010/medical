from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int

class PatientRead(BaseModel):
    id: str
    name: str
    age: int

    class Config:
        orm_mode = True
