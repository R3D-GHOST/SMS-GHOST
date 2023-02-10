#/bin/python/
#Librerias
import os
import time
import subprocess


#Colores
RED = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
WHITE = "\033[1;37m"
#banner
banner = """
 ____  __  __ ____     ____ _   _  ___  ____ _____ 
/ ___||  \/  / ___|   / ___| | | |/ _ \/ ___|_   _|
\___ \| |\/| \___ \  | |  _| |_| | | | \___ \ | |  
 ___) | |  | |___) | | |_| |  _  | |_| |___) || |  
|____/|_|  |_|____/   \____|_| |_|\___/|____/ |_|  
                                                   

"""
os.system('clear')
print(WHITE+banner)
print(GREEN+"1 --> SMS GHOST")
print(RED+"2 --> Exit")
menu_opt = input(">>>> ")
if menu_opt == "1":
    os.system('clear')
    time.sleep(1)
    print(banner)
    print("1 --> Redes Sociales")
    print("2 --> Whatsapp")
    print("3 --> Phone SMS")
    opt_sms = input(">>>> ")
    if opt_sms == "1":
        web = subprocess.getoutput('firefox https://www.instagram.com/accounts/password/reset/')
        web = subprocess.getoutput('firefox https://web.telegram.org/k/')
        web = subprocess.getoutput('firefox https://es-es.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
    elif opt_sms == "2":
        os.system('clear')
        time.sleep(1)
        os.system('cd tools/SpamWa/ ; python3 spam.py ')
    elif opt_sms == "3":
         os.system('clear')
         time.sleep(1)
         print("Inserta el numero de Telefono de la victima")
         print("Ejemplo +346731XXXX")
         numero = input(">>>> ")
         os.system('cd tools/Impulse/ ; python3 impulse.py --method SMS --time 20 --threads 15 --target +str{numero}') 
else:
    print("Invalid Error")
        