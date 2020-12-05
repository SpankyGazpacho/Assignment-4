import platform
import getpass
from datetime import datetime


def alter(inputtext):

    os = str(platform.system())
    uname = str(getpass.getuser())
    daytime = str(datetime.now())

    header = os + '\n' + uname + '\n' + daytime + '\n'

    spltext = inputtext.split('\n')
    proctext = ''

    for i in range(len(spltext)):
        proctext += (str(datetime.now().time()) + ' ' + spltext[i] + '\n')

    finaltext = header + proctext
    return finaltext
