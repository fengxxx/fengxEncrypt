#coding=utf-8
#!/usr/bin/python
import sys
import os
import struct
import pyDes 

fengxMark="fengxEncrypt\n"

def enFile(filePath,targetPath,key):
    from time import time
    f = open(filePath, "rb+")
    d = f.read()
    f.close()
    t = time()
    k = pyDes.des(key)

    d = k.encrypt(d, " ")
    f = open(targetPath, "wb+")
    f.write(d)
    f.close()

    print ("encrypt time: %f s" % (time() - t))


    '''
    fengx=pyDes.des(key)
    fileC=open(filePath,"rb+")
    fileT=open(targetPath,"wb+")
    b=fileC.read()
    fileC.close()
    fileT.write(fengx.encrypt(b," "))
    '''
    '''
    line = fileC.readline()
    while line:
        fileT.write(fengx.decrypt(line," "))
        #fileT.write(decryptTest(key,line))
        line = fileC.readline()
    '''
    
    #fileT.close()
    
def deFile(filePath,targetPath,key):
    from time import time

    f = open(filePath, "rb+")
    d = f.read()
    f.close()

    t = time()
    k = pyDes.des(key)

    d = k.decrypt(d, " ")
    f = open(targetPath, "wb+")
    f.write(d)
    f.close()

    print ("decrypt time: %f s" % (time() - t))

    '''
    fengx=pyDes.des(key)
    fileC=open(filePath,"rb+")
    fileT=open(targetPath,"wb+")
    b=fileC.read()
    fileC.close()
    fileT.write(fengx.decrypt(b," "))
    '''
    '''
    line = fileC.readline()
    while line:
        fileT.write(fengx.decrypt(line," "))
        #fileT.write(decryptTest(key,line))
        line = fileC.readline()
    '''
    
    #fileT.close()
    
def isEncry(filePath):
    state=False
    fileC=open(filePath,"rb")
    line = fileC.readline()  
    if line==fengxMark:
       state=True
    fileC.close()
    return state
    
    
def fengxEorD(filePath,key):
    from time import time
    t = time()
    tS=os.path.split(filePath)
    #print isEncry(filePath)
    if isEncry(filePath)==True: 
        print ("解密文件-->>"+filePath)
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_decrypt" + os.path.splitext(tS[1])[1]
        deFile(filePath,fileOutPath,key)
        print ("输出文件-->>"+fileOutPath)
        print ("解密耗时: %f s" % (time() - t))
    else:
        print ("加密文件-->>"+filePath)
        fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_encrypt" + os.path.splitext(tS[1])[1]
        enFile(filePath,fileOutPath,key)
        print ("输出文件-->>"+fileOutPath)
        print ("加密耗时: %f s" % (time() - t))

'''

try:
    sys.argv[1]
except:
    #test="E:\\GitHub\\fengxEncrypt\\1.jpg"
    #test="K:\\fengxEncrypt\\1.jpg"
    test="K:\\fengxEncrypt\\fengxTest.txt"
    fengxEorD(test,key_1)
    print "没有拖拽！"
else:
    fengxEorD(sys.argv[1],key_1)

raw_input()

#my encrypt function
'''
'''
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


'''  
