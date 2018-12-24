# #1) Pass it as a TUPLE
# def print_full_name(a, b):
#     print("Hello %s %s! You just delved into python." % (a, b))


# #2) Pass it as a DICTIONARY
# def print_full_name(a, b):
#     print("Hello %(first_name)s %(last_name)s! You just delved into python." % {"first_name": a, "last_name": b})


# #3) Use NEW-STYLE FORMATTING:
# def print_full_name(a, b):
#     print("Hello {} {}! You just delved into python.".format(a, b))


# #4) Use NEW-STYLE FORMATTING WITH NUMBERS:
# def print_full_name(a, b):
#     print("Hello {0} {1}! You just delved into python.".format(a, b))


# #5) Use NEW-STYLE FORMATTING WITH EXPLICIT NAMES:
# def print_full_name(a, b):
#     print("Hello {first_name} {last_name}! You just delved into python.".format(first_name = a, last_name = b))

# #6) CONCATENATE strings:
# def print_full_name(a, b):
#     print("Hello " + a + " " + " " + b + "! You just delved into python.")

#THE CLEAREST TWO ARE:
# #7) Pass the values as PARAMETERS:
# def print_full_name(a, b):
#     print("Hello ", a, " ", b,"! You just delved into python.", sep = "")


#8) Use f-string formatting in Python 3.6:
def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")



if __name__ == '__main__':
    first_name = "Enrico"
    last_name = "Spada"
    print_full_name(first_name, last_name)
