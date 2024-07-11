#conditional statements

#Elif statements
 
number = int(input("Enter a number : "))
if number > 0: 
    print("Positive Number.")
elif number < 0:
    print("Negative Number.")
else:
    print("zero.")



#Elif statement

score = int(input("Enter the score : "))

if score >= 90:
    print("A")
elif 80 < score < 90:
    print("B")
elif 70 < score < 80:
    print("C")
elif 50 < score < 70:
    print("D")
else:
    print("F")




# Leap year

year = int(input("Enter a year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
   print("It is Leap yaer.")
else:
    print("It is not a leap year.")
