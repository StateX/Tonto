#Esto es un invento un poco loco.
#Esto es solo la base 
import os
import sys 
import time
from datetime import date 

version = "0.0.0.1"
ideas = []

def trabajo(seleccion):	
	print "Accediendo a banco de trabajo"
	os.system('"C:\Users\Albert\Downloads\Jorge4.wav"')
	time.sleep(3)
	os.system('"C:\Program Files\LibreOffice 4\program\soffice.exe"')
	print "Necesitas algo mas? "
	os.system('"C:\Users\Albert\Downloads\Jorge7.wav"')
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que le vaya bien el dia señor"
		os.system('"C:\Users\Albert\Downloads\Jorge1.wav"')
		time.sleep(3)	
		sys.exit(0)

def estudiar(Albert): 
	print "Se que no le gusta pero hoy ha de aguantarse"
	os.system('"C:\Users\Albert\Downloads\Jorge10.wav"')
	time.sleep(4)
	print "Abriendo carpeta de documentos, espero que usted sea ordenado señor"
	os.system('"C:\Users\Albert\Downloads\Jorge11.wav"')
	time.sleep(4)
	os.system('"start C:\Users\Albert\Documents"')
	time.sleep(3)
	print "Necesitas algo mas? "
	os.system('"C:\Users\Albert\Downloads\Jorge7.wav"')
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que le vaya bien el dia señor"
		os.system('"C:\Users\Albert\Downloads\Jorge1.wav"')
		time.sleep(3)	
		sys.exit(0)

def musica(beethoven):
	print "Accediendo a su carpeta de Musica"
	os.system('"C:\Users\Albert\Downloads\Jorge6.wav"')
	time.sleep(3)
	os.system('"start C:\Users\Albert\Music"')
	print "Necesitas algo mas? "
	os.system('"C:\Users\Albert\Downloads\Jorge7.wav"')
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que le vaya bien el dia señor"
		os.system('"C:\Users\Albert\Downloads\Jorge1.wav"')
		time.sleep(3)	
		sys.exit(0)

def programar(Wozniak):
	 print "Accediendo a su editor de codigo favorito"
	 os.system('"C:\Users\Albert\Downloads\Jorge13.wav"')
	 os.system('"C:\Program Files\Sublime Text 2\sublime_text.exe"')
	 time.sleep(3)
	 print "Necesitas algo mas? "
	 os.system('"C:\Users\Albert\Downloads\Jorge7.wav"')
	 print "[s = si] [n = no]"
	 d2 =  raw_input("-->:")
	 if d2 == "s":
		 os.system('cls')
	 elif d2 == "n":
		 os.system('cls')
		 print "que le vaya bien el dia señor"
		 os.system('"C:\Users\Albert\Downloads\Jorge1.wav"')
		 time.sleep(3)	
		 sys.exit(0)

def banco(delacalle):
	 while True:
	 	 recogedor = open('banco_ideas.txt','a+')
	 	 for item in recogedor:
	 	 	 ideas.append(item)	 
	 	 print "estas son las ideas que ha recogido hasta ahora."
	 	 os.system('"C:\Users\Albert\Downloads\Jorge14.wav"')
	 	 time.sleep(3)
	 	 print ideas
	 	 os.system('"C:\Users\Albert\Downloads\Jorge15.wav"')
	 	 idea = raw_input("Que se le ha ocurrido?:  ")
	 	 ideas.append(idea)
	 	 ideas.append(date.today())
	 	 print ideas
	 	 time.sleep(3)
	 	 os.system('"C:\Users\Albert\Downloads\Jorge16.wav"')
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
		 	 os.system('"C:\Users\Albert\Downloads\Jorge17.wav"')
		 	 print "ideas guardadas con exito"
			 time.sleep(3)
			 print "Algo mas señor? "
	 	 	 os.system('"C:\Users\Albert\Downloads\Jorge8.wav"')
	 	 	 print "[s = si] [n = no]"
	 	 	 d2 =  raw_input("-->:")
	 	 	 if d2 == "s":
		 	 	 os.system('cls')
		 	 	 break
	 	 	 elif d2 == "n":
		 	 	 os.system('cls')
		 	 	 print "que tenga un buen dia señor"
		 	 	 os.system('"C:\Users\Albert\Downloads\Jorge2.wav"')
		 	 	 time.sleep(3)
		 	 	 sys.exit(0)
	 	 else: 
	 	 	 print "selecione una de las 2 señor"
	 	 	 os.system('"C:\Users\Albert\Downloads\Jorge18.wav"')
	 	 	 time.sleep(5)

def games(juegos):
	 print "Iniciando Ragnarock Online, ya que tiene los juegos desordenados por el disco duro."
	 os.system('"C:\Users\Albert\Downloads\Jorge12.wav"')
	 time.sleep(5)
	 os.system('"C:\Users\Albert\Downloads\RagnarokOnline\RagnarokOnline\XatiyaRO.exe"')
	 time.sleep(3)
	 print "Algo mas señor? "
	 os.system('"C:\Users\Albert\Downloads\Jorge8.wav"')
	 print "[s = si] [n = no]"
	 d2 =  raw_input("-->:")
	 if d2 == "s":
		os.system('cls')
	 elif d2 == "n":
		os.system('cls')
		print "que tenga un buen dia señor"
		os.system('"C:\Users\Albert\Downloads\Jorge2.wav"')
		time.sleep(3)
		sys.exit(0)

def who(Snifer):
	print "Soy tu asistente personal para este pc, me has programado tu y actualmente me encuentro en la " + version
	os.system('"C:\Users\Albert\Downloads\Jorge5.wav"')
	time.sleep(7)
	print "Algo mas señor? "
	os.system('"C:\Users\Albert\Downloads\Jorge8.wav"')
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que tenga un buen dia señor"
		os.system('"C:\Users\Albert\Downloads\Jorge2.wav"')
		time.sleep(3)
		sys.exit(0)

def fin(apagar): 
	 print "Siempre es un placer poder descansar"
	 os.system('"C:\Users\Albert\Downloads\Jorge3.wav"')
	 time.sleep(3)
	 sys.exit(0)		
#Saludo, molaria personalizarle el nombre a la maquina

print "Hola Albert, que te apeteceria hacer hoy?" 
os.system('"C:\Users\Albert\Downloads\Jorge.wav"')
time.sleep(3)

#Antes de esto me podria dar la tempertura de mi region. Tendre que mirarlo
#estoy ira así facil y comodo xD

while True:
	 print"""
[a = Me apetece, trabajar] 
[b = bah, tendre que estudiar]
[c = Musica, Animame el dia] 
[p = programar]
[i = ideas]
[d = Jugar] 
[e = Quien eres?] 
[f = No requiero tu ayuda, gracias]	

"""
	 d1 = raw_input("--> : ")
	 if d1 == "a":
		 print trabajo(d1)
	 elif d1 =="b": 
	 	 print estudiar(d1)	 
	 elif d1 == "c": 
	 	 print musica(d1)	
	 elif d1 == "p": 
	 	 print programar(d1)
	 elif d1 == "i": 
	 	 print banco(d1)	 	 
	 elif d1 == "d":
	 	 print games(d1)	  
	 elif d1 == "e":
		 print who(d1)
	 elif d1 == "f":
	 	 print fin(d1)	
	 else: 
		 print "Aun no lo ha programado, señor"
		 os.system('"C:\Users\Albert\Downloads\Jorge9.wav"')
		 time.sleep(3)

