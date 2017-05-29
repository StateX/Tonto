#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Esto es un invento un poco loco.
#En esta version vamos a ordenar un poco el codigo de Tonto.


import os
import sys
import time
from datetime import date
import re
import pyttsx

version = "0.0.1.4"
ideas = []

#Ordenamos todas las frases que reproducira Tonto en una sola deficion
def voz(frase):
 engine = pyttsx.init()
 voices = engine.getProperty('voices')
 engine.setProperty('voice', 'spanish')
 engine.say(frase)
 engine.runAndWait()

def frases(numero):
 if numero == "1":
 linea =  "Aun no lo ha programado."
 elif numero == "2":
 linea =  "Accediendo a banco de trabajo"
 elif numero == "3":
 linea =  "Necesitas algo mas? "
 elif numero == "4":
 linea =  "[s = si] [n = no]"
 elif numero == "5":
 linea =  "que le vaya bien el dia"
 elif numero == "6":
 linea =  "Se que no le gusta pero hoy ha de aguantarse"
 elif numero == "7":
 linea =  "Abriendo carpeta de documentos, espero que usted sea ordenado "
 elif numero == "8":
 linea =  "Accediendo a su carpeta de Musica"
 elif numero == "9":
 linea =  "Abriendo repositorios"
 elif numero == "10":
 linea =  "Accediendo a su editor de codigo favorito"
 elif numero == "11":
 linea =  "estas son las ideas que ha recogido hasta ahora."
 elif numero == "12":
 linea =  "ideas guardadas con exito"
 elif numero == "13":
 linea =  "Algo mas ? "
 elif numero == "14":
 linea =  "selecione una de las dos "
 elif numero == "15":
 linea =  "Iniciando Ragnarock Online, ya que tiene los juegos desordenados por el disco duro."
 elif numero == "16":
 linea = "Soy tu asistente personal para este pc, me has programado tu y actualmente me encuentro en la version 0.0.1.4."
 elif numero == "16bis":
 linea = "Ademas ahora no tienes tiempo de hacerme crecer y no se que haces haceindo videos de estos.Bueno pero has tenido una buena idea"
 elif numero == "16bis2":
 linea = "abriendo el foro tonto.foroactivo.com para que la gente pueda mejorarme."
 elif numero == "17":
 linea =  "Siempre es un placer poder descansar"
 elif numero == "18":
 linea =  "Hola Albert, que te apeteceria hacer hoy?"
 elif numero == "19":
 linea = """
[trabajar]
[bah, tendre que estudiar]
[Musica, Animame el dia]
[programar]
[ideas]
[Jugar]
[Quien eres?]
[No requiero tu ayuda, gracias]
"""
 print(linea)
 voz(linea)

#Lo mismo que hacemos con las frases pero con la voz reproducida
#def voz(diba):
 #if diba = "numerodiba":
 #os.system('"RUTA DE LA CANCION A reproducira"')
 #Aparte de os.system() tambien hay soluciones usando diferentes librerias.



#Este es el sitema de Busqueda o peticiones

def sistema(busqueda):
 trabajar = re.search(r'trabaj(.*)',peticion)
 empollar =  re.search(r'estudi(.*)', peticion)
 ritmo = re.search(r'musi(.*)',peticion)
 codigo =  re.search(r'programa(.*)', peticion)
 bideas = re.search(r'idea(.*)',peticion)
 jugar =  re.search(r'jugar', peticion)
 quien = re.search(r'eres',peticion)
 descansar =  re.search(r'descans(.*)', peticion)

 if trabajar:
 print(trabajo(peticion))
 os.system('clear')
 elif empollar:
 print(estudiar(peticion))
 os.system('clear')
 elif ritmo:
 print(musica(peticion))
 os.system('clear')
 elif codigo:
 print(programar(peticion))
 os.system('clear')
 elif bideas:
 print(banco(peticion))
 os.system('clear')
 elif jugar:
   print(games(peticion))
   os.system('clear')
 elif quien:
 print(who(peticion))
 os.system('clear')
 elif descansar:
 print(fin(peticion))
 os.system('clear')  
 else:
 frases("1")
 #Podriamos ordenar que reproduzca el sonido que queramos
 #voz(diba)
 time.sleep(3)
 os.system('clear')

def trabajo(seleccion):
 frases("2")
 #voz(diba)
 time.sleep(3)
 os.system('"RUTA A TU EDITOR DE TEXTO FAVORITO"')
 frases("3")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("5")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def estudiar(Albert):
 frases("6")
 #voz(diba)
 time.sleep(4)
 frases("7")
 #voz(diba)
 time.sleep(4)
 os.system('"start RUTA CARPETA DOCUMENTOS"')
 time.sleep(3)
 frases("3")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("5")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def musica(beethoven):
 frases("8")
 #voz(diba)
 time.sleep(3)
 os.system('"start cAPERTA MUSICA"')
 frases("3")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("5")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def programar(Wozniak):
 frases("9")
 #voz(diba)
 os.system('"start CAPERTA REPOSITORIOS"')
 time.sleep(3)
 frases("10")
 #voz(diba)
 os.system('"RUTA EDITOR DE CODIGO"')
 time.sleep(3)
 frases("3")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("5")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def banco(delacalle):
 while True:
 recogedor = open('banco_ideas.txt','a+')
 for item in recogedor:
 ideas.append(item)
 frases("11")
 #voz(diba)
 time.sleep(3)
 print(ideas)
 #voz(diba)
 idea = input("Que se le ha ocurrido?:  ")
 ideas.append(idea)
 ideas.append(date.today())
 print(ideas)
 time.sleep(3)
 #voz(diba)
 d3 = input("Ajunto otra idea señor?: ")
 if d3 == "s":
 os.system('clear')
 print(idea)
 elif d3 == "n":
 i = str(ideas)
 banco_ideas = open('banco_ideas.txt','a+')
 print(ideas)
 banco_ideas.write(i)
 banco_ideas.close()
 #voz(diba)
 frases("12")
 time.sleep(3)
 frases("13")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("5")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)
 else:
 frases("14")
 #voz(diba)
 time.sleep(5)

def games(juegos):
 frases("15")
 #voz(diba)
 time.sleep(5)
 os.system('"RUTA A JUEGO O CAPERTA DE JUEGOS"')
 time.sleep(3)
 frases("13")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("14")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def who(Snifer):
 frases("16")
 #voz(diba)
 time.sleep(4)
 frases("16bis")
 time.sleep(2)
 frases("16bis2")
 os.system('firefox http://tonto.foroactivo.com')
 time.sleep(6)
 frases("13")
 #voz(diba)
 frases("4")
 d2 =  input("-->:")
 decision1 =  re.search(r's(.*)', d2)
 decision2 = re.search(r'n(.*)', d2)
 if decision1:
 os.system('clear')
 elif decision2:
 os.system('clear')
 frases("14")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

def fin(apagar):
 frases("17")
 #voz(diba)
 time.sleep(3)
 sys.exit(0)

#Saludo, molaria personalizarle el nombre a la maquina

frases("18")
#voz(diba)
time.sleep(3)
print((frases("19")))
#Antes de esto me podria dar la tempertura de mi region. Tendre que mirarlo
#estoy ira así facil y comodo xD

while True:

 peticion = input("")
 print(sistema(peticion))
