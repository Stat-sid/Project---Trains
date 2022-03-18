class World():

    def __init__(self, stations, trains):
        self.stations = stations
        self.trains = trains

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

    def bfs(self, _from, visited = []):
        queue = []
        visited.append(_from)
        queue.append(_from)
        
        while queue:
            m = queue.pop(0)
            print(m, end = " ")

            for connection in m.get_connections():
                if connection.get_to() not in visited:
                    visited.append(connection.get_to())
                    queue.append(connection.get_to())




