file = open('youtube.txt','w')

try:
    file.write('Hello, how r u')
finally:
    file.close()


# =================== OR ===========================

with open('youtube.txt', 'w') as file:
    file.write("Hellooo")