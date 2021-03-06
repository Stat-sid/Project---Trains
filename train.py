class Train():
        
    def __init__(self, id, line, direction, current_station) -> None:
        self.id = int(id)
        self.line = line
        self.direction = direction
        self.current_station = current_station

    def current_position(self):
        return [self.current_station, self.direction, self.line]

    def move(self):
        self.current_station.get_next_station()
