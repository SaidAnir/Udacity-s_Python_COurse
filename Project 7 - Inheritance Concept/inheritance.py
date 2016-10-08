"""
THis program is meant to show the concept of inheritance.
I've created two classes (Parent & Child), each one of the
defines a contructor and a show_info() method.

"""

class Parent(object):
    """ Class about parents """

    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))

class Child(Parent):
    """ A Child class that inherits from Parent class """

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        # Parent constructor gets called in here
        super(Child, self).__init__(last_name, eye_color) 
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - {}".format(self.last_name))
        print("Eye Color - {}".format(self.eye_color))
        print("Number of Toys - {}".format(self.number_of_toys))

p = Parent("lant", "brown")
p.show_info()
c = Child("Smith-lant", "Brown", "100")
c.show_info()

"""
Output:

Parent constructor called
Last Name - lant
Eye Color - brown
Child constructor called
Parent constructor called
Last Name - Smith-lant
Eye Color - Brown
Number of Toys - 100


"""