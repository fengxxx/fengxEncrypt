#coding=utf-8
import sys
import os
from time import time
from pyDes import *
from PyQt4 import QtCore, QtGui

import sip
#sip.setapi('QString', 2)
#sip.setapi('QVariant', 2)
# my
key_1="key"
#encrypt=1 decrypt=2
ED="null"


class WidgetGallery(QtGui.QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.setAcceptDrops(True)
        self.originalPalette = QtGui.QApplication.palette()


        
        styleComboBox = QtGui.QComboBox()
        styleComboBox.addItems(QtGui.QStyleFactory.keys())

        styleLabel = QtGui.QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QtGui.QCheckBox("&standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QtGui.QCheckBox("&Disable")

        #self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        #self.createBottomLeftTabWidget()
        #self.createBottomRightGroupBox()
        #self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        #disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1,2)
        #mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1,0)
        
        #mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
        self.changeStyle('Windows')
        try:
            #sys.argv[1]
            print sys.argv
        except:
            raw_input("don't click me ! dray file up me ! ")
        else:
            print "noll"
    def changeStyle(self, styleName):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(styleName))
        self.changePalette()
    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
        else:
            QtGui.QApplication.setPalette(self.originalPalette)
     
    def createTopRightGroupBox(self):
        self.topRightGroupBox = QtGui.QGroupBox("Group 2")

        defaultPushButton = QtGui.QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)
        B_en = QtGui.QPushButton("加密")
        defaultPushButton.setDefault(True)
        
        togglePushButton = QtGui.QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QtGui.QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(B_en)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)
  
def browse(self):
    directory = QtGui.QFileDialog.getExistingDirectory(self, "Find Files",
            QtCore.QDir.currentPath())

    if directory:
        if self.directoryComboBox.findText(directory) == -1:
            self.directoryComboBox.addItem(directory)

        self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))



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
''''
try:
	#sys.argv[1]
    print sys.argv
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
'''
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()

    sys.exit(app.exec_()) 
