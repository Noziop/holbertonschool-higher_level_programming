#!/usr/bin/python3
"""Prints State object with name passed as argument"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)
    
    # Create session
    session = Session()
    
    # Query state with name passed as argument
    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()
    
    # Print result or Not found
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    
    # Close session
    session.close()