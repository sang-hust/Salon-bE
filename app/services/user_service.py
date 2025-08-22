from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.security import hash_password, verify_password, create_access_token
from app.repositories import user_repo
from app.models.user import UserRole, User

def register(db: Session, username: str, email: str, password: str) -> str:
    if user_repo.get_by_email(db, email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email đã tồn tại")
    if user_repo.get_by_username(db, username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username đã tồn tại")

    hashed = hash_password(password)
    user = user_repo.create_user(db, username=username, email=email, password_hash=hashed, role=UserRole.user)
    token = create_access_token(subject=str(user.id))
    return token

def login(db: Session, email: str, password: str) -> str:
    user = user_repo.get_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sai email hoặc mật khẩu")
    token = create_access_token(subject=str(user.id))
    return token

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()
