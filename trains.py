"""
#### stations.txt ###
A,0.001
B,0.001
C,0.2
D,0.001
X,0.1
Y,0.1
Z,0.1

#### connections.txt ###
A,B,blue,S
B,C,blue,S
C,D,blue,S
X,Y,green,S
Y,C,green,S
C,Z,green,S

"""

def read_station_delays(f):
    with open(f) as h:
            indata = h.readlines()
            outdata_dict = {}
            for i in indata:
                station, delay = i.strip("\n").split(",")
                outdata_dict[station] = delay
    return outdata_dict

def import_railroad_network(f):
    with open(f) as h:
        indata = h.readlines()
        outdata = [[element.strip("\n").split(",")] for element in indata]
        return outdata

def construct_railroad_network(l): 
    network = {}
    for i in l:
        for el in i:
            if el[0] not in network:
                network[el[0]] = []
            network[el[0]].append(el[1])
            if el[1] not in network:
                network[el[1]] = []
            network[el[1]].append(el[0])
    return network



# def construct_railroad_network_test(l):
#     network = {}
#     for i in l:
#         if i[2] not in network:
#             network[(i[2], i[3])] = []
#         network[(i[2], i[3]].append((i[0], i[1]))
#         if i[3] == "S":
#             network[(i[2], "N")].append((i[1], i[0]))
#         if i[3] == "N":
#             network[(i[2], "S")].append((i[1], i[0]))
#     return network


class Train():
    def __init__(self, id) -> None:
        self.id = int(id)


    def locate(self, network):
        #station = 
        #direction = 
        #line = 
        pass

    def current_position(self):
        return [self.station, self.direction, self.line]

    def move(self):
        pass


class Station():

    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_destination(self, destination, weight=0):
        self.adjacent[destination] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, destination):
        return self.adjacent[destination]

    def get_line(self, line):
        return self.adjacent.keys()


class Railroad_Network():

    def __init__(self, gdict = None) -> None:
        if gdict is None:
            gdict = []
        self.gdict = gdict

    #Get the keys to the dictionary.
    def get_stations(self): #vertices
        return list(self.gdict.keys())

    def connections(self): #edges
        return self.findconnections()

    # Find the distinct list of edges
    def findconnections(self):
      stationname = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in stationname:
               stationname.append({vrtx, nxtvrtx})
      return stationname

    # Add the station as a key
    def addStation(self, vrtx):
      if vrtx not in self.gdict:
         self.gdict[vrtx] = []
    
    # Add the new connection
    def addConnection(self, edge):
      edge = set(edge)
      (vrtx1, vrtx2) = tuple(edge)
      if vrtx1 in self.gdict:
         self.gdict[vrtx1].append(vrtx2)
      else:
         self.gdict[vrtx1] = [vrtx2]

    #def update(self, ):



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


delays = read_station_delays("stations.txt")
connections = import_railroad_network("connections.txt")
rail_network = construct_railroad_network(connections)
g = Railroad_Network(rail_network)


# def main():
#     """
#     This is the main function of the program.
#     """

    
    
    