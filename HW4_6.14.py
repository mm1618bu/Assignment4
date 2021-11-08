# numbers that will be passed through
n = {1,101,201,301,401,501,601,701,801,901}

#define the function to get pi
def calcPi(n):
    #set the value of pi and the value of numer
    pi,numer = 0,4.0

    for i in range(n):
        # for each item in n, multiply by 2 and add 1
        denom = (2*i+1)
        # get the result by dividing the numerator and denominator
        term = numer/denom

        if i%2:

            pi -= term

        else:

            pi += term

    return(pi)

#print the results in a table
print("i"," ","m(i)")
for i in n:
    print(i," ",calcPi(i))
