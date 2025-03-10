print("welcome to tip caliculator!!")

bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

print(bill_with_tip)

total_pay = round(bill_with_tip / people)

print(total_pay)