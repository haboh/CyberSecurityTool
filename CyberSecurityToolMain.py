from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
from CyberSecurityToolUI import Ui_CyberSecurityTool
from Stegano.stegsolve import SteganoMainWindow
from CryptoTool.CryptoToolmain import CryptoToolMainWindow
from FrequencyTextAnalysis.FrequencyAnalysis import FrequencyAnalysisMainWindow
import sys


class CyberSecurityTooMainWindow(QMainWindow, Ui_CyberSecurityTool):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PixMap.setPixmap(QPixmap('CyberSecurityTool.jpg'))
        self.SteganoButton.clicked.connect(self.create_stegano_window)
        self.CryptoToolButton.clicked.connect(self.create_crypto_tool_window)
        self.FrequencyTextAnalysisButton.clicked.connect(self.create_frequency_text_analysis_window)
        # self.LSBcipherButton.clicked.connect()

    def create_stegano_window(self):
        SteganoMainWindow(self).show()

    def create_crypto_tool_window(self):
        CryptoToolMainWindow(self).show()

    def create_frequency_text_analysis_window(self):
        FrequencyAnalysisMainWindow(self).show()


def main():
    app = QApplication(sys.argv)
    ex = CyberSecurityTooMainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
