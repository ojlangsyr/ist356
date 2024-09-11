number = int(input("What is your number grade?"))
if number >= 95 and number > 75:
    grade = "A"
elif number >= 75 and number > 50:
    grade = "B"
elif number >= 50:
    grade = "C"
else:
    grade = "F"

print(f"you got a {grade}")
