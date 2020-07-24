import pathlib

file = pathlib.Path("diary.txt")
if file.exists ():
    f = open("diary.txt", "a")
    f.write("Now the file has more content!")
    f.close()

    #open and read the file after the appending:
    f = open("diary.txt", "r")
    print(f.read())
else:
    print ("File not exist")
    



