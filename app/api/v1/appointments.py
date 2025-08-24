from fastapi import APIRouter, BackgroundTasks, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.session import get_db
from typing import Optional

router = APIRouter()

class AppointmentCreate(BaseModel):
    staffId: str
    date: str    # YYYY-MM-DD
    time: str    # HH:MM

class AppointmentOut(BaseModel):
    id: str
    staffId: str
    date: str
    time: str
    status: str = "pending"
    message: Optional[str] = None

def _fallback_process(payload: AppointmentCreate):
    # placeholder xử lý nền nếu không có service: log / gửi queue...
    print("Processing appointment (fallback):", payload.dict())

@router.post("/appointments", status_code=status.HTTP_202_ACCEPTED, response_model=AppointmentOut)
def create_appointment(
    req: AppointmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    Nhận yêu cầu đặt lịch từ client. Trả về 202 và thêm tác vụ xử lý nền.
    Nếu bạn có app.services.appointment_service thì hàm sẽ cố gọi các hàm đó.
    """
    # Cố gắng dùng service nếu có, nếu không thì dùng fallback
    try:
        # import động để tránh lỗi import khi service chưa tồn tại
        from app.services import appointment_service  # type: ignore

        # nếu service có create_request trả về dict/obj đại diện appointment, dùng nó
        if hasattr(appointment_service, "create_request"):
            appt = appointment_service.create_request(db, req)  # nên trả về dict/obj serializable
            # schedule processing (service xử lý nền nếu cần)
            if hasattr(appointment_service, "process_request"):
                background_tasks.add_task(appointment_service.process_request, db, appt)
            else:
                background_tasks.add_task(_fallback_process, req)
            # normalize trả về AppointmentOut-compatible dict
            if isinstance(appt, dict):
                return {**{"status": "pending"}, **appt}
            return appt
        else:
            # service không có create_request — fallback
            background_tasks.add_task(_fallback_process, req)
    except Exception:
        background_tasks.add_task(_fallback_process, req)

    # trả về id tạm thời (client hiểu là accepted)
    temp_id = f"tmp-{req.staffId}-{req.date.replace('-','')}-{req.time.replace(':','')}"
    return AppointmentOut(id=temp_id, staffId=req.staffId, date=req.date, time=req.time, status="pending", message="accepted")