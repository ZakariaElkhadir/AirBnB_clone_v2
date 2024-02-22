#!/usr/bin/python3
"""
Defines city Class
"""
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class City(BaseModel):
    """defines city to look for"""
    __tablename__ = "cities"  # Class attribute for table name
    if os.getenve("HBNB_TYPE_STORAGE") == db:
        id = Column(String(60), primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship(
                            'Place', backref="cities",
                            cascade="all, delete-orphan"
                            )
    else:
        state_id = ""
        name = ""
