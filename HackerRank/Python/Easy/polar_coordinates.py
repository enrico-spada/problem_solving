# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = complex(input())

print(*cmath.polar(z), sep = "\n")
