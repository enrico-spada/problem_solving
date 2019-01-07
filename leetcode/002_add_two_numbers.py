class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#SOLUTION 1: 112 ms
#the idea of this solution is to:
#A) for each list:
    #1) convert each ListNode object into list
    #2) convert objects into chr for .join() method [2, 4, 3] --> ["2", "4", "3"]
    #3) reverse the list into the correct order     ["2", "4", "3"] --> ["3", "4", "2"]
    #4) join the list into a single str object      ["3", "4", "2"] --> "342"
    #5) convert str object into int  objects        "342" --> 342
#B) sum up the two numbers                          342 + 465 --> 807
#C) reverse the number                              807 --> "708"
#D) split the result into a str and map to int     "708" --> [7, 0, 8]


# define generator to loop over values contained in ListNode objects
def my_generator(linked_list):
    generator_list = linked_list
    while generator_list:
        yield generator_list.val  #https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        generator_list = generator_list.next

class Solution:
    def addTwoNumbers(self, l1, l2):
#A) List 1
        list1 = [str(i) for i in my_generator(l1)]      #Step 1), 2)
        list1_srt = int("".join(list1[::-1]))           #Step 3), 4) and 5)
#A) List 2
        list2 = [str(i) for i in my_generator(l2)]      #Step 1), 2)
        list2_srt = int("".join(list2[::-1]))           #Step 3), 4) and 5)
#B)
        sum = list1_srt + list2_srt
#C) and D)
        return list(map(int, str(sum)[::-1]))


#SOLUTION 2: 204 ms
#The idea of this solution is to try optimizing the algorithm of Solution 1)
#Maybe the bottleneck resides in the two list comprehensions to apply Step A) each ListNode objects

#How can we convert both ListNode objects into lists inside the same loop,
#considering that l1 and l2 might have different lengths??

#One solution is given by itertools.zip_longest()
import itertools            #required for itertools.zip_longest()
                            #https://docs.python.org/3/library/itertools.html#itertools.zip_longest
#This iterator fills the shortest list with None values,
#therefore, we need to find an effective way to filter out None value

#I create my_filter function to map each list,
#this function will be map-applied to two lists in order to remove "None" values
def my_filter(generated_list):
        return list(filter(lambda x: x != 'None', generated_list))
                                        #"None" because the input list will be composed of chr objects

# define generator to loop over ListNode objects and return a list
def my_generator(linked_list):
    generator_list = linked_list
    while generator_list:
        yield generator_list.val   #https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        generator_list = generator_list.next

class Solution:
    def addTwoNumbers(self, l1, l2):
#A)
        #list comprehension using itertools.zip_longest()
        #zip() allows to unpack the output over multiple objects
        #Step 1), 2)
        list1, list2 = zip(*[[str(a),str(b)] for a, b in itertools.zip_longest(my_generator(l1), my_generator(l2))])
        #Step 3), 4), 5)
        #map my_filter function over both lists and convert into reversed int object
        list1_srtd, list2_srtd = map(lambda x: int("".join(my_filter(x)[::-1])), [list1, list2])
#B)
        sum = list1_srtd + list2_srtd
#C) and D)
        return list(map(int, str(sum)[::-1]))

#I am very unsatisfied of the performance of this solution,
#it appears that map and lambda is not a very efficient combination
#https://stackoverflow.com/questions/1247486/list-comprehension-vs-map


#SOLUTION 3: 116 ms
#Starting from Solution 2, the idea is to change the
#filtering approach needed to remove "None" values inserted by itertools.zip_longest()

#One possible solution is to find the index of first "None" values inside the list
#and slice the list example[0:example.index("None")]
#The problem is that list.index() raises ValueError if no such item
#https://docs.python.org/3/tutorial/datastructures.html

#My solution to this additional problem is using try-except statement

# define generator to loop over ListNode objects and return a list
def my_generator(linked_list):
    generator_list = linked_list
    while generator_list:
        yield generator_list.val   #https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        generator_list = generator_list.next

class Solution:
    def addTwoNumbers(self, l1, l2):
#A)
        #list comprehension using itertools.zip_longest()
        #zip() allows to unpack the output over multiple objects
        #Step 1) and 2)
        list1, list2 = zip(*[[str(a),str(b)] for a, b in itertools.zip_longest(my_generator(l1), my_generator(l2))])

        #List1: Step 3), 4) and 5)
        try:
        #if list.index() does NOT raise ValueError...
        #convert list into reversed integer
            list1_srtd = int("".join(list1[0 : list1.index("None")][::-1]))
        except:
            list1_srtd = int("".join(list1[::-1]))
        #List2: Step 3), 4) and 5)
        try:
            list2_srtd = int("".join(list2[0 : list2.index("None")][::-1]))
        except:
            list2_srtd = int("".join(list2[::-1]))
#B)
        sum = list1_srtd + list2_srtd
#C) and D)
        return list(map(int, str(sum)[::-1]))
