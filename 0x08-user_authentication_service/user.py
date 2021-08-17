#!/usr/bin/env python3
"""
USER module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model USER
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    reset_token = Column(VARCHAR(250), nullable=True)
    session_id = Column(VARCHAR(250), nullable=True)
