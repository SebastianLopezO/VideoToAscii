from PIL import Image
import ascii_magic

name=input("Ingrese el nombre base del archivo: ")
formate=input("Ingrese el formato de sus imagenes: ")
num=int(input("Ingrese la cantidad de imagenes que tiene: "))
for i in range(1,num+1):
	my_art = ascii_magic.from_image_file(name+"/"+name+" ("+str(i)+")."+formate)
	ascii_magic.to_terminal(my_art)
	print("break")