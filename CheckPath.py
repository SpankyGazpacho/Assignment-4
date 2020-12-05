import os


def checkfileexist(file):
    if os.path.exists(file):
        if os.path.isfile(file):
            code = 1
            # path ends with a valid filename
        elif os.path.isdir(file):
            code = 2
            # path ends with a folder
        else:
            # I have no idea what you just put in
            code = 3
    else:
        # Path does not exist
        code = 4
    return code
