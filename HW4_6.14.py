n = {1,101,201,301,401,501,601,701,801,901}

def calcPi(n):

    pi,numer = 0,4.0

    for i in range(n):

        denom = (2*i+1)

        term = numer/denom

        if i%2:

            pi -= term

        else:

            pi += term

    return(pi)

  
print("i"," ","m(i)")
for i in n:
    print(i," ",calcPi(i))
