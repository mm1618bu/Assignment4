#! /usr/bin/python3
# Store each pair of state and capitial in a multi-demensional list
unitedStates = [["Alabama","Montgomery"],["Alaska","Juneau"],["Arizona","Phoenix"],["Arkansas","Little Rock"],["California","Sacramento"],["Colorado","Denver"],["Conneticut","Hartford"],["Delaware","Dover"],["Florida","Talahassee"],["Georgia","Atlanta"],["Hawaii","Honolulu"],["Idaho","Boise"],["Illinois","Springfield"],["Indiana","Indianapolis"],["Iowa","Des Moines"],["Kansas","Topeka"],["Kentucky","Frankfort"],["Louisiana","Baton Rouge"],["Maine","Augusta"],["Maryland","Annapolis"],["Massachusetts","Boston"],["Michigan","Lansing"],["Minnesota","Saint Paul"],["Mississippi","Jackson"],["Missouri","Jefferson City"],["Montana","Helena"],["Nebraska","Lincoln"],["Nevada","Carson City"],["New Hampshire","Concord"],["New Jersey","Trenton"],["New Mexico","Santa Fe"],["New York","Albany"],["North Carolina","Raleigh"],["North Dakota","Bismarck"],["Ohio","Columbus"],["Oklahoma","Oklahoma City"],["Oregon","Salem"],["Pennsylvania","Harrisburg"],["Rhode Island","Providence"],["South Carolina","Columbia"],["South Dakota","Pierre"],["Tennessee","Nashville"],["Texas","Austin"],["Utah","Salt Lake City"],["Vermont","Montpelier"],["Virginia","Richmond"],["Washington","Olympia"],["West Virginia","Charleston"],["Wisconsin","Madison"],["Wyoming","Cheyenne"]]
successful = 0 #set the score to zero
for i in range(len(unitedStates)): #for each instance in the list based on the length
    cap= input("What is the capital of "+unitedStates[i][0]+"? ").lower() #ask for the answer and make the inputted answer all lower case
    if cap == unitedStates[i][1].lower(): # if the answer is the same as the input, add 1 point to the score
        successful += 1
        print("Correct")
    else:
        print("Wrong") # if not, print wrong and dont add a point
print(successful) # print the final score
