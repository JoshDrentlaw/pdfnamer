#
# For pdfnamer to run, you need a file named key.py
# This file will show you how to set up your key.py file
#

#
# Trim methods
#
# deleteFront: deletes pages from the front of a document. Useful for removing a cover page or pick ticket from paperwork being sent.
#
# keepBack: only keep a number of pages starting from the back of the document. This option is a little more specialized and might not be as useful to everyone.
#

emailKey = [
    "smtp.office365.com",           # this should be the domain you're connecting to
    "ccdperson@domain.com",         # add the address of anyone that should be cc'd to the client that lines up with this index in the clientKey
    "ccdperson@domain.com, secondperson@domain.com, thirdperson@domain.com"   # if there are multiple people that should be cc'd, add them to the same index
]

clientKey = {
    "empty": "",                                                        # this entry should be left empty
    "Google": {"client": "google@gmail.com", "trim": "deleteFront"}     # follow this template for each client you'd like to email
}