# ╔══╦════╦═══╦═══╦══╦══╦╗─╔╗╔╦═══╗
# ║╔═╩═╗╔═╣╔══╣╔══╣╔═╣╔╗║║─║║║║╔══╝
# ║╚═╗─║║─║╚══╣║╔═╣╚═╣║║║║─║║║║╚══╗
# ╚═╗║─║║─║╔══╣║╚╗╠═╗║║║║║─║╚╝║╔══╝
# ╔═╝║─║║─║╚══╣╚═╝╠═╝║╚╝║╚═╬╗╔╣╚══╗
# ╚══╝─╚╝─╚═══╩═══╩══╩══╩══╝╚╝╚═══╝ by haboh

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from steganoUI import Ui_Stegano
from PIL.ImageQt import ImageQt

from PIL import Image
import sys


def convert_image_to_pix_map(im):
    im = im.convert("RGBA")
    qim = ImageQt(im)
    pix = QPixmap.fromImage(qim)
    return pix


class MainWindow(QMainWindow, Ui_Stegano):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PixMap = QLabel(self)
        self.PixMap.move(20, 20)
        self.PixMap.resize(300, 300)
        self.buttons = [
            self.DefaultButton,
            self.XORButton,
            self.RedPlaneButton,
            self.GreenPlaneButton,
            self.BluePlaneButton,
            self.FullRedButton,
            self.FullGreenButton,
            self.FullBlueButton,
        ]
        self.DefaultButton.setChecked(True)
        for button in self.buttons:
            button.toggled.connect(self.process_buttons)
        self.pushButton.clicked.connect(self.file)
        self.file_name, self.image, self.pixels, self.width, self.height = None, None, None, None, None
        self.file()

    def file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select image',
                                            '/', "Image files (*.jpg)")[0]
        self.file_name = file_name
        self.image = Image.open(self.file_name)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.PixMap.resize(self.width + 200, self.height + 200)
        self.process_buttons()
        self.verticalLayoutWidget.move(self.width + 50, 100)

    def process_buttons(self):
        for button in self.buttons:
            if button.isChecked():
                if button.text() == 'Default':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.image))
                if button.text() == 'XOR (Negative)':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_xor_picture()))
                if button.text() == 'Red Plane':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_plane_picture(0)))
                if button.text() == 'Green Plane':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_plane_picture(1)))
                if button.text() == 'Blue Plane':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_plane_picture(2)))
                if button.text() == 'Full Red':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_full_picture(0)))
                if button.text() == 'Full Green':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_full_picture(1)))
                if button.text() == 'Full Blue':
                    self.PixMap.setPixmap(convert_image_to_pix_map(self.get_full_picture(2)))

    def get_xor_picture(self):
        im = self.image.copy()
        pix = im.load()
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = pix[i, j]
                r, g, b = 255 - r, 255 - g, 255 - b
                pix[i, j] = (r, g, b)
        return im

    def get_plane_picture(self, k):
        im = self.image.copy()
        pix = im.load()
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = pix[i, j]
                if pix[i, j][k] >= 127:
                    r, g, b = 0, 0, 0
                else:
                    r, g, b = 255, 255, 255

                pix[i, j] = (r, g, b)
        return im

    def get_full_picture(self, k):
        im = self.image.copy()
        pix = im.load()
        for i in range(self.width):
            for j in range(self.height):
                r = list(pix[i, j])
                r[k] = 255
                pix[i, j] = (r[0], r[1], r[2])
        return im


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
