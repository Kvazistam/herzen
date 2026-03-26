from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)

    stories = relationship("Story", back_populates="user")


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="stories")