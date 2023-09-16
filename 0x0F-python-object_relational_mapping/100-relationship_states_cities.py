#!/usr/bin/python3
"""
A script that creates the State California with the City
San Francisco from a database.
"""

from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
    session.close()
