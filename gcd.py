'''check older version to put the 2 numbers that you want to find the gcd of in the command prompt like 'python3 gcd.py 5 15'
thanks'''
'''sub to my youtube channel at https://www.youtube.com/channel/UC-xwmwaB2jXQaLf6iM1zWFw?view_as=subscriber. I have no vids but i have good playlists if anyone watches ninjago or plays minecraft :)'''
L1 = []
L2 = []
#get the divisors for a number
def get_factors(num_input):
    tempList=[]
    counter = 1
    while counter <= int(num_input):
        r = int(num_input) % counter

        if r == 0:
            tempList.append(counter)

        counter+=1
    return tempList
def find_GCD(L1, L2):
    gcdset = set(L1) & set(L2)
    L3 = list(gcdset)
    L3.sort()
    return L3[-1]

num1 = input("Enter your first number here: ")
num2 = input("Enter your second number here: ")

L1=get_factors(num1)
#print (str(L1))
L2=get_factors(num2)
#print (str(L2))

gcd = find_GCD(L1, L2)

print ("The GCD of "+str(num1)+" and "+str(num2)+" is "+str(gcd))
