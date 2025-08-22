# app/api/v1/staff.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db

router = APIRouter()

@router.get("")
def list_staff(db: Session = Depends(get_db)):
    return [
        {"id": "s1", "name": "Linh Phan", "role": "Senior Stylist"},
        {"id": "s2", "name": "Minh Anh", "role": "Color Specialist"},
        {"id": "s3", "name": "Hà My", "role": "Nail Artist"},
    ]
