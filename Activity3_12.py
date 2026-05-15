num = int(input("Enter the number: "))
t = num
numLen = 0
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numLen>=4:
    numlen = int(numLen/2)
    chk = 0
    while num> 0:
        rem = num%10
        if chk== numLen:
            midone = rem
        elif chk == (numLen-1):
            midtwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midone*midtwo
    print("\nProduct of Mid digits (" +str(midone)+ "*" +str(midtwo)+ ") = ",prod)

else:
    print("\nIt's not a 4 or more than 4 digit number!")