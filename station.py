class Station():

    def __init__(self, id, delay = 0):
        self.id = id
        self.delay = delay
        self.connections = []
        
    def __str__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

    def get_id(self):
        return self.id
    
    def get_delay(self):
        return self.delay

    def get_next_station(self, line, direction):
        filtered_connection = filter(
            lambda c: True if c.get_line()==line and c.get_direction()==direction else False,
            self.connections
        )
        try:
            next_station = next(filtered_connection).get_to()
            return next_station
        except StopIteration:
            return None
    
    def get_connections(self):
        return self.connections

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self, connection):
        self.connections.remove(connection)

    def is_next(self, to):
        for connection in self.get_connections:
            if to in connection:
                return True
            else:
                return False
