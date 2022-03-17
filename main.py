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
from re import A
from station import Station
from connection import Connection
from train import Train
from world import World

def choose_random_station(station_list):
    """
    Takes a list of station objects as input and chooses a random station object.
    """
    return random.choice(station_list)

def read_nested_lists_from_file(f):
    """
    Reads file f and gives a list of lists as output.
    """
    with open(f) as h:
        indata = h.readlines()
        outdata = [element.strip("\n").split(",") for element in indata]
        return outdata

def get_string(prompt):
    string_input = input(str(prompt)).lower()
    if type(string_input) != str:
        try:
            string_input = str(string_input)
        except ValueError:
            return "EXIT"
    return string_input

def get_int(prompt):
    int_input = input((prompt))
    if type(int_input) != int:
        try:
            int_input = int(int_input)
        except ValueError:
            return "EXIT"
    return int_input

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

def get_matching_station(station, list_of_stations):
    """
    Takes a station id(str) and a list of station objects and matches the id with an existing station object in the list.
    """
    for s in list_of_stations:
        if s.get_id() == station:
            return s


def add_connections_to_stations(nested_lists, list_of_stations):
    for _from, to, line, direction in nested_lists:
        from_station = get_matching_station(_from, list_of_stations)
        to_station = get_matching_station(to, list_of_stations)

        # Add connection:               _from -> to
        new_connection = Connection(to_station, line, direction)
        from_station.add_connection(new_connection)

        # Add symmetrical connection:   to -> _from
        if direction == "S":
            new_connection = Connection(from_station, line, "N")
        elif direction == "N":
            new_connection = Connection(from_station, line, "S")
        to_station.add_connection(new_connection)

def create_trains(no_of_trains, stations_list):
    set_of_trains = set()
    for train_id in range(1, no_of_trains+1):
        random_station = choose_random_station(stations_list)
        random_connection = random.choice(random_station.get_connections())
        assigned_line = random_connection.get_line()
        random_direction = random_connection.get_direction()
        new_train = Train(id=train_id, line=assigned_line ,direction=random_direction, current_station=random_station)
        set_of_trains.add(new_train)
    return set_of_trains

def create_world(list_of_stations, set_of_trains):
    world = World(list_of_stations, set_of_trains)
    return world

def tick(set_of_trains):
    for train in set_of_trains:
        train.move()

def user_inputs():
    stations_input = get_string("Enter name of stations file:  ")
    connections_user = get_string("Enter name of connections file:  ")
    no_of_trains_user = get_int("Enter how many trains to simulate:  ")
    return stations_input, connections_user, no_of_trains_user

def is_delayed(train_object):
    if train_object._am_I_delayed():
        return "(DELAY)"
    else:
        return ""

def get_train_info(train_object):
    train_id = train_object.get_id()
    position = train_object.get_current_station()
    line = train_object.get_line()
    direction = train_object.get_direction()
    delay_indicator = is_delayed(train_object)
    (print(f"Train {train_id} on {line} line, is at station {position}, heading {direction} direction. {delay_indicator}")) 

# def user_world_interaction(world, no_of_trains):
#     is_active = True
#     while is_active:
#         user_selection = input("Continue simulation [1], train info [2], exit [q].\n").lower()
#         while user_selection != "q":
#             if user_selection == "1":
#                 tick(world)
#             elif user_selection == "2":
#                 user_train_selection = int(input(f"Which train [1 - {no_of_trains}]: "))
#                 selected_train = get_matching_train(world, user_train_selection)
#                 get_train_info(selected_train)
#                 break
#             else:
#                 print("Not a valid selection.")
#                 user_selection = input("Continue simulation [1], train info [2], exit [q].").lower() #Error handling?
#     #recursion here?
#     #quit() #Will this only work if the user selects [q] ??

def user_world_interaction(world):
    no_of_trains = world.get_no_of_trains()
    user_selection = input("Continue simulation [1], train info [2], exit [q].\n").lower()
    while user_selection != "q":
        if user_selection == "1":
            world.tick()
            user_selection = input("Continue simulation [1], train info [2], exit [q].\n").lower()
        elif user_selection == "2":
            user_train_selection = int(input(f"Which train [1 - {no_of_trains}]: "))
            # if int(user_selection) > no_of_trains:
            #     print("Train does not exist, please try again.")
            #     user_train_selection = int(input(f"Which train [1 - {no_of_trains}]: "))'
            selected_train = world.get_train(user_train_selection)
            get_train_info(selected_train)
            user_selection = input("Continue simulation [1], train info [2], exit [q].\n").lower()
        else:
            print("Not a valid selection.")
            user_selection = input("Continue simulation [1], train info [2], exit [q].").lower()
        #print("Thank you and goodbye.")




def main():
    """
    This is the main function of the program.
    """

    in_stations, in_connections, in_no_of_trains = user_inputs()

    #Read from file and create station objects.
    station_data = read_nested_lists_from_file(in_stations)
    station_objects = station_creator(station_data)

    #Read from file and add connections to the station_objects.
    connection_data = read_nested_lists_from_file(in_connections)
    add_connections_to_stations(connection_data, station_objects)

    #Create a number of trains at random stations based on user input.
    train_objects = create_trains(in_no_of_trains, station_objects)

    #Create the selected number of trains in assigned to random station objects.
    new_world = World(station_objects, train_objects)


    user_world_interaction(new_world)

main()



# stations_data = read_nested_lists_from_file("stations.txt")
# connections_data = read_nested_lists_from_file("connections.txt")
# stations_obj = station_creator(stations_data)
# add_connections_to_stations(connections_data, stations_obj)
# train_obj = create_trains(4, stations_obj)
# a_world = World(stations_obj, train_obj)
# print(a_world.get_train(1).current_position())
# a_world.tick()
# print(a_world.get_train(1).current_position())
# print(len(a_world.get_trains()))
# [print(train.get_id(), train.get_current_station(), train.get_line(), train.get_direction()) for train in test_world]
# for train in test_world:
#     train.move()
#     print(train.get_id(), train.get_current_station(), train.get_line(), train.get_direction())
#     train.move()
#     print(train.get_id(), train.get_current_station(), train.get_line(), train.get_direction())

# in_stations, in_connections, in_no_of_trains = user_inputs()
# print(in_stations)
# print(in_connections)
# print(in_no_of_trains)