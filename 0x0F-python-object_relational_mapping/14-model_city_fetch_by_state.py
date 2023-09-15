#!/usr/bin/python3

"""
Module that connects python script to a database
and retrieves data from table states and prints
id and name
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

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

    cities = my_session.query(State.name, City.id, City.name).join(
        State).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
