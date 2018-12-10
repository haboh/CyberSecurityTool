import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class SteganoIMGRead(QWidget):
    def __init__(self):
        super().__init__()
        self.makeUI()

    def makeUI(self):
        self.setGeometry(0, 0, 550, 600)
        self.setWindowTitle(
            "LSB IMG Read")

        self.btnshow = QPushButton(self)
        self.btnshow.resize(200, 100)
        self.btnshow.setText("Show all the LSB")
        self.btnshow.move(160, 20)
        self.btnshow.clicked.connect(self.readimg)

        self.label = QLabel(self)
        self.label.resize(370, 100)
        self.label.move(5, 127)
        self.label.setText(
            "Insert path full to your img here(with name and .png/.bmp/etc)->")

        self.filename = QLineEdit(self)
        self.filename.resize(170, 100)
        self.filename.move(375, 127)

        self.red = QLabel(self)
        self.red.resize(80, 40)
        self.red.move(240, 234)
        self.red.setText("RED:")

        self.redLine = QLineEdit(self)
        self.redLine.resize(400, 40)
        self.redLine.move(75, 279)

        self.green = QLabel(self)
        self.green.resize(80, 40)
        self.green.move(240, 324)
        self.green.setText("GREEN:")

        self.greenLine = QLineEdit(self)
        self.greenLine.resize(400, 40)
        self.greenLine.move(75, 369)

        self.blue = QLabel(self)
        self.blue.resize(80, 40)
        self.blue.move(240, 414)
        self.blue.setText("BLUE:")

        self.blueLine = QLineEdit(self)
        self.blueLine.resize(400, 40)
        self.blueLine.move(75, 459)

        self.rgb = QLabel(self)
        self.rgb.resize(80, 40)
        self.rgb.move(240, 504)
        self.rgb.setText("RGB:")

        self.rgbLine = QLineEdit(self)
        self.rgbLine.resize(400, 40)
        self.rgbLine.move(75, 549)

    def readimg(self):
        path = self.filename.text()
        try:
            img = Image.open(path)
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
            self.redLine.setText(red)
            self.greenLine.setText(green)
            self.blueLine.setText(blue)
            self.rgbLine.setText(all)
        except Exception:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = SteganoIMGRead()
    test.show()
    sys.exit(app.exec())
