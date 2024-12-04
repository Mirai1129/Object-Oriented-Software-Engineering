from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Union

from rollcallsystem.database import get_db
from rollcallsystem.core.security import (
    create_access_token,
    verify_password,
    get_password_hash
)
from rollcallsystem.models import User

router = APIRouter(prefix="/api/auth")

class LoginResponse:
    def __init__(self, access_token: str, token_type: str = "bearer"):
        self.access_token = access_token
        self.token_type = token_type

@router.post("/login")
def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    """
    Authenticate user and return an access token

    Args:
        form_data (OAuth2PasswordRequestForm): Contains username and password
        db (Session): Database session dependency

    Returns:
        dict: Access token and token type

    Raises:
        HTTPException: If authentication fails
    """
    # Find user by username (assuming username is used for login)
    user = db.query(User).filter(User.account == form_data.username).first()

    # Check if user exists and password is correct
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # Generate access token
    access_token = create_access_token(
        data={"sub": str(user.account)}  # Use user ID as subject
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
