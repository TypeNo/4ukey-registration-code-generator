# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import csv
import numpy

#VIDEO_SOURCE=0

#cap = cv2.VideoCapture(VIDEO_SOURCE)
#suc,image = cap.read()

#cv2.imwrite("frame0.jpg", image)
#img=cv2.imread("frame0.jpg")
#img=cv2.imread("1_ysr7_sbJAJCWWDfyc9jeiQ - Copy.png")
url="http://192.168.1.3:8080/video"
cap=cv2.VideoCapture(url)
while(True):
  
  suc,img=cap.read()
  if img is not None:
      
      cv2.imwrite("frame0.jpg",img)
      image=cv2.imread("frame0.jpg")
      r=cv2.selectROIs('ROI Selector',image,showCrosshair = False,fromCenter = False)
      rlist=list(r)

      print(rlist)
      with open('data/rois.csv', 'w', newline='') as outf:
        csvw = csv.writer(outf)
        csvw.writerows(rlist)
        q=cv2.waitKey(1)
        
        break



cap.release()
cv2.destroyAllWindows()