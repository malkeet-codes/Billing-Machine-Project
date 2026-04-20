#BILL MACHINE

#welcome & menu
print("""HELLO JI,
      WELCOME TO GILL DI RASOI""")
print("HERE IS YOUR MENU:")
menu={ 
     "SHAHEE PANEER" : 280,
     "TANDOORI MOMOS" : 160,
     "CHILLI PANEER" : 270,
     "NOODLES" : 130,
     "SHAWRMA" : 120,
     "KFC CHAAP" : 290,
     "AFGHANI CHICKEN" : 320,
     "EGG CHICKEN ROLL" : 90,
     "SEEKH KABAB" : 100,
     "SUSHI" : 200
}
print(menu)

for item, price in menu.items():
     print(item, ":", price)

bill=0

#blank list of order
order=[ ]

#number of items should be ordered
noofitems=int(input("HOW MANY ITEMS DO YOU WANT TO ORDER?"))


for i in range(noofitems):
    items=input("Enter item name:").lower()
    quantity=int(input("ENTER THE QUANTITY OF ITEM"))

    if item in menu:
         order.append(item)
         bill += menu[item]*quantity
    else:
         print("Sorry, item not available")

print("\nYOUR FINAL ORDER IS:",order)
print("Thank you for ordering from Gill Di Rasoi","\U0001F600")
print(bill)