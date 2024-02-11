# Problem: Given a string, find the first non-repeated character.

str = "speeches"

for char in str:
    if str.count(char) == 1:
        print("First non-repeated character is:",char)
        break