#! /usr/bin/python3
# Return true if the card number is valid
number = int(input("number please"))
k = 0
d = 0
def isValid(number):

    valid = False
    if prefixMatched(4 , getPrefix(number, 1)): #visa check
        valid |= True # actually its an OR operator used as statement. so True | False => True, boolean OR logic similar to you might have read V(v symbol) in discrete mathematics or related field.
    if prefixMatched(5 , getPrefix(number, 1)): #master check
        valid |= True
    if prefixMatched(6 , getPrefix(number, 1)): #discovery check
        valid |= True
    if prefixMatched(37 , getPrefix(number, 2)): #american express check
        valid |= True

    if getSize(number) < 13 or getSize(number) > 16:
        valid &= False

    result = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if result % 10 != 0:
        valid &= False

    return valid
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    summation = 0
    even = 0
    while number > 0:
        if even == 1:
            summation += getDigit(number % 10)
            even ^= 1 # it's a xor operaotr so basically 1 will become 0 and 0 will become 1 what I actually doing here is making an alternate turn so suppose number is 1213 then so i am traversing from right side (digit 3) its odd place and even = 0, then even = 1 and we are 1 then even = 0 and we are at 2 then even = 1 we are at 1. Now over. So when even = 1 then it is at even place
            number //= 10
    return summation

# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    number *= 2
    return (number % 10) + (number // 10); # suppose number = 8, then number *= 2 will make number = 16, so number % 10 will give 6 and number // 10 will give 1 and we have to return the sum of digits so 1 + 6 = 7. Now suppose number = 3, so number *= 2 will make number = 6, so number % 10 will give 6 and number // 10 will give 0 = 0 + 6 = 6, // it is integer division in python.  
  

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    summation = 0
    odd = 1
    while number > 0:
        if odd == 1:
            summation += number % 10
            odd ^= 1
        number //= 10
    return summation


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return True if str(number).startswith(d) else False


# Return the number of digits in d
def getSize(d):
    return len(str(d))


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    return str(number) if getSize(number) <= k else str(number)[0:k] # actually it works like ternary operator so if condition is true then str(number) will execute else str(number)[0:k] will execute. str(number) just typecasting number to string. getSize(number) returns the no of digits in number. so if its <= k return the number otherwise return its prefix so for example number= 12345, and k = 2 it will return 12, but if k = 5 or more it will return 12345 as string. so "12345"
    print("Enter the credit card number")

print ("valid" if isValid(number) else "invalid")
isvalid(number)
sumOfDoubleEvenPlace(number)
getDigit(number)
sumOfOddPlace(number)
prefixMatched(number)
getSize(number)
getPrefix(number, k)
