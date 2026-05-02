units = int(input("Please enter the number of units you consumed: "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units <= 100):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

elif(units <= 150):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

else:
    amount = 130 + 162.50 +((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill = %.2f" %total)