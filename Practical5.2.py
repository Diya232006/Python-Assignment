# Input prices of sold items in a tuple
prices = tuple(float(x) for x in input("Enter prices separated by space: ").split())

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Price of cheapest item
print("Cheapest item price:", min(prices) if prices else "No items")

# c) Price of costliest item
print("Costliest item price:", max(prices) if prices else "No items")

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
if prices:
    costliest = max(prices)
    count_costliest = prices.count(costliest)
    print("Number of costliest items sold:", count_costliest)
else:
    print("Number of costliest items sold: 0")