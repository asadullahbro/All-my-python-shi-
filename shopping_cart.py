things = ("apple", "banana", "orange")
items = []
added_items = set()

while True:
    thing = input("Add an thing: (q to quit) ")
    if thing == "q":
        break
    if thing in things:
        if thing in added_items:
            print("Item Exists in the cart")
        else:
            items.append(thing)
            added_items.add(thing)
            print(f"Added {thing}")
    else:
        print("Not available.")


print("---- THANK YOU ----")
print()
print("Things", f"{items}")