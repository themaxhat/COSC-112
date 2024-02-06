def main():
    cost = float(input("How much is the item? "))
    sale = float(input("How much is on sale as a %? "))

    print(bigSale(cost, sale))

def bigSale(c, s):
    item_cost = c * (1 - (s/100))
    return item_cost

main()