instance = None

class unica():
    def __new__(cls, arg):
        global instance
        if instance is not None:
            return instance
        instance = object.__new__(cls)
        instance.unica = arg
        return instance

    def __init__(self, arg):
        print(self.unica)

f = unica('a')
f = unica('b')
f = unica('c')