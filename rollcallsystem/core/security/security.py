import os
from datetime import datetime, timedelta
from typing import Optional

from dotenv import load_dotenv
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from rollcallsystem.database import get_db
from rollcallsystem.models import User, Teacher, Student

load_dotenv()

SECRET_KEY = os.getenv("ROLLCALL_SECRET")
ALGORITHM = "HS256"  # JWT encoding algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hashed version.

    Args:
        plain_password (str): The plain password input by the user.
        hashed_password (str): The hashed password stored in the database.

    Returns:
        bool: Returns True if the passwords match, otherwise False.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a password for storing in the database.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.

    Args:
        data (dict): The data to be encoded into the token.
        expires_delta (Optional[timedelta], optional): The expiration time for the token. Defaults to 15 minutes.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def authenticate_user(db: Session, account: str, password: str):
    """
    Authenticate the user by verifying the account and password.

    Args:
        db (Session): The database session to query the database.
        account (str): The account (username) provided by the user.
        password (str): The password provided by the user.

    Raises:
        HTTPException: If the credentials are invalid, raises a 401 Unauthorized exception.

    Returns:
        User: The authenticated user object if credentials are correct.
    """
    user = db.query(User).filter(User.account == account).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    """
    Get the current authenticated user based on the provided JWT token.

    Args:
        token (str): The JWT token passed in the request header.
        db (Session): The database session to query the database.

    Raises:
        HTTPException: If the token is invalid or the user cannot be found, raises a 401 Unauthorized exception.

    Returns:
        User: The authenticated user object, either a Teacher or Student.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        account: str = payload.get("sub")
        if account is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.account == account).first()

    if user and user.role == 1:
        return Teacher(id=user.account, account=user.account, password=user.password)
    else:
        return Student(id=user.account, account=user.account, password=user.password)
