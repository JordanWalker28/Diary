import pathlib
import datetime

def writeToFile(entry):
    file = pathlib.Path("diary.txt")
    if file.exists ():
        f = open("diary.txt", "a")
        timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        f.write("\n" +  timestamp+ ": " + entry)
        f.close()

    else:
        print ("File not exist")
    
    return

def makeEntry():
    entry = input()
    writeToFile(entry)
    
while True:
    makeEntry()
