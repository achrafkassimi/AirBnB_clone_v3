#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

a = storage.all(State)
print(a)

first_state_id = list(a.values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
