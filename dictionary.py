myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

value = []
key = []
for a, b in myData.items():
    value.append(b)
    key.append(a)
    print("Key:", a , "Value:", b)
print("All keys:", key)
print("All value:", value)
