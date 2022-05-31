from PIL import Image
import math
import os
import operator
from functools import reduce
from collections import Counter
def test2(folder,name):
    #Test the pixel values of pictures in a folder
    img_folder=folder
    f=open(name,'w+')
    list=os.listdir(img_folder)
    list.sort()
    for imagename in list:
        imurl=os.path.join(img_folder,imagename)
        print(imurl)
        im=Image.open(imurl)
        rgb_im=im.convert('RGB')
        for i in range(256):
            for j in range(256):
                r,g,b=rgb_im.getpixel((i,j))
                print(r,g,b,file=f)

if __name__ == '__main__':
    #main()
    #compare('E:\\image for testing\\20210901215651.png','E:\\image for testing\\20210901215907.png')
    #test2('E:\\image for testing',"p.txt")
    #test1('F:/autodrive_data/test.png',"o.txt")
    f = open('o.txt', 'w+')
    im = Image.open('F:/autodrive_data/test.png')
    rgb_im = im.convert('RGB')
    for i in range(256):
        for j in range(256):
            r, g, b = rgb_im.getpixel((i, j))
            print(r, g, b, file=f)
    txt1=open('o.txt','r',encoding='utf-8').read()
    #txt2=open('p.txt','r',encoding='utf-8').read()

    for s in "' ' \n":
        txt1=txt1.replace(s,'')

    count=Counter(txt1)
    print("The frequency of each word is:",count)

    val=count.values()
    print(val)

    sum=0
    for key,value in count.items():
        sum+=value
    print(' total of  pixels %d'%sum)
    pre=0
    for key,value in count.items():
        pre=value/sum
        if(pre>0.9):
            print("the picture is wrong")
            break









