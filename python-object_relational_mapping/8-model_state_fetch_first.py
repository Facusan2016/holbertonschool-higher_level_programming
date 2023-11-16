#!/usr/bin/python3
"""
  Write a script that prints the first State
  object from the database hbtn_0e_6_usa.

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
    states_row = session.query(State).order_by(State.id).first()

    if (not states_row):
        print("Nothing.")
    else:
        print(f"{states_row.id}: {states_row.name}")
