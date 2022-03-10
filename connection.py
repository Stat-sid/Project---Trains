class Connection():

    def __init__(self, beginning, next, line):
        self.beginning = beginning
        self.next = next
        self.line = line

    def __repr__(self):
     return str([self.beginning, self.next, self.line])

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