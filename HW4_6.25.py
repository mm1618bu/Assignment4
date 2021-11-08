#! /usr/bin/python3
# Reverse the number
def reverse(x):
 
    rev = 0;
    while (x > 0):
        rev = (rev * 10) + x % 10;
        x = int(x / 10);
 
    return rev;
 
#Generate the emirp number
def printEmirp(n):
 
    #Make an array to determine if correct
    prime = [1] * (n + 1);
    p = 2;
    while (p * p <= n):
         
        # Determine if prime
        if (prime[p] == 1):
             
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = 0;
        p += 1;
 
    # Traverse prime numbers
    for p in range(2, n + 1):
        if (prime[p] == 1):
             
            # reverse a number
            rev = reverse(p);
 
 
            if (p != rev and rev <= n and
                       prime[rev] == 1):
                print(p, rev, end = " ");
     
                # Mark reverse prime as false
                prime[rev] = 0;
 
# Run Program
n = 1000;
printEmirp(n);
