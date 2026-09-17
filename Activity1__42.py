classmates = ["Bob", "Jack", "Pheona", "Aarav"]
print(classmates)

print(len(classmates))
print (classmates[0])
print (classmates[-1])
print(classmates [:3])

classmates.append("Fred")
print(classmates)
classmates.remove("Bob")
print(classmates)
classmates.sort()
print(classmates)
teacher = {"name": "Mr. Coyote", "Subject": "Math", "Expierence": "Not Found"}
print(teacher)

teacher["Email"] = "99087653@my.hartdistrict.org"

teacher.pop("Expierence")

print(teacher)





roll_numbers = [1, 2, 3, 4, 5, 6]
names = ["Fred", "Bob", "Gecko", "Gus", "Shawn"]

dict(zip(roll_numbers, names))

print(names[3])

print(names)