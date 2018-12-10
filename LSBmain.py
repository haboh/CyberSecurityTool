import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import LSBDecode
import LSBEncode


class LSBmain(QWidget,
              CyberSecurityTool):  # LSBmain is a child of CyberSecurityTool class
    def __init__(self):
        super().__init__()
        uic.loadUi('LSBcipher.ui', self)  # Loading UI file to work with
        self.decodeButton.clicked.connect(
            self.runDecode)  # on click decodeButton will run runDecode function
        self.encodeButton.clicked.connect(
            self.runEncode)  # on click encodeButton will run runEncode function

    def runDecode(self):  # runDecode function runs LSBDecode app
        lsbdec = LSBDecode.LSBDecode()  # running LSBDecode
        lsbdec.show()

    def runEncode(self):  # runEncode function runs LSBEncode app
        lsbenc = LSBEncode.LSBEncode()  # running LSBEncode
        lsbenc.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prog = LSBmain()
    prog.show()
    sys.exit(app.exec())
