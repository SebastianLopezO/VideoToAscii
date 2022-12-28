import cv2
import os

name=input("Ingrese el nombre del video: ")
format=input("Ingrese el formato del video: ")

capture = cv2.VideoCapture("videos/"+name+"."+format)
cont = 0
os.mkdir(name)
path = name+"/"


while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imwrite(path + name+' ('+str(cont+1)+').png',frame)    
        cont += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()