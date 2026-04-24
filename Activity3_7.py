print("Enter Marks Obtained in 5 subjects: ")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

tot = markone+marktwo+markthree+markfour+markfive

avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B2")
elif avg>=61 and avg<71:
    print("Your grade is B2")
elif avg>=51 and avg<61:
    print("Your grade is C1")
elif avg>=41 and avg<51:
    print("Your grade is C2")
elif avg>=33 and avg<41:
    print("Your grade is D")
elif avg>=21 and avg<33:
    print("Your grade is F1")
elif avg>=0 and avg<21:
    print("Your grade is F2")
else:
    print("Invalid Input!")



