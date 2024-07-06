#programs on Escape Characters
print("kafia loves python\n")
print("Kafia is learning python\n")
print("I study at Lords College.\t Himayatsagar")
print("hello\\ i am a student\\")
print("\"I love python\"")
print("\'ilovepython\'")


#programs on Bitwise Operators
num_items = int(input("Enter the number of items: "))
cost_per_item = float(input("Enter the cost per item : $"))

#calculation
total_cost_before_tax = num_items * cost_per_item 
 
#assume 10% tax rate 
tax_rate = 0.1
tax_amount = total_cost_before_tax * tax_rate

#total cost with tax
total_cost_after_tax = total_cost_before_tax + tax_amount

#Display the results 
print("\nResults: ")
print("\nTotal cost before tax : ${:.2f}",format(total_cost_before_tax))
print("\nTax amount (10%): ${:.2f}",format(tax_amount))
print("\nTotal cost after tax: ${:.2f}",format(total_cost_after_tax))



#programs on variables & Data Types
length = float(input("Enter the length of the rectanle: "))
width = float(input("Enter the width of the rectangle: "))

#calculation
area = length * width 

#Display the results 
print("\nResults: ")
print("Area of rectangle: {:.2f} sqquare units",format(area))


#Input Varaiables
a = int(input("Enter the value to the variable : "))
b = int(input("Enter the value to the variable : "))

#Displaying values before swapping 
print("Before Swapping: ")
print("a =",a)
print("b =",b)

# Swapping the values 
a = a + b 
b = a - b 
a = a - b 

# Displaying the values after swapping 
print("\nAfater swapping: ")
print("a =",a)
print("b =",b)