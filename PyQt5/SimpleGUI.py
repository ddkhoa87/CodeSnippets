# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:22:22 2017

@author: DangKhoa

Testing PyQt5 simple GUI.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtWidgets import (QDesktopWidget)
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QTextEdit, QLabel)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout) # Box layout
from PyQt5.QtWidgets import (QGridLayout) # Grid layout
from PyQt5.QtGui import QIcon

class SimpleGUI(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI() 
		
	def initUI(self):

		self.setGeometry(300, 300, 350, 300)
		
		#self.resize(300, 200)
		#self.center()
		
		self.initUI_GridLayoutSpanning()
		
		self.setWindowTitle('Simple GUI')
		self.setWindowIcon(QIcon('aircraft_icon.png'))

		self.show()

	def center(self):
        
		qr = self.frameGeometry() # Obtain frame geometry
		cp = QDesktopWidget().availableGeometry().center() # Obtain screen resolution's center point
		qr.moveCenter(cp) # qr.topLeft() to move top-left corner
		
		# We move the top-left point of the application window to the top-left point of the qr rectangle, 
		# thus centering the window on our screen.
		self.move(qr.topLeft()) 
	
	def initUI_GridLayoutSpanning(self):

		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')
		
		titleEdit = QLineEdit() # one line
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit() # multiple lines
		
		grid = QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(title, 1, 0) # row 1 col 0
		grid.addWidget(titleEdit, 1, 1) # row 1 col 1

		grid.addWidget(author, 2, 0) 
		grid.addWidget(authorEdit, 2, 1)

		grid.addWidget(review, 3, 0)
		grid.addWidget(reviewEdit, 3, 1, 5, 1) # row 3 col 1, span 5 rows 1 col
		
		self.setLayout(grid) 
	
	def initUI_GridLayout(self):
		grid = QGridLayout()
		self.setLayout(grid)
 
		names = ['Cls', 'Bck', '', 'Close',
						'7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        
		positions = [(i,j) for i in range(5) for j in range(4)]
        
		for position, name in zip(positions, names):
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)
			
	def initUI_BoxLayout(self):
		
		okButton = QPushButton("OK")
		cancelButton = QPushButton("Cancel")
		
		hbox = QHBoxLayout()
		hbox.addStretch(1) # Add a strechable h-space before the buttons
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)
		
		vbox = QVBoxLayout()
		vbox.addStretch(1) # Add strechable v-space above the h-box
		vbox.addLayout(hbox)
		
		self.setLayout(vbox)  
		
	def closeEvent(self, event):
		pass
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = SimpleGUI()
	#sys.exit(app.exec_())  
	app.exec_()
