#wap to input 3 movie names in list
list = []
movie1 = input('enter 1st movie: ')
movie2 = input('enter 2nd movie: ')
movie3 = input('enter 3rd ovie: ')

list.append(movie1)
list.append(movie2)
list.append(movie3)

print(type(list))
print(list)


#wap to check if list is palindrome
list1 = ['Hello', 'Kafia', 'Kafia', 'Hello']
list2 = [1,2,1]

copy_list1 = list1.copy()
copy_list2 = list2.copy()

reverse_list1 = list1.reverse()
copy_list1.reverse()

reverse_list2 = copy_list2
copy_list2.reverse()

if copy_list1 == copy_list1:
    print("list1 is Palindrome")
else:
    print("list1 is not Palindrome")   


if copy_list2 == copy_list2:
    print("list2 is Palindrome")
else:
    print("list2 is not Palindrome")



#list count operation
grades = ['D', 'A', 'A', 'B', 'B', 'A']
print(grades.count('A'))

#list sort operstion
grades = ['D', 'A', 'A', 'B', 'B', 'A']
grades.sort()
print(grades)