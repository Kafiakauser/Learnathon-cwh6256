dict = {
    "Name" : "Kafia",
    "Class" : "IT-A",
    "College" : "Lords college",
}
print(dict)

print(dict["Name"])


#Nested dictionary
student = {
    "Name" : "kavita",
    "subjects" : {
        "phy" : 20,
        "chem" : 18,
        "maths" : 20,
        "bio" : 19
    }

}

#dictionary methods
print(student.keys())

print(list(student.keys()))

print(len(student.keys()))

print(student.values())

print(list(student.values()))

print(len(student.values()))

print(student.items())

print(list(student.items()))

#print(student['Name1']) --> #error
print(student.get('Name1')) #-->None

student.update({'city' : 'Hyd'})
print(student)


#Sets

collection = {1,2,3,4,"heelo", "world"}
print(collection)
print(type(collection))
print(len(collection))

collection1 = {}     #syntax for creating empty dictionary
print(type(collection1))
collection2 = set() #syntax for creating empty set
print(type(collection))
#set methods
collection2.add(1)
collection2.add("hello")
collection2.add((1,2,45,25,5))
collection2.add(5)
collection2.add(5)
collection2.remove(5)
collection1.clear()
print(collection1)
print(collection2.pop())
print(collection2.pop())
print(collection2.pop())

#union & intersection methods
set1 = {1,2,3,4,5}
set2 = {5,6,3,25}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))

#Practicee
#1st Qn
dict1 = {"table" : ("Apiece of furniture,"
                    " List of facts & figures"), "cat" : "a small animal"}
print(dict1)

#2nd Qn

classroom = {"python", "java", "C++", "python", "Javascript", "java", "python","java", "C++", "C"}
print(classroom)
print(len(classroom))

#3rd Qn
marks = {}
print(type(marks))
x = int(input("enter phy : "))
marks.update({"phy" : x})
y = int(input("enter maths : "))
marks.update({"maths" : y})
print(marks)

#4th Qn
store = set()
store.add(int(9))
store.add(str(9.0))
print(store)

values = {
    ("float", 9),
    ("int", 9.0)}
print(values)
