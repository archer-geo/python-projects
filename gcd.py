'''check older version to put the 2 numbers that you want to find the gcd of in the command prompt like 'python3 gcd.py 5 15'
thanks'''
'''sub to my youtube channel at https://www.youtube.com/channel/UC-xwmwaB2jXQaLf6iM1zWFw?view_as=subscriber.
I have no vids but i have good playlists if anyone watches ninjago or plays minecraft :)'''
import time
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
    #Find the common factors between the two lists
    gcdset = set(L1) & set(L2)
    L3 = list(gcdset)
    #then sort to put the GCD to the rightmost
    L3.sort()
    #return the topmost which is the GCD!
    return L3[-1]

print("Enter 2 numbers and get their GCD! press CTRL + C to exit. (Note to Mac users: it's still control.) By Rohan Arni")
while True:
    num1 = input("Enter your first number here: ")
    num2 = input("Enter your second number here: ")

    L1=get_factors(num1)

    L2=get_factors(num2)


    gcd = find_GCD(L1, L2)
    print("Calculating........")
    
    print ("The GCD of "+str(num1)+" and "+str(num2)+" is "+str(gcd) + "!")
