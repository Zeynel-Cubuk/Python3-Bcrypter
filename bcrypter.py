import bcrypt
import time

class BCrypter(object):
    def __init__(self):
        self.R = '\033[31m'  # kirmizi
        self.G = '\033[1;32m'  # koyu yesil
        self.B = '\033[34m'  # mavi
        self.CYAN = "\033[1;36m"

        print(self.B+"   ___   __  ___  _  __ ___  _____ ___  ___ ")
        print(self.B+"  / o.),'_/ / o || |/,'/ o |/_  _// _/ / o |")
        print(self.B+" / o \/ /_ /  ,' | ,' / _,'  / / / _/ /  ,' ")
        print(self.B+"/___,'|__//_/`_\/_/  /_/    /_/ /___//_/`_\ ")

        print(self.CYAN + "# Author      :" + "KIZILYILDIZ✮")
        print(self.CYAN + "# Instagram   :" + "instagram.com/kiziilyildiz")
        print(self.CYAN + "# GitHub      :" + "github.com/Zeynel-Cubuk")
        print(self.CYAN + "# Title       :" + "bcrypter.py")
        print(self.CYAN + "# Date        :" + "19/1/2021")
        print(self.CYAN + "# Version     :" + "1.1")
        print("#"*43)

    def encoder(self,value):
        # admin -> b'$2a$12$hkAPtUkY3edcDyEkjIQ/u.1.SC9qOWja/pvvbPK.g2UBHgW/6mCEW'
        value = bytes(value.encode('utf-8'))
        # value = bytes(value.encode('utf-8'))
        hash_bc = bcrypt.hashpw(value, salt=bcrypt.gensalt(prefix=b'2a'))
        return hash_bc


    def decoder(self,value, hash_value):
        # value = value.encode('utf-8')
        # True/False
        check_bc = bcrypt.checkpw(value, hash_value)
        if check_bc:
            print( self.G+ '\n[★] Found: ' + str(value.decode('utf-8')) + ':' + str(hash_value.decode('utf-8')))
            time.sleep(1)
            quit()

        else:
            print(self.R+ '\n[✰] Not found: ' + str(value.decode()))
            time.sleep(1)


if __name__ == '__main__':
    bcr = BCrypter()
    print(bcr.B+
"""
1) Bcrypt Encode
2) Bcrypt Decode
""")

    user = input(bcr.R+'[►] Select: ')
    if user == '1':
        value = input(bcr.B+'\n[☙] Password: ')
        time.sleep(2)
        print(bcr.G+"[☣] Bcrypt: ",str(bcr.encoder(value).decode()))

    elif user == '2':
        bc_passwd = input(bcr.B+'\n[►] Bcrypt Passwod: ').encode('utf-8')
        passwdFile = input(bcr.G+'[►] File wordlist: ')

        passwords = open(passwdFile, 'r', encoding='utf-8')

        for value in passwords.readlines():
            value = value.strip('\n')
            value = value.encode('utf-8')
            bcr.decoder(value,bc_passwd)
