#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSlider, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import *
from gpiozero import LED, LEDBoard


# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(250, 120))    
        self.setWindowTitle('Dezimal-Binär-Rechner')
        #self.bitlabels()
        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        vlayout = QVBoxLayout()
        wid.setLayout(vlayout)

        #self.lcd_number = QLCDNumber(2, wid)
        #vlayout.addWidget(self.lcd_number)

        hlayout = QHBoxLayout()
        vlayout.addLayout(hlayout)
        

# Slider + Label Anzeige Dezimalwert
        self.slider = QSlider(Qt.Horizontal)
        self.label = QLabel('0') 
        sliderbox = QHBoxLayout()
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)

        # Labels fuer 4 Bits
    def bitlabels(self):
        bl1 = QLabel('8')
        bl2 = QLabel('4')
        bl3 = QLabel('2')
        bl4 = QLabel('1')
        
        vbox = QVBoxLayout()
        vbox.addWidget(bl1)
        vbox.addWidget(bl2)
        vbox.addWidget(bl3)
        vbox.addWidget(bl4)
        
        setStyleSheet("background-color: rgb(x, y, z)") mit x, y, z

        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        
        self.show()

        # Layout zusammenbauen
        vbox = QVBoxLayout()
        vbox.addLayout(sliderbox)
        vbox.addLayout(bitbox)

        # vbox anzeigen in QWidget
        self.setLayout(vbox)
        
    def dec2bin(self):
        value = 0
       # for index,
       
       
       self.leds = LEDBoard (18,23, 24, 25)

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()