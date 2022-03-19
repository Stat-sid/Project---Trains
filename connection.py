class Connection():

    def __init__(self, to, line, direction):
        self.to = to
        self.line = line
        self.direction = direction

    def __repr__(self):
     return str([self.to, self.line, self.direction])

    def get_to(self):
        return self.to

    def get_line(self):
        return self.line

    def get_direction(self):
        return self.direction