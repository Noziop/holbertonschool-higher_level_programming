#!/usr/bin/python3
"""Lists all State objects from the database"""
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
    
    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()
    
    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close session
    session.close()