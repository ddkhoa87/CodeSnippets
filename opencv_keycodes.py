# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:16:13 2017

@author: DangKhoa

Detect key code with cv2 package

2424832 left arrow
2555904 right arrow
2490368 up arrow
2621440 down arrow

if key == ord('q')

"""
import cv2

if __name__ == '__main__':

	while True:
		#key = input("Keyboard input: ")
		key = cv2.waitKey()
		print(key)
		if key == ord('q'):
			break
