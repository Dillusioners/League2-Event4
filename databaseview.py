a = input("Welcome to data structure viewer.\nPress ENTER to continue")
kw = int(input("How many fields would you like?(includes values for fields too): "))
fieldl = []
valuel = []

while kw != 0:
    field = input("Enter a field: ")
    value = input("Enter the value for field " + field + ": ")
    if(field == ""):
        print("Enter the field with its value again.(Reason: Invalid Field)");
    else:
        fieldl.append(field)
        valuel.append(value)
        kw -= 1

print("                             FIELDS AND VALUES AS FOLLOWS\n")
while kw != len(fieldl):
    print("                                     |", fieldl[kw]+" =======> "+valuel[kw]+" |")
    kw += 1