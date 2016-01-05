#Esto es un invento un poco loco.
#En esta version vamos a ordenar un poco el codigo de Tonto. 

import os
import sys 
import time
from datetime import date 
import re

version = "0.0.1.3"
ideas = []

#Ordenamos todas las frases que reproducira Tonto en una sola deficion

def frases(numero): 
	if numero == "1": 
		print "Aun no lo ha programado, señor"
	elif numero == "2":
		print "Accediendo a banco de trabajo"
	elif numero == "3":
		print "Necesitas algo mas? "
	elif numero == "4":
		print "[s = si] [n = no]"
	elif numero == "5":
		print "que le vaya bien el dia señor"
	elif numero == "6":
		print "Se que no le gusta pero hoy ha de aguantarse"
	elif numero == "7":
		print "Abriendo carpeta de documentos, espero que usted sea ordenado señor"
	elif numero == "8":
		print "Accediendo a su carpeta de Musica"
	elif numero == "9":
		print "Abriendo repositorios"
	elif numero == "10":
		print "Accediendo a su editor de codigo favorito"
	elif numero == "11":
		print "estas son las ideas que ha recogido hasta ahora."
	elif numero == "12":
		print "ideas guardadas con exito"
	elif numero == "13":
		print "Algo mas señor? "
	elif numero == "14":
		print "selecione una de las dos señor"
	elif numero == "15": 
		print "Iniciando Ragnarock Online, ya que tiene los juegos desordenados por el disco duro."
	elif numero == "16": 
		print "Soy tu asistente personal para este pc, me has programado tu y actualmente me encuentro en la " + version
	elif numero == "17":
		print "Siempre es un placer poder descansar"
	elif numero == "18":
		print "Hola Albert, que te apeteceria hacer hoy?" 
	elif numero == "19":
		print"""
[trabajar] 
[bah, tendre que estudiar]
[Musica, Animame el dia] 
[programar]
[ideas]
[Jugar] 
[Quien eres?] 
[No requiero tu ayuda, gracias]	
"""

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
		 print trabajo(peticion)
		 os.system('cls')
	 elif empollar:
 		 print estudiar(peticion)
 		 os.system('cls')
 	 elif ritmo:
 	 	 print musica(peticion)
 	 	 os.system('cls')
 	 elif codigo: 
 	 	 print programar(peticion)
 	 	 os.system('cls')
 	 elif bideas:
 	 	 print banco(peticion)
 	 	 os.system('cls')
 	 elif jugar: 
 	  	 print games(peticion)
 	  	 os.system('cls')
 	 elif quien: 
 	 	 print who(peticion)
 	 	 os.system('cls')
 	 elif descansar: 
 	 	 print fin(peticion)
 	 	 os.system('cls')	  	 	 	 	 	 
 	 else: 
		 frases("1")
		 #Podriamos ordenar que reproduzca el sonido que queramos
		 #voz(diba)
		 time.sleep(3)
		 os.system('cls')

def trabajo(seleccion):	
	frases("2")
	#voz(diba)
	time.sleep(3)
	os.system('"RUTA A TU EDITOR DE TEXTO FAVORITO"')
	frases("3")
	#voz(diba)
	frases("4")
	d2 =  raw_input("-->:")
	decision1 =  re.search(r's(.*)', d2)
	decision2 = re.search(r'n(.*)', d2)
	if decision1:
		os.system('cls')
	elif decision2:
		os.system('cls')
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
	d2 =  raw_input("-->:")
	decision1 =  re.search(r's(.*)', d2)
	decision2 = re.search(r'n(.*)', d2)
	if decision1:
		os.system('cls')
	elif decision2:
		os.system('cls')
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
	d2 =  raw_input("-->:")
	decision1 =  re.search(r's(.*)', d2)
	decision2 = re.search(r'n(.*)', d2)
	if decision1:
		os.system('cls')
	elif decision2:
		os.system('cls')
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
	 d2 =  raw_input("-->:")
	 decision1 =  re.search(r's(.*)', d2)
	 decision2 = re.search(r'n(.*)', d2)
	 if decision1:
		 os.system('cls')
	 elif decision2:
		 os.system('cls')
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
	 	 print ideas
	 	 #voz(diba)
	 	 idea = raw_input("Que se le ha ocurrido?:  ")
	 	 ideas.append(idea)
	 	 ideas.append(date.today())
	 	 print ideas
	 	 time.sleep(3)
	 	 #voz(diba)
	 	 d3 = raw_input("Ajunto otra idea señor?: ") 
		 if d3 == "s":
		 	 os.system('cls')
	 		 print idea
	 	 elif d3 == "n":
	 	 	 i = str(ideas)
	 	 	 banco_ideas = open('banco_ideas.txt','a+')
	 	 	 print ideas
		 	 banco_ideas.write(i)
		 	 banco_ideas.close()
		 	 #voz(diba)
		 	 frases("12")
			 time.sleep(3)
			 frases("13")
	 	 	 #voz(diba)
	 	 	 frases("4")
	 	 	 d2 =  raw_input("-->:")
	 	 	 decision1 =  re.search(r's(.*)', d2)
		 	 decision2 = re.search(r'n(.*)', d2)
		 	 if decision1:
			 	 os.system('cls')
		 	 elif decision2:
			 	 os.system('cls')
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
	 d2 =  raw_input("-->:")
	 decision1 =  re.search(r's(.*)', d2)
	 decision2 = re.search(r'n(.*)', d2)
	 if decision1:
		 os.system('cls')
	 elif decision2:
		 os.system('cls')
		 frases("14")
		 #voz(diba)
		 time.sleep(3)	
		 sys.exit(0) 

def who(Snifer):
	frases("16")
	#voz(diba)
	time.sleep(7)
	frases("13")
	#voz(diba)
	frases("4")
	d2 =  raw_input("-->:")
	decision1 =  re.search(r's(.*)', d2)
	decision2 = re.search(r'n(.*)', d2)
	if decision1:
		os.system('cls')
	elif decision2:
		os.system('cls')
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

#Antes de esto me podria dar la tempertura de mi region. Tendre que mirarlo
#estoy ira así facil y comodo xD

while True: 
	 frases("19")

	 peticion = raw_input("")
	 print sistema(peticion)
