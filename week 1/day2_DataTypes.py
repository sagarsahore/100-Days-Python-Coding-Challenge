#subscripting
print("Hello"[-1]) #-1 will take the last charactor 

#Integer = whole Number
print(1234+2345)

### BMI Calculator
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/(height**2)
print(round(bmi,3))
print(6 + 4 / 2 - (1 * 2))
a = int("5") / int(2.7)
print(round(a,3))

#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")10
