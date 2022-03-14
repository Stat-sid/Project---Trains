import random

class Train():
        
    def __init__(self, id, line, direction, current_station) -> None:
        self.id = int(id)
        self.line = line
        self.direction = direction
        self.current_station = current_station

    def current_position(self):
        return [self.current_station.get_id(), self.direction, self.line]

    def get_id(self):
        return self.id

    # I know this will not work right for a station without connections.
    def move(self):
        if self.__am_I_delayed():
            pass
        else:
            if self.__get_next_station() is None:
                self.__turn_around()
            
            next_station = self.__get_next_station()
            self.current_station = next_station

    def __am_I_delayed(self):
        delay_probability = self.current_station.get_delay()
        if random.random() < delay_probability:
            return True
        else:
            return False

    def __get_next_station(self):
        return self.current_station.get_next_station(self.line, self.direction)

    def __turn_around(self):
        if self.direction == "N":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "N"
