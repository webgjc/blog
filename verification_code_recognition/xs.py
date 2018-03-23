from PIL import Image
import histogram2
import os
f=os.listdir("hduyzm/")
f.remove("Thumbs.db")
l=len(f)
for i in range(l):
    p1=Image.open("hduyzm/"+f[i])
    for j in range(i+1,l):
        p2=Image.open("hduyzm/"+f[j])
        res=histogram2.classfiy_histogram_with_split(p1,p2,size=(60,60),part_size=(6,6))
        print(f[i],f[j])
        if res==1.0:
            print(i)
            os.remove("hduyzm/"+f[i])
            break
'''p1=Image.open("hduyzm/"+"9.png")
p2=Image.open("hduyzm/"+"10.png")
res=histogram2.classfiy_histogram_with_split(p1,p2,size=(60,60),part_size=(6,6))
print(res)'''