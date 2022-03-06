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
import random

def choose_random_station(station_list):
    return random.choice(station_list)

def choose_random_direction():
    return random.choice(["S","N"])

def read_station_delays(f):
    with open(f) as h:
            indata = h.readlines()
            outdata_dict = {}
            for i in indata:
                station, delay = i.strip("\n").split(",")
                outdata_dict[station] = delay
    return outdata_dict

def read_nested_lists_from_file(f):
    with open(f) as h:
        indata = h.readlines()
        outdata = [element.strip("\n").split(",") for element in indata]
        return outdata


def station_creator(nested_list):
    stations = []
    for id, delay in nested_list:
        try:
            delay = float(delay)
            station = Station(id=id, delay=delay)
            stations.append(station)
        except:
            raise ValueError("Float expected")
    return stations

def connection_creator(nested_lists, stations):
    connection_list = []
    current_line = None
    for current, next, line, direction in nested_lists:
        if line in connection_list:
            # get the line object
            current_line.add()
        else:
            connection_list.append(line)
            #create line object with info



# def construct_railroad_network(connection_lists): 
#     network = {}
#     for connection in connection_lists:
#         for element in connection:
#             if element[0] not in network:
#                 network[element[0]] = []
#             network[element[0]].append(element[1])
#             if element[1] not in network:
#                 network[element[1]] = []
#             network[element[1]].append(element[0])
#     return network

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
        
    def __init__(self, id, line, direction, current_station) -> None:
        self.id = int(id)
        self.line = line
        self.direction = direction
        self.current_station = current_station

    def current_position(self):
        return [self.current_station, self.direction, self.line]

    def move(self, delay_prob, next_station):
        is_delayed = random.random() < delay_prob
        if not is_delayed:
            self.current_station = next_station

class Station():

    def __init__(self, id, delay):
        self.id = id
        self.delay = delay
        

    def __str__(self):
        return str(self.id)

    def set_station_north(self, next_station_north):
        self.next_station_north = next_station_north

    def set_station_south(self, next_station_south):
        self.next_station_south = next_station_south

    def get_id(self):
        return self.id
    
    def get_delay(self):
        return self.delay

    def get_next(self, direction = "S"):
        if direction.upper() == "S":
            return self.next_station_south
        else:
            return self.next_station_north

class Connection():

    def __init__(self, beginning, next, line):
        self.beginning = beginning
        self.next = next
        self.line = line

    def set_beginning(self, station):
        self.beginning = station

    def set_next(self, station):
        self.next = station

    def get_beginning(self):
        return self.beginning

    def get_next(self):
        return self.next

    def get_line(self):
        return self.line


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

class Railroad_Network():

    def __init__(self, graph = []) -> None:
        self.graph = graph
        
    #Get the keys to the dictionary.
    def get_stations(self): #vertices
        return list(self.graph.keys())

    def connections(self): #edges
        return self.get_connections()

    # Find the distinct list of edges
    def get_connections(self):
      station_name = []
      for vertex in self.graph:
         for next_vertex in self.graph[vertex]:
            if {next_vertex, vertex} not in station_name:
               station_name.append({vertex, next_vertex})
      return station_name

    # Add the station as a key
    def add_station(self, vertex):
      if vertex not in self.graph:
         self.graph[vertex] = []
    
    # Add the new connection
    def add_connection(self, edge):
      edge = set(edge)
      (vertex_1, vertex_2) = tuple(edge)
      if vertex_1 in self.graph:
         self.graph[vertex_1].append(vertex_2)
      else:
         self.graph[vertex_1] = [vertex_2]

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


stations = read_nested_lists_from_file("stations.txt")
connections = read_nested_lists_from_file("teststations.txt")
print(connections)
n = 1
station_obj = station_creator(stations)
print([station.get_id() for station in station_obj])



# def main():
#     """
#     This is the main function of the program.
#     """

    
    
    