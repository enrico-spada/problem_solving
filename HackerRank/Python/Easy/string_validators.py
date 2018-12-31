if __name__ == '__main__':
    s = input()

#1) better avoid using eval!
# for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
#         print(any(eval("letter." + test + "()") for letter in s))

#2)
for method in (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper):
    print (any(method(letter) for letter in s))

#3)
# t = type(s)
# for method in (t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper):
#     print (any(method(letter) for letter in s))
