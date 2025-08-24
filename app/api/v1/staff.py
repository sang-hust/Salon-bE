# app/api/v1/staff.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db

router = APIRouter()

@router.get("")
def list_staff(db: Session = Depends(get_db)):
    return [
        {
            "id": "s1",
            "name": "Linh Phan",
            "role": "Senior Nail Artist",
            "bio": "10+ years crafting Gel-X and hand-painted designs. Friendly, detail-obsessed, and great with custom sets.",
            "bio_vi": "Hơn 10 năm kinh nghiệm Gel-X và vẽ tay tỉ mỉ. Tư vấn nhiệt tình, chuyên set thiết kế theo yêu cầu.",
            "languages": ["vi", "en"],
            "specialties": ["Gel-X", "Hand-painted art", "Ombré", "Builder Gel Overlay"],
            "can_do_services": [
                "svc-gelx", "svc-gel-mani", "svc-builder-overlay",
                "add-full-art", "add-french", "svc-gel-removal",
                "svc-classic-mani", "svc-polish-change-hands"
            ],
            "years_experience": 10,
            "rating": 4.9,
            "seniority": "senior",
            "price_multiplier": 1.20,
            "aliases": ["Linh", "chị Linh"],
            "image_url": None
        },
        {
            "id": "s2",
            "name": "Minh Anh",
            "role": "Gel Color Specialist",
            "bio": "Known for flawless gel color application and long-lasting shine. Minimalist to bold palettes.",
            "bio_vi": "Chuyên gia sơn gel bền đẹp, lên màu chuẩn từ tối giản đến nổi bật.",
            "languages": ["vi", "en"],
            "specialties": ["Gel Color", "French Tips", "Quick-dry Top"],
            "can_do_services": [
                "svc-gel-mani", "svc-gel-pedi", "add-french",
                "svc-gel-removal", "svc-classic-mani", "svc-classic-pedi"
            ],
            "years_experience": 6,
            "rating": 4.8,
            "seniority": "mid",
            "price_multiplier": 1.10,
            "aliases": ["Minh Anh"],
            "image_url": None
        },
        {
            "id": "s3",
            "name": "Hà My",
            "role": "Nail Artist",
            "bio": "Delicate linework and cute decals. Great for K-beauty inspired sets and short nails.",
            "bio_vi": "Vẽ nét mảnh, decal xinh, hợp style Hàn và móng ngắn.",
            "languages": ["vi", "en"],
            "specialties": ["Simple Art", "Full-set Art", "K-style"],
            "can_do_services": [
                "add-simple-art", "add-full-art", "svc-classic-mani",
                "svc-polish-change-hands", "svc-kids-mani", "svc-gel-mani"
            ],
            "years_experience": 4,
            "rating": 4.7,
            "seniority": "mid",
            "price_multiplier": 1.05,
            "aliases": ["Hamy", "Hà-My"],
            "image_url": None
        },
        {
            "id": "s4",
            "name": "Quang Dũng",
            "role": "Spa Pedicure Technician",
            "bio": "Gentle, hygienic spa pedicures with careful callus care. Customer-first, relaxing experience.",
            "bio_vi": "Chăm sóc chân kỹ, vệ sinh chuẩn, mài gót nhẹ nhàng – trải nghiệm thư giãn.",
            "languages": ["vi", "en"],
            "specialties": ["Spa Pedicure", "Callus Care", "Paraffin"],
            "can_do_services": [
                "svc-classic-pedi", "svc-gel-pedi", "add-callus",
                "add-paraffin", "svc-polish-change-toes", "svc-gel-removal"
            ],
            "years_experience": 7,
            "rating": 4.8,
            "seniority": "senior",
            "price_multiplier": 1.15,
            "aliases": ["Dũng"],
            "image_url": None
        },
        {
            "id": "s5",
            "name": "Thu Trang",
            "role": "Acrylic Master",
            "bio": "Sculpted acrylics with durable shape and balance. Loves modern square and almond forms.",
            "bio_vi": "Chuyên đắp bột form chuẩn, bền đẹp; yêu thích dáng vuông và almond hiện đại.",
            "languages": ["vi", "en"],
            "specialties": ["Acrylic Full Set", "Acrylic Refill", "Sculpting"],
            "can_do_services": [
                "svc-acrylic-full", "svc-acrylic-refill", "svc-acrylic-removal",
                "add-full-art", "add-french", "svc-polish-change-hands"
            ],
            "years_experience": 8,
            "rating": 4.85,
            "seniority": "senior",
            "price_multiplier": 1.20,
            "aliases": ["Trang"],
            "image_url": None
        },
        {
            "id": "s6",
            "name": "Kim Chi",
            "role": "Junior Technician",
            "bio": "Fast and neat polish changes; great with kids’ services and simple gel sets.",
            "bio_vi": "Đổi sơn nhanh gọn, làm dịch vụ trẻ em và gel đơn giản tốt.",
            "languages": ["vi", "en"],
            "specialties": ["Polish Change", "Kids Manicure", "Basic Gel"],
            "can_do_services": [
                "svc-polish-change-hands", "svc-polish-change-toes",
                "svc-kids-mani", "svc-classic-mani", "svc-gel-mani"
            ],
            "years_experience": 2,
            "rating": 4.6,
            "seniority": "junior",
            "price_multiplier": 0.95,
            "aliases": ["Chi"],
            "image_url": None
        },
    ]
