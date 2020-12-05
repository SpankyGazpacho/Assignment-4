import sys
import CheckPath
import Read
import Alter
import Write
numofargs = len(sys.argv)

if numofargs == 3:
    # run normally
    splitoutput = sys.argv[2].split("\\")

    if len(splitoutput) == 1:
        destpath = "C:\\Test\\" + str(sys.argv[2])
    else:
        destpath = sys.argv[2]

    sourcepath = sys.argv[1]

    sourcecode = CheckPath.checkfileexist(sourcepath)
    destcode = CheckPath.checkfileexist(destpath)

    if (sourcecode == 1) & ((destcode == 1) | (destcode == 4)):
        inptext = Read.read(sourcepath)
        ouptext = Alter.alter(inptext)
        Write.write(destpath, ouptext, destcode)
    else:
        # error codes based sourcecode and destcode
        if destcode == 2:
            print("The destination path is folder, not a filename!")
        if destcode == 3:
            print("THIS IS YOUR FAULT: An unexpected error has occurred with the destination path")
        if sourcecode == 2:
            print("The source path is a folder not a file!")
        if sourcecode == 3:
            print("THIS IS YOUR FAULT: An unexpected error has occurred with the source path!")
        if sourcecode == 4:
            print("The source path does not exist!")
else:
    # error based on number of arguments
    if (numofargs == 1) | (numofargs == 2):
        print("You need to specify input and output paths!")
    if numofargs > 3:
        print("You put too many arguments!")
