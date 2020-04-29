
class Room:
    def __init__(self):
        """
        By default a room generates with no Exits.
        """
        self.description = "You are in a room with no exits"
        self.exits = {}
        self.things = {}