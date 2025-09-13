menu = {
    "Burger": 200,
    "Fries": 100,
    "Drink": 80
}
total_price = 0
items = []
added_items = set()
print("MENU:")
for item, price in menu.items():
    print(f"{item} - Rs.{price}")

while True:
    order_ask = input("Write your order: (q to quit): ")

    if order_ask == 'q':
        break
    if order_ask in menu:

        if order_ask in added_items:
            print("your item exists!")
        else:
            items.append(order_ask)

            added_items.add(order_ask)
            total_price += menu[order_ask]
            print(f"{order_ask} added!")
    else:
        print("not available")




print("------- THANK YOU ------")
print("Your items: ", f"{items}")
print("Total Items: ", len(items))
print("Total Bill: Rs.", total_price)
