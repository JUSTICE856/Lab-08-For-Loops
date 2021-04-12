myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
mykeys = []
myValues = []

# iteration in parrallel
for k, v in myData.items():
    print("key: " + str(k) + ", value: " + str(v))
    mykeys.append(k)
    myValues.append(v)

print("ALL KEYS: " + str(mykeys))
print("ALL VALUES: " + str(myValues))
