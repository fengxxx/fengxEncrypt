#!/usr/bin/python
# -*- coding: cp936 -*-
import sys
import os
import struct

import mapCode 
fengxMark="fengxEncrypt\n"

key=[1,2,1,2,1,2,1,2,1,2,1,2,1,2]

#########test
def encryptTest(key, s): 
    b = bytearray(str(s))#.encode("gbk")) 
    n = len(b) # ��� b ���ֽ��� 
    c = bytearray(n*2) 
    j = 0 
    for i in range(0, n): 
        b1 = b[i] 
        b2 = b1 ^ key # b1 = b2^ key 
        c1 = b2 % 16 
        c2 = b2 // 16 # b2 = c2*16 + c1 
        c1 = c1 + 65 
        c2 = c2 + 65 # c1,c2����0~15֮�����,����65�ͱ����A-P ���ַ��ı��� 
        c[j] = c1 
        c[j+1] = c2 
        j = j+2 
    return c.decode("gbk") 
 
def decryptTest(key, s): 
    c = bytearray(str(s))#.encode("gbk")) 
    n = len(c) # ���� b ���ֽ��� 
    if n % 2 != 0 : 
        return "" 
    n = n // 2 
    b = bytearray(n) 
    j = 0 
    for i in range(0, n): 
        c1 = c[j] 
        c2 = c[j+1] 
        j = j+2 
        c1 = c1 - 65 
        c2 = c2 - 65 
        b2 = c2*16 + c1 
        b1 = b2^ key 
        b[i]= b1 
    try: 
        return b.decode("gbk") 
    except: 
        return "failed" 
#########test
def encrypt(s,key):
    eStr=""#s#[::-1]
    for i in range(0,(len(s)-1)):
        #tstr=s[i*4+0]+s[i*4+1]+s[i*4+2]+s[i*4+3]
        #print struct.unpack("f",tstr)
        #print len(s[i])
        #print s.encode('hex')
        print struct.unpack("s",s[i])
        #print int(hex2dec(.upper()))
        #print s[i]
        eStr+=str(struct.unpack("c",s[i]))
    #print s.encode('hex')
    return eStr+"\n"

def decrypt(s,key):
    eStr=""#s#[::-1]
    for i in range(0,(len(s)-1)):
        #tstr=s[i*4+0]+s[i*4+1]+s[i*4+2]+s[i*4+3]
        #print struct.unpack("f",tstr)
        #print len(s[i])
        #print s.encode('hex')
        #print struct.unpack("c",s[i])
        eStr+=struct.pack("c",s[i])
    #print s.encode('hex')
    return eStr

def enFile(filePath,targetPath,key):
    fileC=open(filePath,"rb")
    fileT=open(targetPath,"wb")
    line = fileC.readline()
    fileT.write(fengxMark)
    while line:
        fileT.write(encrypt(line,key))
        #fileT.write(encryptTest(key,line))
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
        #fileT.write(decryptTest(key,line))
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
    #print isEncry(filePath)
    if isEncry(filePath)==True: 
        print ("�����ļ�-->>"+filePath)
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_decrypt" + os.path.splitext(tS[1])[1]
        deFile(filePath,fileOutPath,key)
        print ("����ļ�-->>"+fileOutPath)
    else:
        print ("�����ļ�-->>"+filePath)
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_encrypt" + os.path.splitext(tS[1])[1]
        enFile(filePath,fileOutPath,key)
        print ("����ļ�-->>"+fileOutPath)



try:
    sys.argv[1]
except:
    test="E:\\GitHub\\fengxEncrypt\\1.jpg"
    #test="K:\\fengxEncrypt\\1.jpg"
    #test="K:\\fengxEncrypt\\fengxTest.txt"
    fengxEorD(test,"fengx")
    print "û����ק��"
else:
    fengxEorD(sys.argv[1],150)

raw_input()
