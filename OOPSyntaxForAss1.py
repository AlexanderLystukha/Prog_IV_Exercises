#region Class syntax

# in python if you put (_) next to any variable or function, it means that it is private. No functionality
# ( __ ) means that python has set this up, in lingual it means dunder instead of double underscore
# when defining a class:


# for documenting functions, add """ some text """ right under the function/method.
class Foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print("hi")
        # this method allows for variables to actually output the variable data
        # if you don't it just choose gibberish (method name, memory location, etc)
        # this is what will be outputted to the console or whatever you're outputting too

    def __repr__(self):
        print("bye")
        # this is what will be used by the IDE when debugging and such
    def method(self):
        return self.a + self.b

    # always use "self" because python do be like that


class Boo:
    class_var = 16 # dont declare class variables outside of __init__

# you are able to access class variables from the class object instance (no bueno)

#region Example Coord for __str__

class Coord:
    def __init__(self, x, y):
        self.coord = (x, y)

    def __str__(self):
        return f"Coord: {self.coord}"

    def __repr__(self):
        return f"REPR: {self.coord}"

f = Coord(3, 5)
print(f)
pass

#endregion

class House:
    def __init__(self):
        self.house = ""
    def __str__(self):
        house = """
        [==============]
        [==============]
        [======  ======]
        """

    def __repr__(self):
        return f"REPR: {self.house}"
#endregion