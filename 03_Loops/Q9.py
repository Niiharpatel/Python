# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for i in items:
    if i in unique_item:
        print("Duplicate:", i)
        break
    unique_item.add(i)