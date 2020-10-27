#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
論文等のPDFからの文字のパーサ
'''

# Variable name "ほげ" doesn't conform to snake_case naming style
# pylint: disable=C0103


import sys
import pyperclip as clip
from PyQt5 import QtCore, QtGui, QtWidgets, uic





def text_convert(text,mode=0):
	"""
		テキストの不要な改行を除いた後、句読点で再度改行を付与する
	"""
	text = text.replace('\n','')

	if mode == 0:
		text = text.replace('．','．\n')


	return text

class PTF_UI(QtWidgets.QMainWindow):
	"""
		hoge
	"""
	def __init__(self, parent=None):

		QtWidgets.QMainWindow.__init__(self)
		UI_class = uic.loadUiType("UI.ui", self)[0]

		self.ui = UI_class()
		self.ui.setupUi(self)

		self.ui.Textbox_red.setPlainText(clip.paste())

		self.ui.Botton_read_cb.clicked.connect(self.Botton_read_cb_clicked)
		self.ui.Button_run.clicked.connect(self.Button_run_clicked)
		self.ui.Button_write.clicked.connect(self.Button_write_clicked)


	@QtCore.pyqtSlot()
	def Button_run_clicked(self):
		"""
			変換前の文字列を変換し、変換後窓とクリップボードに書出し
		"""
		text = self.ui.Textbox_red.toPlainText()
		print(f"[debug]変換前[{text}]")

		text = text_convert(text)
		print(f"[debug]変換後[{text}]")

		self.ui.Textbox_send.setPlainText(text)
		clip.copy(text)


	@QtCore.pyqtSlot()
	def Botton_read_cb_clicked(self):
		"""
			クリップボードから読込み
		"""
		self.ui.Textbox_red.setPlainText(clip.paste())

	@QtCore.pyqtSlot()
	def Button_write_clicked(self):
		"""
			クリップボードへ書出し
		"""
		text = self.ui.Textbox_send.toPlainText()
		clip.copy(text)

if __name__ == '__main__':
	#main()
	app = QtWidgets.QApplication(sys.argv)
	window = PTF_UI()
	window.show()

	sys.exit(app.exec_() )
