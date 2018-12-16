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
from PyQt5.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QInputDialog, \
    QFileDialog
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
        self.path=None
        uic.loadUi('LSBcipherdecode.ui', self)
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
            self.path=fileName

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


class LSBEncode(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.image = None
        self.msg = ""
        self.channel = ""
        self.encodeType = ""
        self.previewImg = None
        self.MAXSIZE = (200, 200)
        self.path=None
        uic.loadUi('LSBcipherencode.ui', self)
        self.encodeButton.clicked.connect(self.encodeBtnChnl)
        self.fileExplorerButton.clicked.connect(self.runExplorer)
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
            self.path=fileName

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "QFileDialog.getSaveFileName()",
                                                  "",
                                                  "BMP files (*.bmp);;PNG files (*.png);;JPG Files (*.jpg)",
                                                  options=options)

    def makePreview(self):
        self.openImg()
        self.previewImg = self.image.thumbnail(self.maxsize, Image.ANTIALIAS)
        self.previewImg.save("previewLSBhabohXfatnet.png")
        pixmap = QPixmap("previewLSBhabohXfatnet.png")
        self.previewLabel.setPixmap(pixmap)

    def columnEncode(self):
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        iterator = 0
        flag = 1
        for i in range(w):
            if flag == 0:
                break
            for j in range(h):
                if self.channel == "Red":
                    iterator += 1
                    if self.msg[iterator] == '0':
                        if self.pix[i, j][0] % 2 == 0:
                            continue
                        self.pix[i, j][0] = self.pix[i, j][0] - 1
                    else:
                        if self.pix[i,j][0] % 2 == 1:
                            continue
                        self.pix[i,j][0] = self.pix[i,j][0] + 1
                if self.channel == "Green":
                    iterator += 1
                    if self.msg[iterator] == '0':
                        if self.pix[i, j][1] % 2 == 0:
                            continue
                        self.pix[i, j][1] = self.pix[i, j][1] - 1
                    else:
                        if self.pix[i, j][1] % 2 == 1:
                            continue
                        self.pix[i, j][1] = self.pix[i, j][1] + 1
                if self.channel == "Blue":
                    if self.msg[iterator] == '0':
                        if self.pix[i, j][2] % 2 == 0:
                            continue
                        self.pix[i, j][2] = self.pix[i, j][2] - 1
                    else:
                        if self.pix[j, i][2] % 2 == 1:
                            continue
                        self.pix[i, j][2] = self.pix[i, j][2] + 1
                if iterator >= len(self.msg):
                    flag = 0
                    break

    def rowEncode(self):
        img = Image.open(self.path)
        w, h = img.size[0], img.size[1]
        pix = img.load()
        iterator = 0
        flag=1
        for i in range(h):
            if flag==0:
                break
            for j in range(w):
                if self.channel=="Red":
                    iterator+=1
                    if self.msg[iterator]=='0':
                        if pix[j, i][0]%2==0:
                            continue
                        pix[j, i][0]=pix[j,i][0]-1
                    else:
                        if pix[j, i][0]%2==1:
                            continue
                        pix[j,i][0]=pix[j,i][0]+1
                if self.channel=="Green":
                    iterator+=1
                    if self.msg[iterator]=='0':
                        if pix[j, i][1]%2==0:
                            continue
                        pix[j, i][1]=pix[j,i][1]-1
                    else:
                        if pix[j, i][1]%2==1:
                            continue
                        pix[j,i][1]=pix[j,i][1]+1
                if self.channel=="Blue":
                    if self.msg[iterator]=='0':
                        if pix[j, i][2]%2==0:
                            continue
                        pix[j, i][2]=pix[j,i][2]-1
                    else:
                        if pix[j, i][2]%2==1:
                            continue
                        pix[j,i][2]=pix[j,i][2]+1
                if iterator>=len(self.msg):
                    flag=0
                    break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prog = LSBmain()
    prog.show()
    sys.exit(app.exec())
