#coding=utf-8
from fengxEncrypt import *
key_1="key"
while len(key_1)!=8:
    key_1=raw_input("enter the key:")
    if len(key_1)!=8:
        print "key's lenght wrong !"  
        print "Please enter a string of length 8"
try:
    sys.argv[1]
except:
    print ""
else:
    from time import time
    t = time()
    filePath=sys.argv[1]
    tS=os.path.split(filePath)
    fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_decrypt" + os.path.splitext(tS[1])[1]
    deFile(filePath,fileOutPath,key_1)
    #print ("output file-->>"+fileOutPath)
    #print ("deFile time: %f s" % (time() - t))
#raw_input()
