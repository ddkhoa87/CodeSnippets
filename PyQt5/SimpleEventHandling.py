# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:50:12 2017

@author: DangKhoa

Testing simple event handling, getting information of the sender, emmiting signal.
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication,
										 QLCDNumber, QSlider, 
										 QPushButton, QCheckBox,
										 QVBoxLayout, )
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow

class Communicate(QObject):
    
    closeApp = pyqtSignal() # Declare a PyQT Signal
	
class SimpleEventHandler(QWidget):
	
	def __init__(self):
		super().__init__()
        
		self.initUI()
	
	def initUI(self):
        
		lcd = QLCDNumber(self) # Numbers displayed as on the pocket calculator screen
		sld = QSlider(Qt.Horizontal, self)
		
		# Here we connect a valueChanged signal of the slider to the display slot of the lcd number.
		# The sender is an object that sends a signal. 
		# The receiver is the object that receives the signal.
		# The slot is the method that reacts to the signal.
		sld.valueChanged.connect(lcd.display)
		
		btn1 = QPushButton("Button 1", self)
		btn1.clicked.connect(self.buttonClicked)
		
		b1 = QCheckBox("Check Button 1", self)
		b1.setChecked(True)
		b1.stateChanged.connect(lambda:self.btnstate(self.b1))
		b1.move(30, 30)
		
	  	#self.statusBar()
		
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Signal & slot')
		
		# Create a Communicate object
		self.c = Communicate() 
		# The custom closeApp signal is connected to the close() slot of the QMainWindow.
		self.c.closeApp.connect(self.close) 
		
		self.show()

	# When we click on the window with a mouse pointer, 
	# the closeApp signal is emitted
	def mousePressEvent(self, event):
    
		self.c.closeApp.emit()
	
	# Reimplement event handler	
	def keyPressEvent(self, e):

		if e.key() == Qt.Key_Escape:
			self.close()

	# Get information of the sender
	def buttonClicked(self):
		
		sender = self.sender()
		print(sender.text() + ' was pressed')
		#self.statusBar().showMessage(sender.text() + ' was pressed')
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = SimpleEventHandler()
	app.exec_()
