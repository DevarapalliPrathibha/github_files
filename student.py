class student:
    marks_bonus = 1.5
    somevalue =" "
    something =" "
    read_value ="jk"
    def __init__(self,first,last,marks,read):
        self.first = first
        self.last = last
        self.marks = marks
        self.read = read
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first ,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_bonus(self):
        self.marks = int(self.marks * self.marks_bonus)
    def some_value(self, update):
        self.somevalue = self.email + self.fullname + update
    def Read(self,yamani):
        self.read = self.email + self.fullname +yamani
    def readvalue(self,pinky,jin):
        self.read_value=  self.read_value +pinky +jin
