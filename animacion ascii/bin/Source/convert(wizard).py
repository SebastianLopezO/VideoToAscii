import ascii_wizard 
import os

name=input("Ingrese el nombre base del archivo: ")
formate=input("Ingrese el formato de sus imagenes: ")
num=int(input("Ingrese la cantidad de imagenes que tiene: "))
file=open(name+".txt","w")
for i in range(1,num+1):
	img=ascii_wizard.AsciiWizard(name+"/"+name+" ("+str(i)+")."+formate)
	text=img.grayscale(150, 2.2, None, None, True)
	file.write(text)
	file.write("break\n")
	print("break")
file.close()
