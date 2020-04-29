import pytest
from link import game_objects

def test_room():
    room = game_objects.Room()
    # Explicitly assert the following.
    assert(len(room.description) > 0 )    # Room has a description.
    assert(len(room.exits.keys()) == 0 )  # Room has no exits yet.
    assert(len(room.things.keys()) == 0 ) # Room has no items/things yet.
