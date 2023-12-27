print("LearnPython.py")

# Variables - no declaring variables just set values
x = 5
y = "y"
z = 2.0

# Strings
s = "s"
print(s.upper())
print(s.lower())
print(len(s)) # length of s

# User Input
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
sum = int(num1) + int(num2)
print("num1: " + num1 + ", num2: " + num2 + ", sum: " + str(sum))

# Lists
list = [1,2,3]
print(list[0])
list.append(4)
list.insert(0,0)
list.remove(3)
for x in list:
    print(str(x) + " ")
list.sort()
list2 = list.copy()
print(list2)
list3 = list + list2
print(list3)

# Tuple
tuple = ("a", "b", "c")
print(tuple[1])
for x in tuple:
    print(x)
tuple2 = (1, 2, 3)
tuple3 = tuple + tuple2
print(tuple3)

# Sets
set = {'a', 'b', 'c'}
for x in set:
    print(x)
set.add('d')
set.remove('a')
set2 = {'e', 'f', 'g'}
set3 = set.union(set2)
print(set3)

# Dictionaries
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict)
dict["color"] = "red"
print(dict)
dict.pop("model")
print(dict)
for x in dict:
    print(x)

# If else
if(num1 > num2):
    print("num1 > num2")
elif (num1 < num2):
    print("num1 < num2")
elif (num1 == num2):
    print("num1 = num2")
else:
    print("ERROR")

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# Function - Methods
def fullName(firstName, lastName):
    print(firstName + " " + lastName)
    
fullName("Om", "Janamanchi")