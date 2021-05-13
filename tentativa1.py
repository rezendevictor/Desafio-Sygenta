from PIL import Image
from PIL import ImageOps
from bitmap import BitMap
import pytesseract
from scipy import misc
import numpy as np



def divide_chunks(l, n):
    
    for i in range(0, len(l), n): 
        yield l[i:i + n]

image = Image.open("Syngenta.bmp","r")

pix_val = list(image.getdata())
p = np.array(image)


x = list(divide_chunks(pix_val, 8))

value = 0

final_list = []

for line,chunk in enumerate(x):
    for column,item in enumerate(chunk):
        if x[line][column] == 51:
            x[line][column] = 1
        if x[line][column] == 255:
            x[line][column] = 0
            
    final_list.append(chunk)
        

r = ''        

stringList = []

for chunk in final_list:
    for item in chunk:
        r+= str(item)

    stringList.append(r)
    r = ''
    
palvra =''

for value in stringList:
    int_value = int(value, base=2)
    if(int_value > 0):
        palvra += (chr(33+(int_value)))

print(palvra)

value = 0
outrapalavra = ''
for item in pix_val:
    if item == 51:
        ##print(32+(value%127))
        outrapalavra += (chr(32+(value%127)))
        value = 0
    else:
        value +=1

print(outrapalavra)  




        
