#!/usr/bin/python3
"""Prints all City objects from database"""
import sys
from model_state import Base, State
from model_city import City
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
    
    # Query cities and states together
    cities = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()
    
    # Print results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    # Close session
    session.close()