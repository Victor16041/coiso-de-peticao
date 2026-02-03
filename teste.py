import keyboard
import pyautogui as py
import time
import json
import random

arquivo = open("nomes.json", "r")
dados = json.load(arquivo)
arquivo.close()

aleatorio = random.choice(dados)
aleatorio2 = aleatorio['nome']

print(aleatorio2)