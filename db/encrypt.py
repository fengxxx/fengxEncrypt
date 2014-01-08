#coding=utf-8
import sys
import os
from time import time
from pyDes import *

# my
key_1="key"
#encrypt=1 decrypt=2
ED="null"


def enFile(filePath,targetPath,key):
	f = open(filePath, "rb+")
	d = f.read()
	f.close()
	t = time()
	k = des(key)

	d = k.encrypt(d, " ")
	f = open(targetPath, "wb+")
	f.write(d)
	f.close()

	print ("encrypt time: %f s" % (time() - t))

def deFile(filePath,targetPath,key):
	f = open(filePath, "rb+")
	d = f.read()
	f.close()

	t = time()
	k = des(key)

	d = k.decrypt(d, " ")
	f = open(targetPath, "wb+")
	f.write(d)
	f.close()

	print ("decrypt time: %f s" % (time() - t))	

try:
	sys.argv[1]
except:
	raw_input("don't click me ! dray file up me ! ")
else:
	print "encrypt enter 1"
	print "decrypt enter 2"
	ED=str(raw_input("choice:"))
	while ED!="1" and ED!="2":
		if ED!="1" or ED!="2": 
			print "Please enter 1 or 2"
			ED=raw_input("choice:")
	key_1=raw_input("enter the key:")
	while len(key_1)!=8:
		if len(key_1)!=8:
			print "key's lenght wrong !"   
			print "Please enter a string of length 8"
			key_1=raw_input("enter the key:")
	t = time()
	filePath=sys.argv[1]
	tS=os.path.split(filePath)
	fileOutPath=tS[0]+"\\"+os.path.splitext(tS[1])[0] +"_decrypt" + os.path.splitext(tS[1])[1]
	if ED=="1":
		enFile(filePath,fileOutPath,key_1)
	if ED=="2":
		deFile(filePath,fileOutPath,key_1)
	#print ("output file-->>"+fileOutPath)
	#print ("enFile time: %f s" % (time() - t)) 

