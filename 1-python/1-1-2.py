cost = float(input("what was the total cost? "))
tip = (float(input("what was the tip percentage? ")))/100
dinercount = int(input("how many diners were there? "))
total = ((tip*cost)+cost)
perperson= total / dinercount
print(f"your total is: ${total:.2f}, leaving ${perperson:.2f} per person")

