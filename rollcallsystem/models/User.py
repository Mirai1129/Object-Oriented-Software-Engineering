from typing import Any

from sqlalchemy import Column, String, Integer

from rollcallsystem.database import Base


class User(Base):
    __tablename__ = 'User'

    account = Column(String, primary_key=True)
    password = Column(String)
    role = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
    }

    def __init__(self, account: str, password: str, **kw: Any):
        super().__init__(**kw)
        self.account = account
        self.password = password
