
class World():

    def __init__(self, stations, trains):
        self.stations = stations
        self.trains = trains

    def get_station(self, id):
        for station in self.stations:
            if station.get_id() == id:
                return station
        raise KeyError

    def get_train(self, id):
        for train in self.trains:
            if train.get_id() == id:
                return train
        raise KeyError

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
            # print(m, end = " ")

            for connection in m.get_connections():
                if connection.get_to() not in visited:
                    visited.append(connection.get_to())
                    queue.append(connection.get_to())
        return visited


    def get_shortest_path(self, start, end, path=[]):
        """
        __source__='https://www.python.org/doc/essays/graphs/'
        __author__='Guido van Rossum'
        Adapted by: Efstathios Sidiropoulos.
        """
        path = path + [start]
        if start == end:
            return path
        if start not in self.stations:
            return None
        shortest = None

        for connection in start.get_connections():
            if connection.get_to() not in path:
                newpath = self.get_shortest_path(connection.get_to(), end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest



