from os import listdir
from os.path import getmtime, isfile, join
from datetime import date
import PyPDF2, os, string, time
from marrow.mailer import Mailer, Message
from emailer import emailKey, clientKey
#
# Universal methods for any client
#

def clientFileNamer(clientName):
    """Used to name the new file for any client."""

    print("\nWhat is the new %(client)s file name?" % {'client': clientName})
    emailSubjectName = input()
    clientFileName = emailSubjectName + '.pdf'

    print("\nIs the file name correct?")
    print("%(subject)s" % {'subject': emailSubjectName})
    answer = input("(Y/N) ")
    answer = str.upper(answer)

    if answer == "Y":
        return [clientFileName, emailSubjectName]
    elif answer == "N" or "":
        return clientFileNamer(clientName)

def listScanFiles():
    """List the files in C:/SCANS, and select the one you wish to edit."""

    print("")
    print("\nWhich file would you like to send?")

    path = 'C:/SCANS'
    scanFiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i, f in enumerate(scanFiles):
        index = i + 1

        # Format the seconds since last epoch into a time stamp string.
        secs = os.path.getmtime(join(path, f))
        formatTime = time.localtime(secs)
        modTime = time.strftime("%x %X", formatTime)

        print("%(index)i: %(file)s    Last Modified: %(time)s" %
              {'index': index, 'file': f, 'time': modTime})

    selectedFile = int(input("Enter # "))
    selectedFile = selectedFile - 1

    path = 'C:/SCANS/' + scanFiles[selectedFile]

    return path

#
# Removal methods
#

def rwFile(fileName, back):
    """Open file, copy pages you want to keep, and close the file."""
    
    delete = int(input())

    selectedFile = listScanFiles()

    ogFile = open(selectedFile, 'rb')
    readOgFile = PyPDF2.PdfFileReader(ogFile)
    writeNewFile = PyPDF2.PdfFileWriter()

    ogFileEnd = readOgFile.numPages

    if (back):
        delete = ogFileEnd - delete

    for pageNum in range(delete, ogFileEnd):
        newPage = readOgFile.getPage(pageNum)
        writeNewFile.addPage(newPage)

    newFile = open(fileName, 'wb')
    writeNewFile.write(newFile)
    newFile.close()
    ogFile.close()

def deleteFront(fileName):
    """Used to trim the scanned file by deleting pages from the front."""

    print("\nHow many pages to delete from the front?")
    back = False
    rwFile(fileName, back)

def keepBack(fileName):
    """Used to trim the scanned file by keeping pages at the back."""

    print("\nHow many pages to keep from the back?")
    back = True
    rwFile(fileName, back)

def trimMethod(trim, fileName):
    if trim == 'deleteFront':
        deleteFront(fileName)
    elif trim == 'keepBack':
        keepBack(fileName)
