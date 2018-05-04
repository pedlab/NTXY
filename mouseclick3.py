# -*- coding: utf-8 -*-
"""
Created on Fri May 04 10:12:36 2018

@author: alquine
"""


import cv2
import numpy as np

FPS = 8


def col(i):
    C = [(0,0,255),(64,0,64),
     (122,122,122),(255,64,0),(191,64,255),
     (65,255,64),(255,191,64),(64,64,64)
     ]
    return C[i%len(C)]


# file open dialog
import Tkinter, tkFileDialog, tkMessageBox
def openf():    
    Tkinter.Tk().withdraw()
    path = tkFileDialog.askopenfilename()
    fname = path.split('/').pop().encode('ascii','ignore').split('.')[0]
    return fname

# read video to np array A
def v2np(fname):    
    cap = cv2.VideoCapture(fname+'.avi')
    fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    fh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fpsx = int(round(fps/FPS))
    A = np.empty((fc/fpsx+1, fh, fw, 3), np.dtype('uint8'))    
    i,j = 0,0
    ret = True
    print 'reading ' + fname
    while (ret and i < fc):
        if i%fpsx==0:
            ret, A[j] = cap.read()
            j=j+1
        i = i+ 1
    cap.release()
    print str(j)+' frames (out of '+str(fc)+' @ '+str(fps)+') read.'
    return A

# read the existing NTXY records
def f2l(fname):
    lst = []
    try:    
        with open(fname+'.dat','r') as file:
            for line in file:
                row = [int(c) for c in line.split(' ')]
                lst.append(row)
    except IOError:
        print 'No data file found'
    return lst    

# overwrite the NTXY records    
def l2f(lst,fname):
    with open(fname+'.dat','w') as file:
        for row in lst:
            if len(row)<5:
                file.write(' '.join(map(str, row))+"\n")


# openfile dialog, read frames, read NTXY
def getFR():
    fname = openf()
    if fname:
        return v2np(fname), f2l(fname), fname
    print 'File Open cancelled?'
    return [], [], None

# draw path, draw stat, show
def showIm(f,img,R,N,T):
    # path
    path = [row for row in R if row[1]<=T and row[1]>=T-10]
    for n,t,x,y in path:
        cv2.circle(img, (x,y),2,col(n), -1)
    # stats
    currClicked = [n for (n,t,x,y) in path if t==T]
    currCarClicked = [n for n in currClicked if n==N]
    h,w = img.shape[:2]
    c = col(N)
    s = .4    
    frame = '[f:'+str(T)+','+str(len(currClicked))+']'
    count = '[c:'+str(N)+','+str(len(currCarClicked))+']'
    cv2.putText(img,frame,(5,h-5),cv2.FONT_HERSHEY_SIMPLEX,s,c)
    cv2.putText(img,count,(60,h-5),cv2.FONT_HERSHEY_SIMPLEX,s,c)
    # show
    cv2.imshow(f,img)
    
# command - eval
def loop(f,F,R,i,n):
    key = cv2.waitKey(0)
    # inc/dec car number
    if key == ord('+'):
        n=n+1
    elif key == ord('-'):
        n=n-1
    # delete most recent coord (pop stack)
    elif key == ord('d'):
        R.pop()
        print 'removed recent item'
    # overwrite data to file
    elif key == ord('s'):
        l2f(R,f)       
    # navigate frame: next/back commands 
    elif key == ord('l'):
        i=i+1
        if i>=len(F):
            i=0
    elif key == ord('r'):
        i=i-1
        if i<0:
            i=len(F)-1
    elif key == ord(' '):
        n,i,x,y =  R[-1]
    elif key == ord('q') or key == 27:
        if (tkMessageBox.askquestion("Closing window", "You want to save the coordinates first?", icon='warning') == 'yes'):
            l2f(R,f)
    return f,i,n,key
            
# driver program
def main():
    i,n=0,0
    F,R,f = getFR()
    if len(F)<=0:
        return
    # mouse call back
    def onMseClk(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            R.append([n,i,x,y])
            showIm(f,np.copy(F[i]),R,n,i)

    showIm(f,np.copy(F[0]),R,n,i)
    cv2.setMouseCallback(f, onMseClk)
   
    q,key = 0,0
    while key != ord('q'):
        f,i,n,key = loop(f,F,R,i,n)
        showIm(f,np.copy(F[i]),R,n,i)        
        q=q+1
        print '['+str(q)+']:'+str(key)+ ' pressed'
    cv2.destroyAllWindows()
    