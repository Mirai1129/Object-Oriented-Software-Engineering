from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from participationsystem.core.security import (
    create_access_token,
    verify_password
)
from participationsystem.database import get_db
from participationsystem.models import User
from participationsystem.schemas import Token

router = APIRouter()


@router.post("/token", response_model=Token)
async def token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.account == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.account, "role": user.role})

    return {"access_token": access_token, "token_type": "bearer"}
