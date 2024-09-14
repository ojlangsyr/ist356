from datetime import datetime, timedelta

today = datetime.now()

print(today)

birthday = input("Enter your date of birth: ")

test = datetime.strptime(birthday,"%m/%d/%Y")

test = test + timedelta(days=15)

test_str = test.strftime("%A, %B %d %Y")
print(test_str)