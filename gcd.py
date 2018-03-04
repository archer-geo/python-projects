
import sys
L1 = []
L2 = []
#get the divisors for a number
def get_factors(num_input):
    tempList=[]
    counter = 1
    while counter <= num_input:
        r = num_input % counter

        if r == 0:
            tempList.append(counter)

        counter+=1
    return tempList
def find_GCD(L1, L2):
    gcdset = set(L1) & set(L2)
    L3 = list(gcdset)
    L3.sort() 
    return L3[-1]

num1=int(sys.argv[1])
num2=int(sys.argv[2])

L1=get_factors(num1)
#print (str(L1))
L2=get_factors(num2)
#print (str(L2))

gcd = find_GCD(L1, L2)

print ("The GCD of "+str(num1)+" and "+str(num2)+" is "+str(gcd))
