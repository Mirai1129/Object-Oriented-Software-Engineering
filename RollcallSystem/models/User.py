from typing import Any

from sqlalchemy import Column, String
from RollcallSystem.database import Base


class User(Base):
    __tablename__ = 'user'

    account = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, account: str, password: str, **kw: Any):
        super().__init__(**kw)
        self.account = account
        self.password = password
