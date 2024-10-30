#!/usr/bin/python3
"""Deletes State objects with letter a"""
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
    
    # Query and delete states containing letter 'a'
    states_with_a = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    
    # Delete each state found
    for state in states_with_a:
        session.delete(state)
    
    # Commit the changes
    session.commit()
    
    # Close session
    session.close()