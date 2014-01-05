#!/usr/bin/python
# -*- coding: cp936 -*-
import sys      
import os
def encrypt(s,key):
    eStr=""
    eStr=s
    return eStr

def decrypt(s,key):
    dStr=""
    dStr=s
    return dStr

def enFile(filePath,targetPath,key):
    fileC=open(filePath,"rb")
    fileT=open(targetPath,"wb")
    line = fileC.readline()             
    while line:
        fileT.write(encrypt(line,key))
        line = fileC.readline()
    fileC.close()
    fileT.close()
    
def deFile(filePath,targetPath,key):
    fileC=open(filePath,"rb")
    fileT=open(targetPath,"wb")
    line = fileC.readline()             
    while line:
        fileT.write(decrypt(line,key))
        line = fileC.readline()
    fileC.close()
    fileT.close()

    
def main():
    filePath=sys.argv[1]
    tS=os.path.split(filePath)
    fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_fengx" + os.path.splitext(tS[1])[1]
    enFile(filePath,fileOutPath,"s")
    print ("加密文件-->>"+filePath)
    print ("输出文件-->>"+filePath)
main()
#os.path.exists
raw_input()
