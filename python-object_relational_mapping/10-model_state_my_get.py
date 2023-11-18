#!/usr/bin/python3
"""
    Write a script that prints the State object
    with the name passed as argument from the database hbtn_0e_6_usa

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
    states = states.where(State.name == sys.argv[4]).all()

    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print('Not found')