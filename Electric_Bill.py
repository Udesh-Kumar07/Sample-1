C_Name = input("Enter Consumer Name : ")
C_Number = input("Enter Consumer Number : ")
O_Reading = int(input("Enter Old Reading : "))
C_Reading = int(input("Enter Current Reading : "))
used_unit = C_Reading - O_Reading
unit_price = 0

while used_unit > 0:
    if used_unit > 200:
        unit1 = used_unit - 200
        used_unit = used_unit - unit1
        unit_price += unit1 * 9
        #print("Unit1-" + str(unit1))
    elif used_unit <= 200 and used_unit > 150 :
        unit2 = used_unit - 150
        used_unit = used_unit - unit2
        unit_price += unit2 * 7
        #print("Unit2-" + str(unit2))
    elif used_unit <= 150 and used_unit > 100 :
        unit3 = used_unit - 100
        used_unit = used_unit - unit3
        unit_price += unit3 * 5
        #print("Unit3-" + str(unit3))
    else:
        unit_price += used_unit * 3
        #print("Unit1-" + str(used_unit))
        used_unit = 0
print("Electricity Bill")
print("Consumer Name : " + C_Name)
print("Consumer Number : " + C_Number)
print("Used Unit : " + str(C_Reading - O_Reading))
print("Total Bill : Rs " + str(unit_price))

