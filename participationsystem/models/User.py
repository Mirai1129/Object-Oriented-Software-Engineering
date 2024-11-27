from sqlalchemy import Column, Integer, String

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    account = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

    # Discriminator for polymorphic inheritance
    type = Column(String(50))

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": type
    }
