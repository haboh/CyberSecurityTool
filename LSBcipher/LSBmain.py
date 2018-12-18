#  _       _____ ____   _____ _       _
# | |     / ____|  _ \ / ____(_)     | |
# | |    | (___ c| |_) | |     _ _ __ | |__   ___ _ __
# | |     \___ \|  _ <| |    | | '_ \| '_ \ / _ \ '__|
# | |____ ____) | |_) | |____| | |_) | | | |  __/ |
# |______|_____/|____/ \_____|_| .__/|_| |_|\___|_|    by fatnet
#                              | |
#                              |_|


import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QInputDialog, \
    QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from LSBcipher.LSBcipherdecodeUI import LSBDecodeUI
from LSBcipher.LSBcipherencodeUI import LSBEncodeUI
from LSBcipher.LSBcipherUI import LSBMainUI
from PIL.ImageQt import ImageQt
import os


# Debugged. Works Ok.
def bin_encrypt(s):  # binary cipher encrypt function
    st = s.split()
    ciph = []
    for word in st:
        for letter in word:
            ciph.append(bin(ord(letter))[2:])
    return ' '.join(ciph)


# Debugged. Works Ok.
def bin_decrypt(s):  # binary cipher decrypt function
    st = s.split()
    enc = ''
    for n in st:
        enc += chr(int(n, 2))
    return enc


# This function takes PIL image and convert it into the QPixMap
def convert_image_to_pix_map(im):
    im = im.convert("RGBA")
    qim = ImageQt(im)
    pix = QPixmap.fromImage(qim)
    return pix


# Debugged. Works Ok.
class LSBmain(QMainWindow, LSBMainUI):  # LSBmain is a child of CyberSecurityTool class
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.decodeButton.clicked.connect(
            self.runDecode)  # on click decodeButton will run runDecode function
        self.encodeButton.clicked.connect(
            self.runEncode)  # on click encodeButton will run runEncode function
        self.decodeButton.setEnabled(False)

    def runDecode(self):  # runDecode function runs LSBDecode app
        lsbdec = LSBDecode(self)  # running LSBDecode
        lsbdec.show()

    def runEncode(self):  # runEncode function runs LSBEncode app
        lsbenc = LSBEncode(self)  # running LSBEncode
        lsbenc.show()


class LSBDecode(QMainWindow, LSBDecodeUI, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.decodeType = ""
        self.image = None
        self.height = None
        self.width = None
        self.pix = None
        self.redmsg = ""
        self.greenmsg = ""
        self.blumsg = ""
        self.rgbmsg = ""
        self.previewImg = None
        self.MAXSIZE = (200, 200)
        self.path = None
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
            self.decodeType = i
            if self.decodeType == "Through Columns":
                self.columnDecode()
            else:
                self.rowDecode()

    def openImg(self):
        self.image = Image.open(self.pathEdit.text())
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "QFileDialog.getOpenFileName()",
                                                  "",
                                                  "BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)",
                                                  options=options)
        if fileName:
            self.pathEdit.setText(fileName)
            self.path = fileName

    def makePreview(self):
        self.openImg()
        self.previewImg = self.image.thumbnail(self.maxsize, Image.ANTIALIAS)
        self.previewImg.save("previewLSBhabohXfatnet.png")
        pixmap = QPixmap("previewLSBhabohXfatnet.png")
        self.previewLabel.setPixmap(pixmap)

    def columnDecode(self):
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        red = ''
        green = ''
        blue = ''
        all = ''
        pix = img.load()
        for i in range(w):
            for j in range(h):
                red = red + str(pix[i, j][0] % 2)
                green = green + str(pix[i, j][1] % 2)
                blue = blue + str(pix[i, j][2] % 2)
                all = all + str(pix[i, j][0] % 2) + str(
                    pix[i, j][1] % 2) + str(pix[i, j][2] % 2)
        self.lineEdit_r.setText(red)
        self.lineEdit_rr.setText(red[::-1])
        self.lineEdit_g.setText(green)
        self.lineEdit_gr.setText(green[::-1])
        self.lineEdit_b.setText(blue)
        self.lineEdit_br.setText(blue[::-1])
        self.lineEdit_rgb.setText(all)
        self.lineEdit_rgbr.setText(all[::-1])

    def rowDecode(self):
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        red = ''
        green = ''
        blue = ''
        all = ''
        pix = img.load()
        for i in range(h):
            for j in range(w):
                red = red + str(pix[j, i][0] % 2)
                green = green + str(pix[j, i][1] % 2)
                blue = blue + str(pix[j, i][2] % 2)
                all = all + str(pix[j, i][0] % 2) + str(
                    pix[j, i][1] % 2) + str(pix[j, i][2] % 2)
        self.lineEdit_r.setText(red)
        self.lineEdit_rr.setText(red[::-1])
        self.lineEdit_g.setText(green)
        self.lineEdit_gr.setText(green[::-1])
        self.lineEdit_b.setText(blue)
        self.lineEdit_br.setText(blue[::-1])
        self.lineEdit_rgb.setText(all)
        self.lineEdit_rgbr.setText(all[::-1])


