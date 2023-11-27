#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
