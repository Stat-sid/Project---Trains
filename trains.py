

def read_station_delays(f):
    with open(f) as h:
            indata = h.readlines()
            outdata_dict = {}
            for i in indata:
                station, delay = i.strip("\n").split(",")
                outdata_dict[station] = delay
    return outdata_dict

def construct_railroad_network(f):
    with open(f) as h:
        indata = h.readlines()
        outdata = [tuple(element.strip("\n").split(",")) for element in indata]
        return outdata



class Train():
    def __init__(self, id) -> None:
        self.id = int(id)


    def position(self):

        self.station = 
        self.direction = 
        self.line = 
        pass


class Rairoad_Network():

    def __init__(self, station, line, delay) -> None:
        self.station = ...
        self.line = ...
        self.delay = ...
        pass

def user_inputs():
    stations_input = input("Enter name of stations file:  ").upper()
    if type(stations_input) != str:
        try:
            stations_input = str(stations_input)
        except ValueError:
            return "EXIT"
    connections_user = input("Enter name of connections file:  ").upper()
    if type(connections_user) != str:
        try:
            connections_user = str(connections_user)
        except ValueError:
            return "EXIT"
    no_of_trains_user = input("Enter how many trains to simulate:  ").upper()
    if type(no_of_trains_user) != int:
        try:
            no_of_trains_user = int(no_of_trains_user)
        except ValueError:
            return "EXIT"
    return stations_input, connections_user, no_of_trains_user



def main():
    """
    This is the main function of the program.
    """

    
    
    