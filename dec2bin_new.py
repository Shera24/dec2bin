#!/usr/bin/env python3
# Aufgabe: Decimal-binary-converter / Bitverschiebung 
# LEHNER Sarah-Jasmin
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause

led1=LED(18)
led2=LED(23)
led3=LED(24)
led4=LED(25)

class MyWindow(QMainWindow): 
    def __init__(self):
 
        super().__init__()
        self.setMinimumSize(QSize(500, 200))    
        self.setWindowTitle('Decimal-Binary-Converter') 

        wid = QWidget(self)        
        self.setCentralWidget(wid)        
        vbox= QVBoxLayout() 
        wid.setLayout(vbox)
        
          # slider / label display decimal
        sliderbox= QHBoxLayout() 
        wid.setLayout(sliderbox)
        
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setRange(0, 15)        
        self.slider.setStyleSheet("QSlider::handle:horizontal {height: 20px;}"
            "QSlider::sub-page:horizontal {background-color:rgb(0,100,255);}"
            "QSlider::handle:horizontal {background-color: white; border: 2px solid gray; border-radius: 4px; width: 20px;  height: 20px;}")  
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel('0') 
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)        
        vbox.addLayout(sliderbox)       
 
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")]
        self.length=len(self.bitlabels)
        print (self.length)
     
        bitbox = QHBoxLayout()       
        vboxBitboxes= QVBoxLayout()
        vboxBitboxes.addLayout(bitbox)        
        vboxBitboxes.setAlignment(Qt.AlignCenter)
        vbox.addLayout(vboxBitboxes)
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(127, 127, 127)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)
    
    

        
    def changeValue(self, value):  
        self.label.setText(str(value)) 
        for j in range(self.length):
            print (j)
            if (value & 1<<j):        
                self.bitlabels[self.length-1-j].setStyleSheet("background-color: rgb(255, 0, 0)")
                leds1.on()            
            else:
                self.bitlabels[self.length-1-j].setStyleSheet("background-color: rgb(127, 127, 127)")
                leds1.off()          


app = QtWidgets.QApplication([]) 
win = MyWindow()
win.show()
app.exec_()
