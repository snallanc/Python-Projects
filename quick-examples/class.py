"""
Classes:
Provide a means to encapsulate data that define the state and functions that modify the state into a single unit.
Classes provide 2 ways for accessing the data:
1. Attribute references(<class>.<variable>) and 2. Instantiation(creating class objects)
"""

"""
EXAMPLE:
Attribute reference and Instantiation. Attribute reference works only for variables and not methods. Instantiation
works for both.
"""

class Class1:
    name = "Class1" # This is a class variable that is shared by all instances.
                    # Its a shared data that is not meant to be unique like instance variables.
                    # Mutable objects like list, dict etc., should not be used as class variables.

    def __init__(self, name):
        self.instance_name = name # This is an instance variable that is unique to each instance.

    def printInstance(self):
        print("Instance {0} of class {1}".format(self.instance_name, Class1.name))


print(Class1.name)
# print(Class1.printInstance())  ====> This would fail since function call expects an instance(self)!!
c1 = Class1("c1")
# Class1.printInstance(c1)       ====> Now, this will work since the instance is passed
c1.printInstance()             # ====> This just translates to Class1.printInstance(c1)

c2 = Class1("c2")
c2.printInstance()
# c2.name = "Class2"          ====> While this works, it is not expected to change the class variable per instance
# print(c.name)
print("\n###################################### \n")


"""
Inheritance:
Python supports inheritance where a sub class can be derived from one or more base classes.
Attribute search path follows a Depth First, Left to Right order where the attribute is
1. searched first in the derived class,
2. if not found, searched in the first base class and then in the base classes of this first base class
3. if not found, searched in the second base class and then in the base classes of this second base class
and so on.
"""

"""
EXAMPLE:
"""
class baseClass:
    def __init__(self, items):
        print("__init__ is called")
        self.data = []
        # baseClass.add(self, items) # You need to explicitly specify how the add method should be invoked like this
        self.__add(items)            # Or like this. Here, you clearly tell python to invoke the private method,
                                     # __add that uses name mangling.
    def add(self, items):
        print("add in baseClass is called")
        for item in items:
            self.data.append(item)
    __add = add                      # Private copy of add method. Python does name mangling to resolve this.

class derivedClass(baseClass):
    def add(self, keys, values):
        print("add in derivedClass is called")
        for item in zip(keys, values):
            self.data.append(item)
    def printData(self):
        print("data is {0}".format(self.data))

d = derivedClass([i for i in range(10, 0, -2)])
# d.__add([i for i in range(9, -1, -2)]) # This baseClass invocation would fail since __add is a "Private" method of the
                                         # baseClass!!
# d.add([i for i in range(9, -1, -2)])   # This baseClass invocation would fail because add method is overridden in the
                                         # derivedClass, so it can't invoke baseClass's add method!!
d.add(("name", "age", "location"),("Superman", 1000, "Anywhere but not everywhere"))
                                         # This derivedClass invocation would go through.
d.printData()

"""
isinstance() and issubclass():
isinstance() tells whether a given object is an instance of the given class or not.
issubclass() tells whether a given class inherits from the other class or not.

EXAMPLE:
"""
print(isinstance(d, derivedClass))
print(isinstance(d, baseClass))
print(issubclass(derivedClass, baseClass))