def createfile(name):
    _file = open(name, 'w')
    _file.close()


def editfile(thefile, new_text):
    with open(thefile, 'w') as db:
        db.write(new_text)


def resetall(thefile):
    with open(thefile, 'w') as db:
        editfile(thefile, '')


def getdata(thefile, take_off_list_format=False):
    with open(thefile, 'r') as db:
        if take_off_list_format is False:
            book = str(db.readlines())
        elif take_off_list_format is True:
            book = str(db.readlines()).replace('[', '').replace("'", '').replace("'", '').replace(']', '')
    return book


def appendtext(thefile, appending_text):
    editfile(thefile, getdata(thefile, True) + appending_text)


def removefile(thefile):
    import os
    os.remove(thefile)


def renamefile(old_name, new_name):
    import os
    os.rename(old_name, new_name)


def savetime(thefile, separator, hour, minute, second, milliseconds=''):
    editfile(thefile, str(hour) + separator + str(minute) + separator + str(second) + separator + str(
        milliseconds))


def version():
    with open('version.txt') as v:
        return str(v.readlines()).replace("['", '').replace("']", '')
