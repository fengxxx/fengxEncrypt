# -*- coding: cp936 -*-
import struct  
 
a = 20 
b = 400 
c="����"
#str = struct.pack("ii", a, b)  
#print 'length:', len(str)  
#print str  
#print repr(str)  
 
def encrypt(key, s): 
    b = bytearray(str(s).encode("gbk")) 
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
 
def decrypt(key, s): 
    c = bytearray(str(s).encode("gbk")) 
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
 
key = 15 
s1 = encrypt(key, 'hello world') 
s2 = decrypt(key, s1) 
print s1
print s2
