phone_book = dict()

n = int(input())
for record in range(n):
    line = input()
    line = line.split()
    name = line[0]
    number = int(line[1])
    phone_book[name] = phone_book.get(name, number)

while True:
    query = input()
    if query == "":
        quit()
    if query in phone_book:
        print("%s=%s" % (query, phone_book[query]))
    else:
        print("Not found")
