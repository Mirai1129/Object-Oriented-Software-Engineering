from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from rollcallsystem.core.security import (
    create_access_token,
    verify_password
)
from rollcallsystem.database import get_db
from rollcallsystem.models import User
from rollcallsystem.schemas import Token

router = APIRouter(prefix="/api/auth")


@router.post("/token", response_model=Token)
async def token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    # Find the user by account (username)
    user = db.query(User).filter(User.account == form_data.username).first()

    # Check if user exists and password is correct
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.account})

    return {"access_token": access_token, "token_type": "bearer"}
