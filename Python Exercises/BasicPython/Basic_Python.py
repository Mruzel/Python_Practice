print("Hello Python")

name = "Mahfuj"
print("Hello " + name + ", " "welcome" )

print("My name is Mahfuj")
print("""I am very much excited to learn Python, 
it looks interesting and fun so far.
This is really easy to learn""")

print(3 + 2)
print(9999 - 6666)
print(9999 / 3333)
print(3333 * 3)
print(2 ** 3)

length = 9
width = 5
area = length * width
print(area)

print("Name: Mahfuj Ruzel")
print("Age: 38")
print("Hobby: Play Cricket")

name =("Mahfuj Ruzel")
print("Hello, " + name + " ! ")

for i in range(1, 6):
    print(i * 3)

for i in range(1, 7):
    print(i * 4)

for i in range(1, 9):
    print(i * 2)

print("3 + 5 =", 3 + 5 )
print("5 - 3 =", 5 - 3)
print("10 / 5=", 10 / 5)
print("3 * 2 =", 3 * 2)
print("3 ** 2=", 3 ** 2)

print("333 + 333=", 333 + 333)
print("10 / 3=", 10 / 3)

age = 38
current_year = 2025
birth_year = current_year - age
print("My Birth Year is: ", birth_year)

age = int(input("Enter your current age: "))
current_year = int(input("Enter current year: "))
birth_year = current_year - age
print("Your Birth Year is:", birth_year)

x = 5
y = 5.5
name = "mahfuj"
is_active = True
print("X is of type:", type(x))
print("Y is of Type:", type(y))
print("name is of type:", type(name))
print("Is active is of type:", type(is_active))

a = 10
b = 20
print("Before Swapping: a=", a, "b=", b )

a, b = b, a
print("After Swapping: a=", a, "b=", b)

a = 20
b = 10
print("Before Swapping: a=", a, "b=", b)
a, b = b, a
print("After Swapping: a=", a, "b=", b)

principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100
print("The Simple Interest is:", simple_interest)

num = 10
num_str = str(num)

print("Integer to String:", num_str)


flt = 5.67
flt_int = int(flt)
print("Float to Integer:", flt_int)

str_num = "12.34"
str_flt = float(str_num)
print("String to Float:", str_num)


first_name = "Mahfuj"
last_name = "Ruzel"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Updated list:", numbers)


fruits = ["Apple", "Banana", "Lemon", "Date"]
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

persons = {"name": "Mahfuj", "age": 39, "city": "New York"}
print("Name:", persons["name"])
print("Age:", persons["age"])
print("CIty:", persons["city"])

name = "mahfuj"
print(name)

name = "Mahfj"
print(name)
