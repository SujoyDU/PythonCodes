import os
import datetime
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED, is_zipfile

def helpInfo():
    print('''
        This program compresses those files in a given folder that are bigger than a given size and achive more than 25% compress ratio.\n
        This program takes two parameters.\n
            a. First parameter is a String that is Path of the Folder to compress.
            b. Second paramenter is an Integer that is MinimumSize in Bytes.\n
        This program will compress those files whose file size is bigger than the MinimumSize and attain compress ratio better than 25%.\n
        If No MinimumSize is given this will compress all the files in the folder.
    ''')


def getRatio(path):    
    with tempfile.TemporaryFile() as delFile:
        outputFile = ZipFile(delFile,'w')
        outputFile.write(path,'testfile',compress_type=ZIP_DEFLATED)
        outputFile.close()

        with ZipFile(delFile, 'r') as archive: 
            for info in archive.infolist(): 
                    ratio = (info.compress_size/info.file_size)*100
        
    compressRatio = 100 - ratio
    print(compressRatio)
    return compressRatio
        



def compressedFile(path,size=0):
    try:     
        description = 'Description of archive code\n'
        outputFileName = 'archive.zip'
        outputZip = ZipFile(outputFileName, 'w')
        if(os.path.exists(path)):       
            for folder,subfolders, files in os.walk(path):
                for fileName in files:
                    fsize = os.stat(os.path.join(folder,fileName)).st_size
                    if(fsize < size):
                        description += f'{fileName} has file size of {fsize} Bytes which is less than minimum size {size} Bytes\n'
                    elif is_zipfile(os.path.join(folder,fileName)):
                        description += f'{fileName} is already an achived file\n'        
                    else:
                        description +=f'{fileName} has file size of {fsize} Bytes which is greater than minimum size {size} Bytes\n'
                        ratio = getRatio(os.path.join(folder,fileName))

                        if(ratio > 25):
                            zippedFilePath = os.path.join(folder, fileName)
                            zippedFileName = fileName

                            outputZip.write(zippedFilePath,zippedFileName, compress_type=ZIP_DEFLATED)      
                        else:
                            description += f'{fileName} would achive {ratio:.2f}% compress ratio. Which is not beneficial\n'                                                  
        else:
            description += 'Path is invalid\n'
    
    finally:
        outputZip.close()
        if(os.path.exists(outputFileName)):
            with ZipFile(outputFileName, 'r') as zip: 
                for info in zip.infolist(): 
                        description += info.filename + '\n' \
                                       + ('\tModified:\t' + str(datetime.datetime(*info.date_time))) + '\n' \
                                       + ('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') + '\n' \
                                       + ('\tZIP version:\t' + str(info.create_version)) + '\n' \
                                       + ('\tCompressed:\t' + str(info.compress_size) + ' bytes') + '\n' \
                                       + ('\tUncompressed:\t' + str(info.file_size) + ' bytes') + '\n'               
        print(description)       
                                                



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

# helpInfo()
# compressedFile('C:\FolderToUse', 100000)
