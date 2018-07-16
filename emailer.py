import os
from marrow.mailer import Mailer, Message
from key import *

def emailMessage():
    print("")
    print("\nWhat is the email message? (or leave blank)")
    plain = input()

    print("")
    print("\nIs the email message correct?")
    print("%(message)s" % {'message': plain})
    print("Y or N")
    answer = input()
    answer = str.upper(answer)

    if answer == "Y":
        return plain
    elif answer == "N" or "":
        return emailMessage()

def emailClient(mailer, userName, clientName, clientNum, clientFileName, plain=""):
    """Email the new file to any client."""
    
    if plain == "":
        plain = "Documents attached."

    mailer.start()
    message = Message(
        author=userName,
        to=clientKey[clientName]['client'],
        cc=emailKey[clientNum],
        bcc=userName,
        subject=clientFileName[1],
        plain=plain
    )
    message.attach(clientFileName[0])
    mailer.send(message)
    mailer.stop()

    os.remove(clientFileName[0])