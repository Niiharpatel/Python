# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = "Dog"
age = 3

if species == "Dog":
    if age < 2:
        food =  "Puppy food"
    elif 2<= age < 5:
        food = "Adult food"
    else:
        food = "Senior food"
elif species == "Cat" and age > 5:
        food = "Senior food"
 
print(food)