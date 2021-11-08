fileName = input("Enter Filename:")
try:
    f = open(fileName) #Open the file as requested
    words = [] # make an empty list for the words
    for x in f:
        words = x.strip().split(" ")
    words = list(set(words))# make the set into a list
    words.sort() #sort the list
    print(words)
    f.close()

except FileNotFoundError as f:
    print("\nFile",fileName,"could not found. Try again.")
except Exception as e:
    print("Exception..")
