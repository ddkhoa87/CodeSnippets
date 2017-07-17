# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:29:54 2017

@author: DangKhoa

Unit test.
"""

import unittest
import TemplateMatching
import numpy as np

class Test(unittest.TestCase):
	
	def test_normalizedRange(self):
		mat = np.matrix([ [0.8, 0.9], [0.85, 0.95] ])
		mat_normed = TemplateMatching.normalizedRange(mat, 0.8, 0.95, 0, 1)
		self.assertEqual(mat_normed[0,0], 0)
		self.assertEqual(mat_normed[1,1], 1)
		pass
	
	def test_loadTemplate(self):
		templateImgs = TemplateMatching.loadTemplate('.\\Templates')
		self.assertGreater(len(templateImgs), 0)
		
def unittestMain():
	unittest.main();
	
unittestMain()