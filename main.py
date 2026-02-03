import keyboard
import pyautogui as py
import time
import json
import random
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()


# Abre e fecha o arquivo de nomes
arquivo = open("nomes.json", "r")
dados = json.load(arquivo)

nome1 = random.choice(dados)
nome2 = nome1['nome']

nome3 = random.choice(dados)
nome4 = nome3['nome']

# Faz literalmente a mesma coisa do de cima só que com o email

arquivo2 = open("email.json", "r")
dados2 = json.load(arquivo2)

email1 = random.choice(dados2)
email2 = email1['email']

link_do_negocio = "LINK_DO_SITE"

amongus = simpledialog.askinteger("Quantidade de loops", "Quantas vezes você quer que repita?")



for i in range(amongus):
    keyboard.press_and_release("ctrl+shift+p")
    time.sleep(0.5)
    keyboard.write(link_do_negocio)
    keyboard.press("enter")
    time.sleep(6)
    py.click(x = 1421, y = 464)
    time.sleep(0.4)
    keyboard.write(nome2)
    time.sleep(0.4)
    py.click(x = 1461, y = 542)
    time.sleep(0.4)
    keyboard.write(nome4)
    time.sleep(0.4)
    py.click(x = 1484, y = 615)
    time.sleep(0.4)
    keyboard.write(email2)
    time.sleep(0.4)
    py.click(x = 1279, y = 874)
    time.sleep(0.5)
    py.click(x = 1374, y = 831)
    time.sleep(0.2)
    py.scroll(-200)
    time.sleep(0.3)
    py.click(x = 1461, y = 932)
    time.sleep(3)
    py.scroll(-200)
    time.sleep(0.5)
    py.click(x = 973, y = 964)



    
