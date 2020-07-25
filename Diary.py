import pathlib
import datetime


file = pathlib.Path("diary.txt")
if file.exists ():
    f = open("diary.txt", "a")
    timestamp = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    f.write("\n" +  timestamp+ ": Now the file has more content!")
    f.close()

else:
    print ("File not exist")
    



