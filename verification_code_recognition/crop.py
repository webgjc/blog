from PIL import Image
import os
d=os.listdir("dealyzm/")
k=0
for i in d:
    file=Image.open("dealyzm/"+i)
    for j in range(5):
        crop=file.crop((9*j+5,4,9*j+14,18))
        crop.save("crop/"+i[j]+str(k)+".png")
    k+=1
    '''crop=file.crop((5,4,50,18))
    crop1=file.crop((5,4,14,18))
    crop2=file.crop((14,4,23,18))
    crop3=file.crop((23,4,32,18))
    crop4=file.crop((32,4,41,18))
    crop5=file.crop((41,4,50,18))
    crop1.save("crop/"+i[0]+str(j)+".png")
    crop2.save("crop/"+i[1]+str(j)+".png")
    crop3.save("crop/"+i[2]+str(j)+".png")
    crop4.save("crop/"+i[3]+str(j)+".png")
    crop5.save("crop/"+i[4]+str(j)+".png")'''
    j+=1