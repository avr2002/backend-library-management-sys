from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Query
from models.students import Student, UpdateStudent
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId
from typing import Optional
# from routes.rate_limit import rate_limit


router = APIRouter()


# @rate_limit(key_prefix="rate_limit", max_requests=2, expire_time=10)
@router.post("/students", status_code=status.HTTP_201_CREATED)
async def add_student(student: Student):
    student_dict = student.dict()
    inserted_student = collection_name.insert_one(student_dict)

    return {
        "id": str(inserted_student.inserted_id)
    }


# @rate_limit(key_prefix="rate_limit", max_requests=2, expire_time=10)
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


# @rate_limit(key_prefix="rate_limit", max_requests=2, expire_time=10)
@router.get("/students/{id}", status_code=status.HTTP_200_OK)
async def get_student(id: str):
    student = individual_serial(collection_name.find_one({"_id": ObjectId(id)}))
    student.pop('id')
    return student


# @rate_limit(key_prefix="rate_limit", max_requests=2, expire_time=10)
@router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(id: str, student: UpdateStudent):
    student_data = student.dict(exclude_unset=True)

    existing_student = collection_name.find_one({"_id": ObjectId(id)})

    if 'address' in student_data:
        updated_address = student_data['address']
        if not 'city' in updated_address:
            updated_address['city'] = existing_student['address']['city']

        if not 'country' in updated_address:
            updated_address['country'] = existing_student['address']['country']

        student_data['address'] = updated_address

    collection_name.find_one_and_update({"_id": ObjectId(id)},
                                        {"$set": student_data})

    return


# @rate_limit(key_prefix="rate_limit", max_requests=2, expire_time=10)
@router.delete("/students/{id}", status_code=status.HTTP_200_OK)
async def delete_student(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return
