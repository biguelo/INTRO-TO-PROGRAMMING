#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     06/01/2016
# Copyright:   (c) Owner 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import webbrowser
import time
import os
import urllib

def main():
    pass

if __name__ == '__main__':
    main()

def find_element(l,v):
    p = l.index(v)
    if p > 0:
        return p
    return -1

##for i in range(3):
##    time.sleep(20)
##    webbrowser.open("https://www.youtube.com/watch?v=i1Jp-V4jalI&index=26&list=RDcHHLHGNpCSA&spfreload=1")

def rename_files():
    file_names = os.listdir(r"C:\Users\Owner\Downloads\photos")

    directory = os.getcwd()
    os.chdir(r"C:\Users\Owner\Downloads\photos")
    for files in file_names:
        os.rename(files,''.join(c for c in files if c not in '0123456789'))

    os.chdir(directory)



##rename_files()

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14159352345",    # Replace with your phone number
    from_="+14158141829") # Replace with your Twilio number
print(message.sid)