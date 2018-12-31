# Enter your code here. Read input from STDIN. Print output to STDOUT
string, length = input().split()

string = "".join(sorted(string))

from itertools import permutations
for i in permutations(string, int(length)):
    print("".join(i))
