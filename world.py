class World():

    def __init__(self, stations, trains):
        self.stations = stations
        self.trains = trains

    # def set_stations(self):
    #     pass
    
    # def set_trains(self):
    #     pass

    def get_station(self, id):
        for s in self.stations:
            if s.get_id() == id:
                return s

    def get_train(self, id):
        for train in self.trains:
            if train.get_id() == id:
                return train

    def get_stations(self):
        return self.stations

    def get_trains(self):
        return self.trains

    def get_no_of_trains(self):
        return len(self.trains)

    def tick(self):
        for train in self.trains:
            train.move()


