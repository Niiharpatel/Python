# username = "Nihar"

# def fun():
#     username = 'Guru'
#     print(username)

# print(username)
# fun()

# ====================================

# x = 28

# def fun2(y):
#     z = x + y
#     return z

# result = fun2(10)

# print(result)


# ================== Avoid ==========================
# x = 20

# def fun3():
#     global x
#     x = 30


# fun3()
# print(x)

# ======================================================
x = 20

def f1():
    x = 30
    def f2():
        print(x)
    f2()
f1()