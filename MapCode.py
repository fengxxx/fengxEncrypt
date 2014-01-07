
import struct

def toString_BMP(filePath):
    mapInfor=["" for i in range(20)]
    
    fileC=open(filePath,"rb")
    line = fileC.readline()
    width_b=(line[18]+line[19]+line[20]+line[21])
    height_b=(line[22]+line[23]+line[24]+line[25])

   
    
    width=struct.unpack("i",width_b)[0]
    height=struct.unpack("i",height_b)[0]

    #-- map infor
    i=1
    for c in line:        
  
        if i>=0 and i<=2:
            mapInfor[0]+=c
        if i>=3 and i<=6:
            mapInfor[1]+=c
        if i>=19 and i<=22:
            mapInfor[2]+=c
        if i>=22 and i<=26:
            mapInfor[3]+=c
        if i>=35 and i<=38:
            mapInfor[4]+=c
        i+=1
    #mapInfor[0][0]=struct.unpack("c",mapInfor[0][0])
    print len(mapInfor[1])

    mapInfor[1]=struct.unpack("i",mapInfor[1])
    mapInfor[2]=struct.unpack("i",mapInfor[2])
    #mapInfor[3]=struct.unpack("i",mapInfor[3])
    #mapInfor[4]=struct.unpack("I",mapInfor[4])
    #print struct.unpack("c3Iu",mapInfor[0],mapInfor[1],mapInfor[2],mapInfor[3],mapInfor[4])

    #print ("bitmap size = " size)
    print ("bitmap dpi = " +str(width) +"x"+str(height))


    fileC.close()
    print mapInfor
bmpPath="K:\\fengxEncrypt\\testPNG.bmp"
#bmpPath="E:\\GitHub\\fengxEncrypt\\testPNG.bmp"
toString_BMP(bmpPath)