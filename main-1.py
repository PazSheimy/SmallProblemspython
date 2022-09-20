#Sheimy Paz
#Class CNT 4104
'''
Calculate a meal's price with tax and tip.
Tiprate can be changed but Tax is constant.
Adding while loop, list, string manipulation, and for loop.
'''

# few "constants"
TAXRATE = .065
TIPRATE = .18
tip = 0.0

if __name__ == '__main__':
    prices = []
    total = 0.0

    while True:

        item = input("Did you bough an item? ")
        if item.lower().startswith("n"):
            print("No item was purchased")
            break
        else:
            itemPrice = float(input("How much does the item cost"))
            if itemPrice > 0:
                prices.append(itemPrice)
                print("item add to list")
                print(f"{prices}")

    if len(prices) < 1:
        print("Must enter a valid value")
    else:
        for i in prices:
            print(str("Item price was: " + "{:.2f}".format(i)))
            total += i

            # print suggested tip rate
    print(f"Suggested tip is {TIPRATE * total}")

    # getting users desired tip
    tip = float(input("Enter desire tip"))
    if tip <= 0:
        print(f"Tip was less that 0 {tip}")
    else:
        print(f"Tip was {tip}")

     # Finally print a whole message "With a tip of the tip price (rounded) your cost is fullprice (rounded)"
        print(f"Meal Price was {total}")
        print(f"Meal Tax rate was {total * TAXRATE}")
        print("Tip was %.2f" % (tip))

        print(f"Meal Price was {total} ag")

        itemPrice += (total * TAXRATE) + tip
        print("Your total meal price including tax and tip was: %.2f" % (itemPrice))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/