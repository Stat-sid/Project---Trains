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

def choose_random_station(station_list):
    return random.choice(station_list)

def choose_random_direction():
    return random.choice(["S","N"])

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
            raise ValueError("Float expected.")
    return stations

def set_station_delays(set_of_stations, nested_lists):
    for station in set_of_stations:
        for id, delay in nested_lists:
            if station.get_id() == id:
                station.set_delay(delay)
                #print(station.get_delay())

def get_matching_station(station, set_of_stations):
    for s in set_of_stations:
        if s.get_id() == station:
            return s

def add_connections_to_stations(nested_lists, set_of_stations):
    for _from, to, line, direction in nested_lists:

        # Add connection:               _from -> to
        from_station = get_matching_station(_from, set_of_stations)
        new_connection = Connection(to, line, direction)
        from_station.add_connection(new_connection)

        # Add symmetrical connection:   to -> _from
        to_station = get_matching_station(to, set_of_stations)
        if direction == "S":
            new_connection = Connection(_from, line, "N")
        elif direction == "N":
            new_connection = Connection(_from, line, "S")
        to_station.add_connection(new_connection)

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


stations_data = read_nested_lists_from_file("stations.txt")
connections_data = read_nested_lists_from_file("connections.txt")
stations_obj = station_creator(stations_data)
#[print(station.get_id(), station.get_next(), station.get_line(), station.get_delay()) for station in station_obj]
add_connections_to_stations(connections_data, stations_obj)
#print(station.get_next_station()) for station in stations_obj
[print(station, "towards", station.get_next_station("blue", "S")) for station in stations_obj]
[print(station, "towards", station.get_next_station("blue", "N")) for station in stations_obj]
# [print(station.get_next_station("blue", "N")) for station in stations_obj]
# [print(station.get_next_station("green", "S")) for station in stations_obj]
# [print(station.get_next_station("green", "N")) for station in stations_obj]





# def main():
#     """
#     This is the main function of the program.
#     """

    
    
    