#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dog(Base):
    __tablename__ = "dogs"
    __table_args__ = (PrimaryKeyConstraint("id", name="id_pk"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
