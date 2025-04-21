class Converter:
    def __init__(self, value, unit):
        self.unit= unit
        self.value=value
        convert_to_feet={"Feet":self.value, "Inche":self.value/12, "Yard":self.value*3, "Mile":self.value*5280, "Millimeter":self.value/304.8,  "Centimetre":self.value/30.48, "Meter":self.value*.281, "Kilometer":self.value*3281}
        self.feet = convert_to_feet[self.unit]
        self.conversions={"Inch":self.feet*12, "Yard":self.feet/3, "Mile":self.feet/5280, "Millimeter":self.feet*304.8, "Centimetre":self.feet*30.48, "Meter":self.feet/3.281, "Kilometer":self.feet/3281}
    def feet(self):
        return self.feet
    def inches(self):
        return self.conversions["Inches"]
    def yards(self):
        return self.conversions["Yards"]
    def miles(self):
        return self.conversions["Miles"]
    def milimeters(self):
        return self.conversions["Millimeter"]
    def centimeters(self):
        return self.conversions["Centimetre"]
    def meters(self):
        return self.conversions["Meter"]
    def kilometer(self):
        return self.conversions["Kilometer"]
data=input("Enter value,unit:\t")
lst=data.split(',')
conversion_obj=Converter(float(lst[0]), lst[1].title())
print("""Enter your choice:
      1. inches
      2. feet
      3. yards
      4. miles
      5. kilometers
      6. meters
      7. centimeters
      8. millimeters.
      """)
choice =int(input("Enter Choice:\t"))
if choice == 1:
    print(conversion_obj.inches())
elif choice == 2:
    print(conversion_obj.feet())
elif choice == 3:
    print(conversion_obj.yards())
elif choice == 4:
    print(conversion_obj.miles())
elif choice == 5:
    print(conversion_obj.kilometer())
elif choice == 6:
    print(conversion_obj.meters())
elif choice == 7:
    print(conversion_obj.centimeters())
elif choice == 8:
    print(conversion_obj.milimeters())
else:
    print("Wrong choice")