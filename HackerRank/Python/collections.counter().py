from collections import Counter
# https://docs.python.org/3/library/collections.html#module-collections

# Enter your code here. Read input from STDIN. Print output to STDOUT
X = int(input())
shoes = map(float, input().split())

# stock = dict()
# for size in shoes:
#     stock[size] = stock.get(size, 0) + 1

stock = Counter()
for size in shoes:
    stock[size] += 1

customers = int(input())
revenue = 0
for i in range(customers):
    vals = list(map(float, input().split()))
    customer = {"size": vals[0], "price": vals[1]}
    # if stock.get(customer["size"], 0) > 0:
    if stock[customer["size"]] > 0:
        revenue += customer["price"]
        # stock[customer["size"]] = stock[customer["size"]] - 1
        stock[customer["size"]] -= 1

print(int(revenue))
