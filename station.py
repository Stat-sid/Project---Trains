class Station():

    def __init__(self, id, delay = 0):
        self.id = id
        self.delay = delay
        
    def __str__(self):
        return str(self.id)

    def get_id(self):
        return self.id
    
    def get_delay(self):
        return self.delay

    def __hash__(self):
        return hash(self.id)

    def get_next_station(self, line, direction):
        pass
    
    def set_connections(self, connections):
        self.connections = connections

    def get_connections(self):
        return self.connections

    def add_connection(self, connection):
        pass

    def remove_connection(self):
        pass