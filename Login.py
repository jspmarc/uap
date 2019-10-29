#   Program: Login

import MenuGame
import pickle
import os

def save_obj(obj, name): #Menyimpan dictionary ke file luar
    f = open(name, 'wb')
    pickle.dump(obj,f)
    f.close()

def load_obj(name): #Me-load dictionary dari file luar
    with open(name, 'rb') as f:
        return pickle.load(f)

def main():
    DictUsers = load_obj('UsernamesDictionaries.txt') #Mengambil dictonary yang dari file luar bernama UsernamesDicitonaries
    while True:
        LoginRegister = int(input("1. Login\n2. Register or change your old password\n3. Quit\nChoose a menu: ")) #User memilih untuk login atau register
        os.system("clear")
        #os.system("cls")
        if(LoginRegister == 1):
            username = input("Username: ") #Menerima input username
            password = input("Password: ") #Menerima input password
            try:
                if (password == DictUsers[username]): #Bila password benar
                    os.system("clear")
                    #os.system("cls")
                    MenuGame.main()
                    break
                else:
                    os.system("clear")
                    #os.system("cls")
                    print("The username or password is wrong.") #Apabila password salah, user akan terlempar lagi ke LoginRegister (Line 13)
            except KeyError: #Akan ke sini apa bila username tidak ada di dictionary, user akan terlempar lagi ke LoginRegister (Line 13)
                os.system("clear")
                print("The username or password is wrong.") 
                #os.system("cls")
        elif (LoginRegister == 2):
            username = input("New or old username: ")
            while True:
                password = input("New password: ")
                confirmPassword = input("Confirm new password: ")
                if (password == confirmPassword):
                    DictUsers[username] = password #Mengupdate dictionary
                    save_obj(DictUsers, 'UsernamesDictionaries.txt') #Menyimpan dictionary ke file luar
                    os.system("clear")
                    # os.system("cls")
                    break
                else:
                    os.system("clear")
                    print("Password confirmation is wrong.")
                    #os.system("cls")
        elif (LoginRegister == 3):
            os.system("clear")
            #os.system("cls")
            print("Goodbye, thank you for using Uap")
            break
        else:
            os.system("clear")
            #os.system("cls")
            print("The menu isn't available.")