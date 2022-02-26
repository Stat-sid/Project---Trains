def construct_railroad_network(f):
    with open(f) as h:
        indata = h.readlines()
        outdata = [tuple(element.strip("\n").split(",")) for element in indata]
        return outdata
    
    
    
