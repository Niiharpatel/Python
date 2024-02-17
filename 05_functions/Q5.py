# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

# def greet(user):
#     return "Hello, " + user + " !"

# print(greet("Nihar"))

# ================================

def greet(user="Guru"):
    return "Hello, " + user + " !"

print(greet())
print(greet("Nihar"))