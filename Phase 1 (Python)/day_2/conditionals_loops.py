# Day 2: Conditionals & Loops in Python

# 1️⃣ If-Else Condition
num = 10
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# 2️⃣ For Loop (Printing numbers 1 to 5)
for i in range(1, 6):l
    print(i)

# 3️⃣ While Loop (Printing numbers 10 to 1)
x = 10
while x >= 1:
    print(x)
    x -= 1

# 4️⃣ Break Statement (Stops loop when num = 3)
for num in range(1, 6):
    if num == 3:
        break
    print(num)

# 5️⃣ Continue Statement (Skips number 3)
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 6️⃣ Looping Through a Dictionary
countries = {"India": "Delhi", "USA": "Washington", "Japan": "Tokyo"}
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")
