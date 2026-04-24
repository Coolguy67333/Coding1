x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x= 5.5

if (type(x) is not float):
    print("true")
else:
    print("false")

x = 20
y = 20

if (x is y):
    print("X & Y ARE THE SAME IDENTITY!")

y = 30

if (x is not y):
    print("X & Y HAVE DIFFERENT IDENTITIES")