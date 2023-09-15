#!/usr/bin/python3

"""
Module that connects python script to a database
and retrieves data from table states thats
has letter a and prints
id and name
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  # creates session interacting with db
from model_state import Base, State

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

    for state in my_session.query(State).order_by(State.id).filter(State.name.like("%a%")).all():
        print("{}: {}".format(state.id, state.name))
    # close the session
    my_session.close()
