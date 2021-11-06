largestnum = 0


for i in range (0 ,5):
    userinput= input("Number please...")
    usernum = int(userinput)
    if  usernum > (largestnum):
        largestnum = usernum
print(largestnum)
