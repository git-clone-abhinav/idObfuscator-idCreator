from os import path 
import hashlib
import time

def sha1calc():
    #id=os.popen("vcgencmd otp_dump | grep '28:'").read()
    #id=id.strip()
    id="20:shdyandf"
    salt = "RKh?^rLYSBf#nD-2tGzjx^zXy+q#Ph=^kb^r6&A_9NAhdh7r7k%H!d%-k%5D@C5-ysn=dd-rwKMR6#y_yR@Ds^#4-Wc-hy3&aKT&"
    saltedid = id[2:] + salt + id[:2]
    temp = bytes(saltedid, 'utf-8') 
    a = hashlib.sha1(temp)
    hex_dig = a.hexdigest()
    return hex_dig

while True:
    if(str(path.exists("d:\password.txt")) == "True"):
        with open('d:\password.txt') as f :
            first_line = f.readline()
        a = first_line
        b = sha1calc()

        if a == b != "":
            print("Access Granted.")
            break
        else:
            print("Licence Violation")
            time.sleep(10000)
    else:
        print("Licence Violation")
        time.sleep(10000)
