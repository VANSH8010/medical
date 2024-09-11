from typing import List

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from backend.schemas import PatientCreate, PatientRead
from backend.crud import insert_patient, find_all_patients, find_patient_by_id, update_patient, delete_patient

router = APIRouter()

@router.post("/patients", response_model=PatientRead)
async def create_patient(patient: PatientCreate):
    return insert_patient(patient)

@router.get("/patients", response_model=List[PatientRead])
async def get_patients():
    return find_all_patients()

@router.get("/patients/{patient_id}", response_model=PatientRead)
async def get_patient(patient_id: str):
    return find_patient_by_id(patient_id)

@router.put("/patients/{patient_id}", response_model=PatientRead)
async def update_patient(patient_id: str, patient: PatientCreate):
    return update_patient(patient_id, patient)

@router.delete("/patients/{patient_id}", response_model=PatientRead)
async def delete_patient(patient_id: str):
    return delete_patient(patient_id)

