#!/usr/bin/python3

"""

   Model state.

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sys import argv

engine = create_engine(f'mysql://{argv[1]}:{argv[2]}@localhost/{argv[2]}')
Base = declarative_base()


class State(Base):
    """
        Implementation of the state class

    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )
