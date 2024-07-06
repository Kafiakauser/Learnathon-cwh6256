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