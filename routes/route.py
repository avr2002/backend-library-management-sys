from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Query
from models.students import Student, UpdateStudent
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId
from typing import Optional

router = APIRouter()


@router.post("/students", status_code=status.HTTP_201_CREATED)
async def add_student(student: Student):
    student_dict = student.dict()
    inserted_student = collection_name.insert_one(student_dict)

    return {
        "id": str(inserted_student.inserted_id)
    }


@router.get("/students", status_code=status.HTTP_200_OK)
async def get_students(country: Optional[str] = Query(None, description="Filter by country"),
                       age: Optional[int] = Query(None, description="Filter by minimum age")):
    filter_params = {}
    if country:
        filter_params['address.country'] = country
    if age:
        filter_params['age'] = {"$gte": age}

    students = list_serial(collection_name.find(filter_params))
    return {
        "data": students
    }


@router.get("/students/{id}", status_code=status.HTTP_200_OK)
async def get_student(id: str):
    student = individual_serial(collection_name.find_one({"_id": ObjectId(id)}))
    student.pop('id')
    return student


@router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(id: str, student: UpdateStudent):
    student_data = student.dict(exclude_unset=True)
    result = collection_name.find_one_and_update({"_id": ObjectId(id)},
                                                 {"$set": student_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    return


@router.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def delete_student(id: str):
    result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    if result.modified_count == 0:
        raise HTTPException(status_code=204, detail="Student not found")

    return
