inp = "1 2 3 4"
integer_list = map(int, inp.split())

integer_list = list(integer_list)
# t = tuple(map(int, integer_list))
t = ( *map( int, integer_list ), )   #note the , at the end..
print(hash(t))
