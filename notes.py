###############################################################################

## BUILT-IN "OPERATOR" MODULE

# Possibly the most popular usage is operator.itemgetter.
# Given a list lst of tuples, you can sort by the ith element by:
# lst.sort(key=operator.itemgetter(i))


#In general, "OPERATOR" is to allow a functional style of programming:
# You might argue: "Why do I need operator.add when I can just do: add = lambda x, y: x+y?"
# The answers are:
# operator.add is (I think) slightly faster.
# It makes the code easier to understand for you, or another person later, looking at it.
# They don't need to look for the definition of add, because they know what the operator module does.

#Another example is in the use of the reduce() function:
# >>> import operator
# >>> a = [2, 3, 4, 5]
    # >>> reduce(lambda x, y: x + y, a)
# 14
# >>> reduce(operator.add, a)
# 14

###############################################################################

## "COLLECTIONS" MODULE
# implements specialized container datatypes providing alternatives to
# Python’s general purpose built-in containers, dict, list, set, and tuple.

# namedtuple():	factory function for creating tuple subclasses with named fields
# deque:		list-like container with fast appends and pops on either end
# ChainMap:		dict-like class for creating a single view of multiple mappings
# Counter:		dict subclass for counting hashable objects
# OrderedDict:	dict subclass that remembers the order entries were added
# defaultdict:	dict subclass that calls a factory function to supply missing values
# UserDict:		wrapper around dictionary objects for easier dict subclassing
# UserList:		wrapper around list objects for easier list subclassing
# UserString:	wrapper around string objects for easier string subclassing

#factory function: takes as input a string and returns an object
#Example:
class Shape(object):
    # Create based on class name:
    def factory(type):          #this is the factory function
        #return eval(type + "()")
        if type == "Circle": return Circle()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)
class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

shape = Shape.factory("Circle")
shape.draw()
shape.erase()
###############################################################################

#Assert statement: sanity-check (like a raise-if-not statement)
#an expression is tested, and if the result comes up false, an exception is raised

#AssertionError exceptions can be caught and handled using try-except

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

###############################################################################

## *args **kwargs: allows to pass a variable number of arguments to a function

#*args --> sends non-keyworded list
#**kwargs --> pass keyworded arguments to a function


#*args used to unpack a list to pass multiple arguments (or key-value arguments) to a function
val = [1, 2, 3]
print(*val, sep = '\n')
#1
#2
#3


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')
# first normal arg: yasoob
# another arg through *argv: python
# another arg through *argv: eggs
# another arg through *argv: test

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
greet_me(name="yasoob")
# name = yasoob

###############################################################################

## ENUMERATE
#allows us to loop over an iterable and have an automatic counter

my_list = ['apple', 'banana', 'grapes', 'pear']

for counter, value in enumerate(my_list, 1):  #counter starts from 1 (and not from 0)
    print(counter, value)

print(list(enumerate(my_list, 1)))

###############################################################################

## MAP WITH LAMBDA FUNCTION
month, day, year = map(lambda x : int((re.sub("^0", "", x))), input().split())

###############################################################################

## ITERTOOLS


#STACKOVERFLOW question: https://stackoverflow.com/questions/34443946/count-consecutive-characters
#As many have pointed out, your method fails because you're looping through range(len(s))
#but addressing s[i+1]. This leads to an off-by-one error when i is pointing at the last index of s,
#so i+1 raises an IndexError. One way to fix this would be to loop through range(len(s)-1),
#but it's more pythonic to generate something to iterate over.
s = "111000222334455555"
#For string that's not absolutely huge, zip(s, s[1:]) isn't a a performance issue, so you could do:
counts = []
count = 1
for a, b in zip(s, s[1:]):
    if a==b:
        count += 1
    else:
        counts.append((a, count))
        count = 1

#If you do have a truly huge string and can't stand to hold two of them in memory at a time,
#you can use the itertools recipe pairwise.

def pairwise(iterable):
    """iterates pairwise without holding an extra copy of iterable in memory"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.zip_longest(a, b, fillvalue=None)

counts = []
count = 1
for a, b in pairwise(s):
    ...

###############################################################################

class Abstractclass:
    def do_something(self):
        pass

class B(Abstractclass):
    pass

a = Abstractclass()

b = B()


#This is not an abstract class because:
#1) we can instantiate an instance from
#2) we are not required to implement do_something in the class definition of B

#In fact, this simple case of inheritance has nothing to do with


#Python comes with a module which provides the infrastructure for defining
#Abstract Base Classes


#The following code uses abc module and defines an abstract class:
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

c = AbstractClassExample()
#Error: Can't instantiate abstract class AbstractClassExample with abstract methods do_something


#Now we define a subclass using the previously defined abstract class
class DoAdd42(AbstractClassExample):
    pass

d = DoAdd42(4)
#Error: Can't instantiate abstract class DoAdd42 with abstract methods do_something


#The correct way to inherit from an abstract class is:
class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42

class DoMul42(AbstractClassExample):
    def do_something(self):
        return self.value * 42

e = DoAdd42(5)
f = DoMul42(5)
print(e.do_something())
print(f.do_something())


#A class that is derived from an abstract class cannot be instantiated
#unless all of its abstract methods are overridden.


#To implement abstract methods in the abstract class you can invoke them
#with super() call mechanism. This makes it possible to provide some basic
#functionality in the abstract method, which can be enriched by the subclass implementation.

from abc import ABC, abstractmethod
class AbstractClassExample(ABC):

    #abstractmethod
    def do_something(self):
        print("Some implementation!")

class AnotherSubclass(AbstractClassExample):
    
    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubClass!")

x = AnotherSubclass()
x.do_something()
#Some implementation!
#The enrichment from AnotherSubClass!

###############################################################################
