from random import sample, randrange
flag = 0
prices = []

TIPRATE = 0.18
TAXRATE = 0.06
used = set()

def get_tip(total):
    print(f"Suggested tip is ${TIPRATE * total}")
    tip = float(input("Enter desire tip"))
    if tip <= 0:
        print(f"Tip was less that $0 {tip}")
    else:
        print(f"Tip was ${tip}")
        return tip

def get_checkexitflag(flag = "n") -> str:


    if flag.upper().startswith("N"):
        return "move to part 4 i have to implemented"
    get_order()

def get_order() -> list:
    dictionaryitems = {"item1": 1.00,
                  "item2": 2.00,
                  "item3": 3.00,
                  "item4": 4.00,
                  "item5": 5.00,
                  "item6": 6.00}

    while True:
        saveitem= float(input(f"What items would you like to order\n {dictionaryitems} "
                              f"+ enter 0 if you dont want to buy anything"))
        if saveitem > 0:
            prices.append(saveitem)
            print("item add to list")
            print(f"{prices}")


        else:
            if len(prices) < 1:
                print("Must enter a valid price")
                break
            else:
                print("here")
                total = 0
                for i in prices:
                    print(str(f"Item purchase for: ${i}"))
                    total += i

                print(f"The total for your purchase is {total}")
                print(f"The total Tax sales for your purchase is {TAXRATE}")
                print(f"Your total amount is {total * TAXRATE}")
                get_tip(total)
            break







if __name__ == '__main__':
    checkexitflag = input("Would you like to order using check exit? (y/n)? ")
    get_checkexitflag(checkexitflag)
