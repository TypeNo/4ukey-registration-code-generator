import cv2
import numpy as np
import csv
import os
import statistics

z='data/z.csv'
y='data/y.csv'
with open('data/rois.csv','r',newline='')as inf:
    csvr=csv.reader(inf)
    rlist=list(csvr)
rlist=[[int(float(j)) for j in i]for i in rlist]
for i in range(len(rlist)):
    img = np.zeros([max(i[3] for i in rlist)+max(i[1] for i in rlist)+100,max(i[2] for i in rlist)+max(i[0] for i in rlist)+100,4],dtype=np.uint8)

    img[:]=239,206,139,255
entrance=cv2.rectangle(img,(0,0),(20,20),(255,0,0),1)

zx=os.path.isfile("data/z.csv")
if(zx==True):
    with open('data/z.csv','r',newline='')as inf:
        csvr=csv.reader(inf)
        zlist=list(csvr)

zlist=[[int(float(j)) for j in i]for i in zlist]
for i in range(len(zlist)):
    cv2.rectangle(img,(zlist[i][0],zlist[i][1]),(zlist[i][2],zlist[i][3]),(0,255,0),-1)
    
    y=min(i[1] for i in zlist)
    if(y<min(i[3] for i in zlist)):
        x=min(i[0] for i in zlist if i[1]<min(i[3] for i in zlist))
        z=min(i[2] for i in zlist if i[1]<min(i[3] for i in zlist))
    else:
        x=min(i[0] for i in zlist if i[1]>min(i[3] for i in zlist))
        z=min(i[2] for i in zlist if i[1]<min(i[3] for i in zlist))
    q=[x,z]
    r=statistics.mean(q)
    #r=[min(i[1] for i in zlist),min(i[3]for i in zlist)]
    if(y<min(i[3] for i in zlist)):
        
        cv2.line(img,(10,20),(10,y-50),(255,255,255),1)
        cv2.line(img,(10,y-50),(int(r),y-50),(255,255,255),1)
        cv2.line(img,(int(r),y-50),(int(r),y),(255,255,255),1)
    else:
        cv2.line(img,(10,20),(10,y+50),(255,255,255),1)
        cv2.line(img,(10,y+50),(int(r),y+50),(255,255,255),1)
        cv2.line(img,int(r),y+50),(int(r,y),(255,255,255),1)
yx=os.path.isfile("data/y.csv")
if(yx==True):
    with open('data/y.csv','r',newline='')as inf:
        csvr=csv.reader(inf)
        ylist=list(csvr)


ylist=[[int(float(j))for j in i]for i in ylist]
for i in range(len(ylist)):
    cv2.rectangle(img,(ylist[i][0],ylist[i][1]),(ylist[i][2],ylist[i][3]),(0,0,255),-1)
cv2.imshow('paper',img)
cv2.waitKey(0)