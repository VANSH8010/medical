from bson import ObjectId
from fastapi import HTTPException
from backend.models import collection
from backend.schemas import PatientCreate

def insert_patient(patient: PatientCreate):
    result = collection.insert_one(patient.dict())
    return {**patient.dict(), "id": str(result.inserted_id)}

def find_all_patients():
    return [{"id": str(patient["_id"]), "name": patient["name"], "age": patient["age"]} for patient in collection.find()]

def find_patient_by_id(patient_id: str):
    try:
        patient = collection.find_one({"_id": ObjectId(patient_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"id": str(patient["_id"]), "name": patient["name"], "age": patient["age"]}

def update_patient(patient_id: str, patient: PatientCreate):
    try:
        result = collection.update_one({"_id": ObjectId(patient_id)}, {"$set": patient.dict()})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    updated_patient = collection.find_one({"_id": ObjectId(patient_id)})
    return {"id": str(updated_patient["_id"]), "name": updated_patient["name"], "age": updated_patient["age"]}

def delete_patient(patient_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(patient_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"id": patient_id, "message": "Patient deleted successfully"}
