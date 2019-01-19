import os
import smtplib
import zipfile
import re

MY_ADDRESS = 'my_email_address'
PASSWORD = 'my_password'
HOST = 'HOST'
PORT = '587'
DESCRIPTION ='None'
SIZE = 100000


def compressFile(path,size):
    output_zip = zipfile.ZipFile('D:\\archive.zip', 'w')
    description = 'Description of archive code\n'
    if(os.path.exists(path)):
        for folder, subfolders, files in os.walk(path):

            for file in files:
                fsize = os.stat(os.path.join(folder,file)).st_size
                if(fsize < size):
                    description += f'{file} has file size of {fsize}  which is below requirement\n'
                elif (file.endswith('.jpg') or file.endswith('.zip')):
                    description += f'{file} is already compressed\n'
                    print()
                else:
                    description +=f'{fsize} and {file} meets requirement\n'
                    output_zip.write(os.path.join(folder, file),
                                      os.path.relpath(os.path.join(folder, file), 'D:\\images'),
                                      compress_type=zipfile.ZIP_DEFLATED)

        return True, description
    else:
        return False, 'no folders in the path'



def send_email(recipient):

    pattern = "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$"
    if re.match(pattern,recipient)!=None :

        FROM = MY_ADDRESS
        TO = recipient
        SUBJECT = 'description of the code'
        TEXT = DESCRIPTION

        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, "".join(TO), SUBJECT, TEXT)

        # print(message)
        try:
            server = smtplib.SMTP(HOST,PORT)
            server.ehlo()
            server.starttls()
            server.login(MY_ADDRESS,PASSWORD)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")
    else:
        print('please enter correct email address')


flag, des = compressFile('D:\\images', SIZE)

if(flag):
    DESCRIPTION = des
    send_email('abcd@cd.com')
else:
    DESCRIPTION= None
    print(des)