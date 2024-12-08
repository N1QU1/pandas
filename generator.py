class Accident(Exception):
    def __init__(self, name):
        self.name = name
    def print_exception(self):
        print("Oh no ha ocurrido un " + self.name + ", llamen a la policía")

try:
    raise Accident(MemoryError.__name__)
except Accident as a:
    a.print_exception()