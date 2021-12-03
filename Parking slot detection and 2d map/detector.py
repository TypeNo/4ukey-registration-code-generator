from typing import ClassVar
import cv2
import csv
import os

z="data/z.csv"
y="data/y.csv"
zx=os.path.isfile(z)
if(zx==True):
    os.remove(z)

yx=os.path.isfile(y)
if(yx==True):    
    os.remove(y)

def drawRectangle(img,a,b,c,d):
    sub_img= img[b:b+d,a:a+c]

    edges = cv2.Canny(sub_img,lowThreshold,highThreshold)

    pix=cv2.countNonZero(edges)
    slot=[]
    if pix in range(min,max):
        
            cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),3)
            spots.loc +=1
            #zlist=[z1,z2]
            slot=[(a,b,a+c,b+d)]
            #slot.append((slot[0][0],slot[0][1],slot[0][2],slot[0][3]))
            zlist=list(slot)
            print(zlist)
            for i in range(len(zlist)):
                with open('data/z.csv','a',newline='')as outf:
                    csvw = csv.writer(outf)
                    csvw.writerows(zlist)

        
    else:
        y=cv2.rectangle(img,(a,b),(a+c,b+d),(0,0,2550,4))
        #ylist=list(y)
        slot=[(a,b,a+c,b+d)]
        ylist=list(slot)
        print(ylist)
        for i in range(len(ylist)):
            with open('data/y.csv','a',newline='')as outf:
                csvw=csv.writer(outf)
                csvw.writerows(ylist)
        

def callback(foo):
    pass
cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1','parameters',186,700,callback)
cv2.createTrackbar('Threshold2','parameters',122,700,callback)
cv2.createTrackbar('Min pixels','parameters',0,1500,callback)
cv2.createTrackbar('Max pixels','parameters',100,1500,callback)

class spots:
    loc=0

with open('data/rois.csv','r',newline='')as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i]for i in rois]

VIDEO_SOURCE=0

url="http://192.168.1.3:8080/video"
cap=cv2.VideoCapture(url)
while True:
    spots.loc = 0

    ret,frame = cap.read()
    ret2,frame2=cap.read()

    min = cv2.getTrackbarPos('Min pixels','parameters')
    max = cv2.getTrackbarPos('Max pixels','parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1','parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')
    
    for i in range(len(rois)):
        drawRectangle(frame,rois[i][0],rois[i][1],rois[i][2],rois[i][3])

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Available spots:'+str(spots.loc),(10,30),font,1,(0,255,0),3)
    cv2.imshow('detector',frame)

    canny=cv2.Canny(frame2,lowThreshold,highThreshold)
    cv2.imshow('canny',canny)


    if cv2.waitKey(0) & 0xFF ==ord('q'):
        break



#print(ylist)
#with open('data/.csv','w',newline='')as outf:
            #csvw = csv.writer(outf)
            #csvw.writerows(ylist)




cap.release()
cv2.destroyAllWindows()


