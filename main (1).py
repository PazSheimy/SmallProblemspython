#Sheimy Paz
#Class CNT 4104
'''
Calculate a meal's price with tax and tip.
Tiprate can be changed but Tax is constant.
'''

# few "constants"
TAXRATE = .065
TIPRATE = .18
tip = 0.0


if __name__ == '__main__':
    price = 0.0

#getting and process the meal price as float
    price = float(input("what is the price meal"))

#if price is 0 or negative: then print out an "invalid price" notice
if price <= 0:
   print("Invalid Price. Enter correct amount please.")

#if price is a dollar or less then no tax or tip will be calculated
# instead print a message with the meal price then " but no tax or tip"
elif 0 < price < 1:
   print(f"Meal price is {price}")

else:
#print suggested tip rate
   print(f"Suggested tip is {TIPRATE*price}")

#getting users desired tip
   tip = float(input("Enter desire tip"))
   if tip <= 0:
       print(f"Tip was less that 0 {tip}")
   else:
       print(f"Tip was {tip}")

# Finally print a whole message "With a tip of the tip price (rounded) your cost is fullprice (rounded)"
   print(f"Meal Price was {price}")
   print(f"Meal Tax rate was {price*TAXRATE}")
   print("Tip was %.2f" % (tip))

   price += ((price * TAXRATE) + tip)
   print("Your total meal price including tax and tip was: %.2f" % (price))
