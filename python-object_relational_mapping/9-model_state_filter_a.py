#!/usr/bin/python3
"""
  Write a script that lists all State objects that
  contain the letter a from the database hbtn_0e_6_usa

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
      Main function.
    """
    conn = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(conn.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    states = states.filter(State.name.contains('a')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
