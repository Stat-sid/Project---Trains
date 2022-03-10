class Line():
    
    def __init__(self, list_of_stations):
        self.list_of_stations = list(list_of_stations)

    def get_beginning_station_southward(self):
        return list(self.get_list_of_stations)[0]

    def get_final_station_southward(self):
        return list(self.get_list_of_stations)[-1]

    def get_beginning_station_northward(self):
        return list(self.get_list_of_stations)[-1]

    def get_final_station_northward(self):
        return list(self.get_list_of_stations)[0]  
        
    def get_list_of_stations(self):
        return self.list_of_stations