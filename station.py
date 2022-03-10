class Station():

    def __init__(self, id, delay = 0):
        self.id = id
        self.delay = delay
        
    def __str__(self):
        return str(self.id)

    def set_delay(self, delay):
        self.delay = delay

    def set_station_north(self, next_station_north):
        self.next_station_north = next_station_north

    def set_station_south(self, next_station_south):
        self.next_station_south = next_station_south

    def set_line(self, line):
        self.line = line

    def get_id(self):
        return self.id
    
    def get_delay(self):
        return self.delay

    def get_line(self):
        return self.line

    def get_next(self, direction = "S"):
        if direction.upper() == "S":
            return self.next_station_south
        else:
            return self.next_station_north

    def __hash__(self):
        return hash(self.id)