import os


def write(destpath, text, destcode):
    if destcode == 1:
        okflag = input("The output file already exists! Would you like to overwrite it? Y/N: ").upper()
        if okflag == "Y":
            try:
                placeholder = open(destpath, "w")
                placeholder.write(text)
                placeholder.close()
                # exit the program
            except:
                print("An unexpected error has occurred. Please contact your local programmer.")
        elif okflag == "N":
            print("Goodbye!")
            # exit the program
        else:
            print("That's not what I asked for! Goodbye!")
            # exit the program

    elif destcode == 4:
        # check if the path minus the last element is a valid directory
        splitinp = destpath.split("\\")
        if splitinp[-1] == '':
            splitinp.remove('')

        reass = ''
        for i in range(len(splitinp) - 1):
            reass += splitinp[i]
            reass += '\\'

        if os.path.isdir(reass):
            # If path is valid
            placeholder = open(destpath, "w")
            placeholder.write(text)
            placeholder.close()
        else:
            print("The destination path is invalid!")