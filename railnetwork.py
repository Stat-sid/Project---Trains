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