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
from station import Station
from connection import Connection
from train import Train

def choose_random_station(station_list):
    """
    Takes a list of station objects as input and chooses a random station object.
    """
    return random.choice(station_list)

def choose_random_direction():
    """
    Chooses a random direction between "N" for Northbound and "S" for Southbound.
    """
    return random.choice(["S","N"])

def choose_random_line(list_of_lines):
    return random.choice(list_of_lines)

def read_nested_lists_from_file(f):
    """
    Reads file f and gives a list of lists as output.
    """
    with open(f) as h:
        indata = h.readlines()
        outdata = [element.strip("\n").split(",") for element in indata]
        return outdata

def station_creator(nested_lists):
    """
    Takes a list of lists as input and returns a list of station objects.
    """
    stations = []
    for id, delay in nested_lists:
        try:
            delay = float(delay)
            station = Station(id=id, delay=delay)
            stations.append(station)
        except:
            raise ValueError("Float expected.")
    return stations

def line_creator(nested_lists):
    """
    CODESMELL - FIX IT!
    """  
    line_dict = {}
    for _from, to, line, direction in nested_lists:
        if line not in line_dict:
            line_dict[line] = [_from]
        elif _from not in line_dict[line]:
            line_dict[line].append(_from)
    for _from, to, line, direction in nested_lists:
        if to not in line_dict[line]:
            line_dict[line].append(to)
    return line_dict


# def set_station_delays(set_of_stations, nested_lists):
#     for station in set_of_stations:
#         for id, delay in nested_lists:
#             if station.get_id() == id:
#                 station.set_delay(delay)
#                 #print(station.get_delay())

def get_matching_station(station, list_of_stations):
    """
    Takes a station id(str) and a list of station objects and matches the id with an existing station object in the list.
    """
    for s in list_of_stations:
        if s.get_id() == station:
            return s

def get_matching_line(station, line_dict):
    for line in line_dict:
        if station.get_id() in line_dict[line]:
            return line


def add_connections_to_stations(nested_lists, list_of_stations):
    for _from, to, line, direction in nested_lists:

        # Add connection:               _from -> to
        from_station = get_matching_station(_from, list_of_stations)
        new_connection = Connection(to, line, direction)
        from_station.add_connection(new_connection)

        # Add symmetrical connection:   to -> _from
        to_station = get_matching_station(to, list_of_stations)
        if direction == "S":
            new_connection = Connection(_from, line, "N")
        elif direction == "N":
            new_connection = Connection(_from, line, "S")
        to_station.add_connection(new_connection)

def create_random_world(no_of_trains, stations_list, line_dict):
    set_of_trains = set()
    for train_id in range(no_of_trains):
        random_station = choose_random_station(stations_list)
        random_direction = choose_random_direction()
        assigned_line = get_matching_line(random_station, line_dict)
        new_train = Train(id=train_id, line=assigned_line ,direction=random_direction, current_station=random_station)
        set_of_trains.add(new_train)
    return set_of_trains

def tick(set_of_trains):
    for train in set_of_trains:
        train.move()

def user_inputs():
    #CLI
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


stations_data = read_nested_lists_from_file("stations.txt")
connections_data = read_nested_lists_from_file("connections.txt")
test_lines = line_creator(connections_data)
stations_obj = station_creator(stations_data)
#[print(station.get_id(), station.get_next(), station.get_line(), station.get_delay()) for station in station_obj]
add_connections_to_stations(connections_data, stations_obj)
#print(station.get_next_station()) for station in stations_obj
# [print(station, "towards", station.get_next_station("blue", "S")) for station in stations_obj]
# [print(station, "towards", station.get_next_station("blue", "N")) for station in stations_obj]
# [print(station.get_next_station("blue", "N")) for station in stations_obj]
# [print(station.get_next_station("green", "S")) for station in stations_obj]
# [print(station.get_next_station("green", "N")) for station in stations_obj]
# for station in stations_obj:
#     line = get_matching_line(station, test_lines)
#     print(station.get_id(), "is in", line)
test_world = create_random_world(10, stations_obj, test_lines)
[print(train.get_id(), train.current_position()) for train in test_world]






# def main():
#     """
#     This is the main function of the program.
#     """

    
    
    