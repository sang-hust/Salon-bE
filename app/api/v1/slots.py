# app/api/v1/slots.py
from fastapi import APIRouter, Query
router = APIRouter()

@router.get("")
def slots(staff_id: str = Query(...), date: str = Query(...)):
    # TODO: lấy từ DB; tạm trả mock
    return ["09:00","09:30","10:00","10:30","11:00","14:00","14:30","15:00"]
