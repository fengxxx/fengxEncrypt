#!/usr/bin/python
# -*- coding: cp936 -*-
import sys      
import os
import struct
fengxMark="fengxEncrypt\n"
key=[1,2,1,2,1,2,1,2,1,2,1,2,1,2]  



def encrypt(s,key):
    eStr=s[::-1]
    for c in s:
        d=struct.unpack("s",c)
        print d
        #for cc in d:
        #print struct.unpack("i",d)
    #eStr=s.encode('utf8')
    #eStr=s.encode('ISO-8859-1')
    print eStr

    return eStr

def decrypt(s,key):
    eStr=s[::-1]
    #eStr=s.replace(key, [count]) 
    return eStr

def enFile(filePath,targetPath,key):
    fileC=open(filePath,"rb")
    fileT=open(targetPath,"wb")
    line = fileC.readline()
    fileT.write(fengxMark)
    while line:
        fileT.write(encrypt(line,key))
        line = fileC.readline()
    fileC.close()
    fileT.close()
    
def deFile(filePath,targetPath,key):
    fileC=open(filePath,"rb")
    fileT=open(targetPath,"wb")
    line = fileC.readline()
    line = fileC.readline()
    while line:
        fileT.write(decrypt(line,key))
        line = fileC.readline()
    fileC.close()
    fileT.close()
    
def isEncry(filePath):
    state=False
    fileC=open(filePath,"rb")
    line = fileC.readline()  
    if line==fengxMark:
       state=True
    fileC.close()
    return state
    
    
def fengxEorD(filePath,key):
    tS=os.path.split(filePath)
    print isEncry(filePath)
    if isEncry(filePath)==True: 
        print "true"
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_decrypt" + os.path.splitext(tS[1])[1]
        deFile(filePath,fileOutPath,key)
        print ("�����ļ�-->>"+filePath)
        print ("����ļ�-->>"+fileOutPath)
    else:
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_encrypt" + os.path.splitext(tS[1])[1]
        enFile(filePath,fileOutPath,key)
        print ("�����ļ�-->>"+filePath)
        print ("����ļ�-->>"+fileOutPath)


try:
    sys.argv[1]
except:
    print "û����ק��"
else:
    fengxEorD(sys.argv[1],"s")


test="E:\\GitHub\\fengxEncrypt\\bghm.prefab"
fengxEorD(test,"s")
 
raw_input()
