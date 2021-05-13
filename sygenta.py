from PIL import Image


image = Image.open("Syngenta.bmp","r")

pix_val = list(image.getdata())

print("Numero de Pixels Verdes =",pix_val.count(51))


        
        
        

