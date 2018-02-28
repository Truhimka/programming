print("Task 1")

text = "i wish eat your cancer"

while "." in text:
    print(text.capitalize())
    break
else:
    print(text.capitalize()+".")

print(" ")
print("Task 2")
number = int(input("Enter number"))

if number % 3 and number % 5:
    number == 0
    print(number)
elif number % 3:
    number > 0
    print("Only 5")
elif number % 5:
    number > 0
    print("Only 3")
else:
    print("Two ways possible")


print(" ")
print("Task 3")

text = "adwDsghwIhwEjwPLkwaS"
lst = ""

for i in text:
    if i.istitle():
        lst += i
    else:
        continue
print(lst)
