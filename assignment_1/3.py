feet=int(input("Enter length in feet: "))
lst=[[feet*12, "Inches"], [feet/3, "Yards"], [feet/5280, "Miles"], [feet*304.8, "Millimeter"], [feet*30.48, "Centimetre"], [feet/3.281, "Meters"], [feet/3281, "Kilometers"]]
choice=int(input("1. Inches\n2. Yards\n3. Miles\n4. Millimeters\n5. Centimeters\n6. Meters\n7. Kilometers\n"))
print(feet, "Feet =", lst[choice-1][0], lst[choice-1][1])