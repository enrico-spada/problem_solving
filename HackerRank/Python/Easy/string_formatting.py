# https://www.python.org/dev/peps/pep-3101/
# https://stackoverflow.com/questions/40123901/python-integer-to-hex-string
        #'0x{:02x}'.format(integer)

# https://pyformat.info


n = int(input())
width = len("{:b}".format(n))
for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width))

#"{0:{width}d}.format(i, width = width)
#print the element 0 of the format list
#padded by width characters defined by width parameters of format list
#formatted as d (decimal number)