class LSBEncode(QMainWindow, LSBEncodeUI, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.msg, self.channel, self.encodeType = "", "", ""
        self.previewImg, self.path, self.image = None, None, None
        self.MAXSIZE = (200, 200)
        self.encodeButton.clicked.connect(self.encodeBtnChnl)
        self.fileExplorerButton.clicked.connect(self.openFileNameDialog)
        self.previewButton.clicked.connect(self.makePreview)
        self.saveFileButton.clicked.connect(self.saveFileDialog)

    def encodeBtnChnl(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Encode",
            "Choose channel to encode to",
            ("Red", "Green", "Blue"),
            1,
            False
        )
        if okBtnPressed:
            self.channel = i
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
            self.encodeType = j
            if self.encodeType == "Through Columns":
                self.columnEncode()
            else:
                self.rowEncode()

    def openImg(self):
        file_name = self.pathEdit.text()
        if os.path.exists(file_name):
            self.image = Image.open(file_name)
            self.width = self.image.size[0]
            self.height = self.image.size[1]
            self.pix = self.image.load()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   "QFileDialog.getOpenFileName()",
                                                   "",
                                                   "BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)",
                                                   options=options)
        if file_name:
            self.pathEdit.setText(file_name)
            self.path = file_name

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self,
                                                   "QFileDialog.getSaveFileName()",
                                                   "",
                                                   "BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)",
                                                   options=options)
        self.image.save(file_name)

    def error(self):
        QMessageBox('Error').show()

    def makePreview(self):
        try:
            self.openImg()
            self.previewImg = self.image.copy()
            self.previewImg.thumbnail(self.MAXSIZE, Image.ANTIALIAS)
            pixmap = convert_image_to_pix_map(self.previewImg)
            self.previewLabel.setPixmap(pixmap)
        except Exception:
            self.error()

    def get_message(self):
        m = self.msgEdit.text()
        return bin_encrypt(m)

    def columnEncode(self):
        self.msg = self.get_message()
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        iterator = 0
        flag = 1
        for i in range(w):
            if flag == 0:
                break
            for j in range(h):
                if iterator >= len(self.msg):
                    flag = 0
                    break
                if self.channel == "Red":
                    self.pix[i, j][0] = int(self.msg[iterator])
                if self.channel == "Green":
                    self.pix[i, j][1] = int(self.msg[iterator])
                if self.channel == "Blue":
                    self.pix[i, j][2] = int(self.msg[iterator])
                iterator += 1

    def rowEncode(self):
        self.msg = self.get_message()
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        iterator = 0
        flag = 1
        for j in range(h):
            if flag == 0:
                break
            for i in range(w):
                if iterator >= len(self.msg):
                    flag = 0
                    break
                if self.channel == "Red":
                    self.pix[i, j][0] = int(self.msg[iterator])
                if self.channel == "Green":
                    self.pix[i, j][1] = int(self.msg[iterator])
                if self.channel == "Blue":
                    self.pix[i, j][2] = int(self.msg[iterator])
                iterator += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prog = LSBmain()
    prog.show()
    sys.exit(app.exec())
