# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:02:01 2017

@author: DangKhoa

Sample GUI.
"""

import sys
from PyQt5.QtWidgets import (QWidget, QApplication)
from PyQt5.QtWidgets import (QDesktopWidget)

from PyQt5.QtWidgets import (QGridLayout) # Grid layout
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout) # Box layout
from PyQt5.QtWidgets import (QPushButton, QTextEdit, QLabel, QCheckBox)

from PyQt5.QtGui import QIcon, QPixmap

class SimpleGUI(QWidget):
	
	def __init__(self):
		super().__init__()

		self.imageWidth = 1920
		self.imageHeight = 1080
		self.frameScaleRatio = 0.6
		
		self.initUI() 
		
		pass
		
	def initUI(self):

		self.resize(self.imageWidth*self.frameScaleRatio, self.imageHeight*self.frameScaleRatio)
		self.center()
		
		self.setWindowTitle('Simple GUI')
		self.setWindowIcon(QIcon('aircraft_icon.png'))

		self.setFODImageNameField('S01002_170614_123045', 'S01', '02', '170614', '123045')
		
		self.show()
		
		pass
	
	def center(self):
        
		qr = self.frameGeometry() # Obtain frame geometry
		cp = QDesktopWidget().availableGeometry().center() # Obtain screen resolution's center point
		qr.moveCenter(cp) # qr.topLeft() to move top-left corner
		self.move(qr.topLeft())
	
		pass
	
	def createEmptyBoxLayout(self):
		vboxEmpty = QVBoxLayout()
		emptyspace0 = QLabel('\t');
		vboxEmpty.addWidget(emptyspace0)
		vboxEmpty.addStretch(1)
		return vboxEmpty
		pass
	
	def setFODImageNameField(self, imageName, cameraID, subsectorID, date, time):
		
		title_FODImgName = QLabel('Image name: ' + imageName)
		title_cameraID = QLabel('Camera: ' + cameraID)
		title_subsectorID = QLabel('Subsector: ' + subsectorID)
		title_date = QLabel('Date: ' + date)
		title_time = QLabel('Time: ' + time)
		
		vbox1 = QVBoxLayout()
		vbox1.addWidget(title_FODImgName)
		vbox1.addWidget(title_cameraID)
		vbox1.addWidget(title_subsectorID)
		vbox1.addWidget(title_date)
		vbox1.addWidget(title_time)
		vbox1.setSpacing(10)
		vbox1.addStretch(1) # Add a strechable h-space before the widgets
		
		title_UserRemark = QLabel('User Remark: ')
		textbox_UserRemark = QTextEdit() # multiple lines
		textbox_UserRemark.setFixedHeight(textbox_UserRemark.document().size().height()*4)
		textbox_UserRemark.setFixedWidth(textbox_UserRemark.document().size().width()*20)
		textbox_UserRemark.setDisabled(True)
		gridUserRemark = QGridLayout()
		gridUserRemark.addWidget(textbox_UserRemark, 0, 0) # row 1 col 0, span 1 row 1 col
		vbox2 = QVBoxLayout()
		vbox2.addWidget(title_UserRemark)
		vbox2.addLayout(gridUserRemark)
		vbox2.setSpacing(10)
		vbox2.addStretch(1)
		
		title_SSLRemark = QLabel('SSL Remark: ')
		textbox_SSLRemark = QTextEdit() # multiple lines
		textbox_SSLRemark.setFixedHeight(textbox_SSLRemark.document().size().height()*4)
		textbox_SSLRemark.setFixedWidth(textbox_SSLRemark.document().size().width()*20)
		gridSSLRemark = QGridLayout()
		gridSSLRemark.addWidget(textbox_SSLRemark, 0, 0) # row 1 col 0, span 1 row 1 col
		vbox3 = QVBoxLayout()
		vbox3.addWidget(title_SSLRemark)
		vbox3.addLayout(gridSSLRemark)
		vbox3.setSpacing(10)
		vbox3.addStretch(1)
		
		button_SaveRemarks = QPushButton("Save Remarks")
		button_CopyImage = QPushButton("Copy Image")
		checkbox_skipEmptyImg = QCheckBox("Skip empty images")
		checkbox_skipEmptyImg.setChecked(True)
		#checkbox_skipEmptyImg.hide() # Not to let users know there are FOD detail without images.
		vbox4 = QVBoxLayout()
		vbox4.addWidget(button_SaveRemarks)
		vbox4.addWidget(button_CopyImage)
		vbox4.addWidget(checkbox_skipEmptyImg)
		vbox4.setSpacing(10);
		vbox4.addStretch(1)
		
		hbox = QHBoxLayout()
		hbox.addLayout(vbox1)
		hbox.addLayout(self.createEmptyBoxLayout())
		hbox.addLayout(vbox2)
		#hbox.addLayout(self.createEmptyBoxLayout())
		hbox.addLayout(vbox3)
		hbox.addLayout(self.createEmptyBoxLayout())
		hbox.addLayout(vbox4)
		hbox.addStretch(1) # Add strechable v-space above the h-box

		pixmap_FODImage = QPixmap("FODImage.jpg")
		pixmap_FODImage = pixmap_FODImage.scaledToWidth(self.imageWidth * self.frameScaleRatio)
		display_FODImage = QLabel(self)		
		display_FODImage.setPixmap(pixmap_FODImage)
		
		gridAppLayout = QGridLayout()
		gridAppLayout.addLayout(hbox, 0, 0)
		gridAppLayout.addWidget(display_FODImage, 1, 0)
		self.setLayout(gridAppLayout)
		
		pass
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = SimpleGUI()
	sys.exit(app.exec_())
	#app.exec_()
