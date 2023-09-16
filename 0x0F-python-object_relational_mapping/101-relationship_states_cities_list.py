#!/usr/bin/python3

"""
Module that connects python script to a database
and retrieves data from table states and prints
id and name
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True  # specifies that the engine should check db status
    )

    # create session maker object that binds to the previous db
    Session = sessionmaker(bind=engine)

    # creates a new session
    my_session = Session()
    query = my_session.query(State).outerjoin(City).order_by\
            (State.id, City.id).all()
    for states in query:
        print(f"{states.id}: {states.name}")
    for city in states.cities:
        print(f"    {city.id}: {city.name}")
    # close the session
    my_session.close()
