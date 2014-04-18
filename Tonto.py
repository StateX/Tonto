#Esto es un invento un poco loco.
#Esto es solo la base 
import os
import sys 
import time
version = "0.0.0.1"
def trabajo(seleccion):	
	print "Accediendo a banco de trabajo"
	os.system('"C:\Program Files\LibreOffice 4\program\soffice.exe"')
	print "Necesitas algo mas? "
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que le vaya bien el dia señor"
		time.sleep(3)	
		sys.exit(0)

def who(Snifer):
	print "Soy tu asistente personal para este pc, me has programado tu y actualmente me encuentro en la " + version
	print "Algo mas señor? "
	print "[s = si] [n = no]"
	d2 =  raw_input("-->:")
	if d2 == "s":
		os.system('cls')
	elif d2 == "n":
		os.system('cls')
		print "que le vaya bien el dia señor"
		time.sleep(3)
		sys.exit(0)
		#me gustaria que tambien cerrara la consola xD
#Saludo, molaria personalizarle el nombre a la maquina

print "Hola Albert, que te apeteceria hacer hoy?"

#Antes de esto me podria dar la tempertura de mi region. Tendre que mirarlo
#estoy ira así facil y comodo xD
while True:
	 print"""
[a = Me apetece, trabajar] 
[b= bah, tendre que estudiar]
[c = Musica, Animame el dia] 
[d = Jugar] 
[e = Quien eres?] 
[f = No requiero tu ayuda, gracias]	

"""
	 d1 = raw_input("--> : ")
	 if d1 == "a":
		 print trabajo(d1)
	 elif d1 == "e":
		 print who(d1)	
	 else: 
		 print "estamos trabajando en ello escoje otra opcion"	

