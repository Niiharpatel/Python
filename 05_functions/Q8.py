# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def kw_args(**kwargs):
 for key, value in kwargs.items():
    print(f"{key}: {value}")
    
kw_args(name="guru",age="24")