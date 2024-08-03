## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent=int(input("Enter your Hostel/PG rent= "))
food=int(input("Enter the amount of food which you ordered= "))
electricity_spend=int(input("Enter the total of electricity spend = "))
charge_per_unit=int(input("Enter the charge per unit of electricity = "))
person=int(input("Enter the preson living in the room : "))

total_bill=electricity_spend * charge_per_unit

output=(food+rent+total_bill)/person
print("Total amount you've to pay is ",output)
