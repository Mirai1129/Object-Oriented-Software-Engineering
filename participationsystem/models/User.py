from typing import Any

from sqlalchemy import Column, String, Integer

from ..database import Base


class User(Base):
    __tablename__ = "User"

    account = Column(String(50), primary_key=True)
    password = Column(String(255), nullable=False)
    role = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    def __init__(self, account: str, password: str, **kw: Any):
        super().__init__(**kw)
        self.account = account
        self.password = password
