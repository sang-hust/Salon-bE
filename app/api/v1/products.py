# app/api/v1/products.py
from fastapi import APIRouter
router = APIRouter()

@router.get("")
def list_products():
    return [
        { "id": "p1", "name": "Shampoo Repair", "price": 199000 },
        { "id": "p2", "name": "Hair Oil Glow", "price": 249000 },
        { "id": "p3", "name": "Nail Care Kit", "price": 99000 },
    ]

