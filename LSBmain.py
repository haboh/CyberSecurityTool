#  _       _____ ____   _____ _       _               
# | |     / ____|  _ \ / ____(_)     | |              
# | |    | (___ | |_) | |     _ _ __ | |__   ___ _ __ 
# | |     \___ \|  _ <| |    | | '_ \| '_ \ / _ \ '__|
# | |____ ____) | |_) | |____| | |_) | | | |  __/ |   
# |______|_____/|____/ \_____|_| .__/|_| |_|\___|_|    by fatnet
#                              | |                    
#                              |_|                    



import sys
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QInputDialog
from PyQt5.QtGui import QPixmap, QIcon


class LSBmain(QMainWindow):  # LSBmain is a child of CyberSecurityTool class
    def __init__(self):
        super().__init__()
        uic.loadUi('LSBcipher.ui', self)  # Loading UI file to work with
        self.decodeButton.clicked.connect(
            self.runDecode)  # on click decodeButton will run runDecode function
        self.encodeButton.clicked.connect(
            self.runEncode)  # on click encodeButton will run runEncode function

    def runDecode(self):  # runDecode function runs LSBDecode app
        lsbdec = LSBDecode(self)  # running LSBDecode
        lsbdec.show()

    def runEncode(self):  # runEncode function runs LSBEncode app
        lsbenc = LSBEncode(self)  # running LSBEncode
        lsbenc.show()


class LSBDecode(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('LSBcipherdecode.ui', self)
        self.decodeType=""
        self.image=None
        self.height=None
        self.width=None
        self.pix=None
        self.redmsg=""
        self.greenmsg=""
        self.blumsg=""
        self.rgbmsg=""
        self.previewImg=None
        self.MAXSIZE = (PREVIEWW, PREVIEWH)
        self.decodeButton.clicked.connect(self.decodeBtn)
        self.fileExplorerButton.clicked.connect(self.openFileNameDialog)
        self.previewButton.clicked.connect(self.makePreview)

    def decodeBtn(self):
        i, okBtnPressed = QInputDialog.getItem(
    		self, 
    		"Decode",
    		"Choose decoding type",
    		("Through Columns", "Through Rows"),
    		1,
    		False
		)
		if okBtnPressed:
            self.decodeType=i
        if self.decodeType="Through Columns":
        	self.columnDecode()
        else:
        	self.rowDecode()

    def openImg(self):
    	self.image = Image.open(pathEdit.getText())  
		self.width = image.size[0] 
		self.height = image.size[1] 	
		self.pix = image.load()

    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)", options=options)
        if fileName:
            self.pathEdit.setText(fileName)

    def makePreview(self):
    	self.openImg()
		self.previewImg = self.image.thumbnail(self.maxsize, Image.ANTIALIAS)
		self.previewImg.save("previewLSBhabohXfatnet.png")
		pixmap = QPixmap("previewLSBhabohXfatnet.png")
		self.previewLabel.setPixmap(pixmap)
		
    def columnDecode(self):
    	pass

    def rowDecode(self):
    	pass



class LSBEncode(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi('LSBcipherencode.ui', self)
        self.image=None
        self.msg=""
        self.channel=""
        self.encodeType=""
        self.previewImg=None
        self.MAXSIZE = (PREVIEWW, PREVIEWH)
        self.encodeButton.clicked.connect(self.encodeBtnChnl)
        self.fileExplorerButton.clicked.connect(self.runExplorer)
        self.previewButton.clicked.connect(self.makePreview)
        self.saveFileButton.clicked.connect(self.saveFileDialog)

    def encodeBtnChnl(self):
        i, okBtnPressed = QInputDialog.getItem(
    		self, 
    		"Encode",
    		"Choose channel to encode to",
    		("Red", "Green", "Blue", "RGB"),
    		1,
    		False
		)
		if okBtnPressed:
            self.channel=i
	        self.encodeBtnType()

	def encodeBtnType(self):
		j, okBtnPressed = QInputDialog.getItem(
    		self, 
    		"Encode",
    		"Choose encoding type",
    		("Through Columns", "Through Rows"),
    		1,
    		False
		)
		if okBtnPressed:
            self.encodeType=j
        if self.decodeType="Through Columns":
        	self.columnEncode()
        else:
        	self.rowEncode()

    def openImg(self):
    	self.image = Image.open(pathEdit.getText())  
		self.width = self.image.size[0] 
		self.height = self.image.size[1] 	
		self.pix = self.image.load()

    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)", options=options)
        if fileName:
            self.pathEdit.setText(fileName)


    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileNa me, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)", options=options)

    def makePreview(self):
    	self.openImg()
		self.previewImg = self.image.thumbnail(self.maxsize, Image.ANTIALIAS)
		self.previewImg.save("previewLSBhabohXfatnet.png")
		pixmap = QPixmap("previewLSBhabohXfatnet.png")
		self.previewLabel.setPixmap(pixmap)

    def columnEncode(self):
    	pass

    def rowEncode(self):
    	pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    prog = LSBmain()
    prog.show()
    sys.exit(app.exec())
