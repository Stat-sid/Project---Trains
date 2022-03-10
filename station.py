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
        next_station = filter(
            lambda c: c.get_to()
                if c.get_line()==line and c.get_direction()==direction
                else None
            , self.connections)
        return next_station
    
    def get_connections(self):
        return self.connections

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self, connection):
        self.connections.remove(connection)