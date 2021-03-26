"""
When you're going to build a completely new universe filled with completely new creatures that have nothing in common
with all the familiar things, you may want to build your own exception structure.

For example, if you work on a large simulation system which is intended to model the activities of a pizza restaurant,
it can be desirable to form a separate hierarchy of exceptions.

You can start building it by defining a general exception as a new base class for any other specialized exception.
We've done in in the following way:
"""

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese
