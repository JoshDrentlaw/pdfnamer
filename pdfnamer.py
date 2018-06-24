import getpass
import trimmer
from emailer import *
from key import *
from marrow.mailer import Mailer

if __name__ == "__main__":
    print("What is your Outlook User Name?") 
    userName = input()

    print("What is your Outlook Password?")
    password = getpass.getpass('')

    mailer = Mailer(
        dict(
            transport = dict(
                use = 'smtp',
                username = userName,
                password = password,
                tls = 'required',
                host = emailKey[0]
            )
        )
    )

    proceed = True

    while proceed:
        print("\nChoose which client to email.")
        clients = list(clientKey.keys())
        for idx, client in enumerate(clients):
            if client != 'empty':
                print('{}: {}'.format(idx, client))
        print("0: Exit")
        client = int(input('Enter # '))

        if client == 0:
            proceed = False
        elif client <= 1:
            client = clients[client]
            clientFileName = trimmer.clientFileNamer(client)
            trimmer.trimMethod(clientKey[client]['trim'], clientFileName[0])
            plain = emailMessage()
            emailClient(mailer, userName, client, clientFileName, plain)
        else:
            print("Please enter 1 or 2.")
            print("Or press Ctrl-Z or 0, then Enter to exit.")
