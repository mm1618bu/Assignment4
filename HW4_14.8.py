print("Enter the name of the file to open: ")
fileName = input("")
try:
    f = open(fileName)
    words = []
    for x in f:
        words = x.strip().split(" ")
    words = list(set(words))
    words.sort()
    print(words)
    f.close()

except FileNotFoundError as f:
    print("\nFile",fileName,"could not found. Try again.")
except Exception as e:
    print("Exception..")
