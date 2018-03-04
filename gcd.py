L1 = []
L2 = []
L3 = []
num1=6
num2=36

#get the divisors for a number
def get_factors(num_input):
    tempList=[]
    counter = 1
    while counter <= num_input:
        #print("This is working inside while loop")
        r = num_input % counter

        if r == 0:
            #print("This is working inside if loop")
            tempList.append(counter)

        counter+=1
    return tempList


#print ("checking factors for "+str(num1))
L1=get_factors(num1)
L2=get_factors(num2)
#print('out of func all good')
print(str(L1))
print(str(L2))
