name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
for num in numbers:
    sum_numbers += num
print(f"Sum of numbers: {sum_numbers}")

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

grade = int(input("Enter your grade (0-100): "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

for number in numbers:
    if number == 3:
        break  
    print(f"Number: {number}")

for number in numbers:
    if number == 3:
        continue 
    print(f"Number: {number}")