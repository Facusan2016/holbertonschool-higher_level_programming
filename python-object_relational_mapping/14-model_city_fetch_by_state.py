#!/usr/bin/python3
"""
  write a script 14-model_city_fetch_by_state.py that
  prints all City objects from the database hbtn_0e_14_usa

"""

import sys
from model_state import Base, State
from model_city import City
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

    res = session.query(City, State)
    res = res.join(State, State.id == City.state_id).all()

    for city, state in res:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
