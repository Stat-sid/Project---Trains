import random
from station import Station
from connection import Connection
from train import Train
from world import World

def read_nested_lists_from_file(f):
    """
    Reads file f and gives a list of lists as output.
    """
    with open(f) as h:
        indata = h.readlines()
        outdata = [element.strip("\n").split(",") for element in indata]
        return outdata

def get_string(prompt):
    """
    Returns a string from user input.
    """
    string_input = input(str(prompt)).lower()
    if type(string_input) != str:
        try:
            string_input = str(string_input)
        except ValueError:
            return "EXIT"
    return string_input

def user_inputs_stations_file():
    stations_input = get_string("Enter name of stations file:  ")
    return stations_input

def user_inputs_connections_file():
    connections_user = get_string("Enter name of connections file:  ")
    return connections_user

def user_inputs_no_of_trains():
    no_of_trains_user = input("Enter how many trains to simulate:  ")
    return no_of_trains_user

def IO_stations():
    while True:
        try:
            stations_in = user_inputs_stations_file()
            stations_data = read_nested_lists_from_file(stations_in)
        except FileNotFoundError:
            print("File not found. Try again.")
        else:
            break
    return stations_data

def IO_connections():
    while True:
        try:
            connections_in = user_inputs_connections_file()
            connection_data = read_nested_lists_from_file(connections_in)
        except FileNotFoundError:
            print("File not found. Try again.")
        else:
            break
    return connection_data

def IO_no_of_trains():
    while True:
        try:
            no_of_trains = int(user_inputs_no_of_trains())
        except ValueError:
            print("Only integers accepted. Try again.")
        else:
            break
    return no_of_trains

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

def add_connections_to_stations(connections_list, list_of_stations):
    for _from, to, line, direction in connections_list:
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

def choose_random_station(station_list):
    """
    Takes a list of station objects as input and chooses a random station object.
    """
    return random.choice(station_list)

def create_trains(no_of_trains, stations_list):
    """
    Takes a list of station objects and cretes a number of trains on random stations based on user input.
    """
    set_of_trains = set()
    for train_id in range(1, no_of_trains+1):
        random_station = choose_random_station(stations_list)
        random_connection = random.choice(random_station.get_connections())
        assigned_line = random_connection.get_line()
        random_direction = random_connection.get_direction()
        new_train = Train(id=train_id, line=assigned_line ,direction=random_direction, current_station=random_station)
        set_of_trains.add(new_train)
    return set_of_trains

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

def IO_route_info_start(world):
    while True:
        try:
            starting_in = input("Select a start station: ").upper()
            starting_station = world.get_station(starting_in)
        except KeyError:
            print("Station does not exist. Please try again. Available stations:")
            [print(station.get_id()) for station in world.get_stations()]
        else:
            break
    return starting_station

def IO_route_info_end(world):
    while True:
        try:
            end_in = input("Select a end station: ").upper()
            end_station = world.get_station(end_in)
        except KeyError:
            print("Station does not exist. Please try again. Available stations:")
            [print(station.get_id()) for station in world.get_stations()]
        else:
            break
    return end_station

def IO_route_info_steps():
    while True:
        try:
            selected_steps = int(input("Select time steps: "))
        except ValueError:
            print("Only integers accepted. Try again.")
        else:
            break
    return selected_steps

def route_info(world, starting_station, end_station, selected_steps):
    shortest_path = world.get_shortest_path(starting_station, end_station)
    if len(shortest_path) - 1 > selected_steps or not starting_station.get_connections(): # - 1 in order to exclude the starting station.
        return False
    else:
        return True

def user_world_interaction(world):
    """
    This is the main user interaction function.
    """
    no_of_trains = world.get_no_of_trains()
    user_prompt = "Continue simulation [1], train info [2], route info [3] exit [q].\n"
    user_selection = input(user_prompt).lower()
    while user_selection != "q":
        if user_selection == "1":
            world.tick()
            user_selection = input(user_prompt).lower()

        elif user_selection == "2":
            while True:
                try:
                    user_train_selection = int(input(f"Which train [1 - {no_of_trains}]: "))
                except ValueError:
                    print("Only integers accepted. Try again.")
                else:
                    if user_train_selection > no_of_trains:
                        print("Train does not exist. Please select a valid train.")
                    else:
                        break            
            selected_train = world.get_train(user_train_selection)
            get_train_info(selected_train)
            user_selection = input(user_prompt).lower()

        elif user_selection == "3":
            starting_station = IO_route_info_start(world)
            end_station = IO_route_info_end(world)
            selected_steps = IO_route_info_steps()
            reachable = route_info(world, starting_station, end_station, selected_steps)
            if reachable:
                print(f"Station {end_station} is reachable from station {starting_station} within {selected_steps} timesteps.")
            else:
                print(f"Station {end_station} is not reachable from station {starting_station} within {selected_steps} timesteps.")
            user_selection = input(user_prompt).lower()

        else:
            print("Not a valid selection.")
            user_selection = input(user_prompt).lower()
    print("Thank you and goodbye.")





def main():
    """
    This is the main function of the program.
    """

    #Read from file and create station objects.
    station_data = IO_stations()
    station_objects = station_creator(station_data)

    #Read from file and add connections to the station_objects.
    connection_data = IO_connections()
    add_connections_to_stations(connection_data, station_objects)

    #Create a number of trains at random stations based on user input.
    in_no_of_trains = IO_no_of_trains()
    train_objects = create_trains(in_no_of_trains, station_objects)

    #Store the created trains in stations in a World object.
    new_world = World(station_objects, train_objects)

    user_world_interaction(new_world)



main()