#!/usr/bin/python3
"""
Module that contains the class definition of a State
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database and its relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
