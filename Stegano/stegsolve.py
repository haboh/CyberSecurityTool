# ╔══╦════╦═══╦═══╦══╦══╦╗─╔╗╔╦═══╗
# ║╔═╩═╗╔═╣╔══╣╔══╣╔═╣╔╗║║─║║║║╔══╝
# ║╚═╗─║║─║╚══╣║╔═╣╚═╣║║║║─║║║║╚══╗
# ╚═╗║─║║─║╔══╣║╚╗╠═╗║║║║║─║╚╝║╔══╝
# ╔═╝║─║║─║╚══╣╚═╝╠═╝║╚╝║╚═╬╗╔╣╚══╗
# ╚══╝─╚╝─╚═══╩═══╩══╩══╩══╝╚╝╚═══╝ by haboh

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from Stegano.steganoUI import Ui_Stegano
from PIL.ImageQt import ImageQt

from PIL import Image
import sys


# This function takes PIL image and convert it into the QPixMap
def convert_image_to_pix_map(im):
    im = im.convert("RGBA")
    qim = ImageQt(im)
    pix = QPixmap.fromImage(qim)
    return pix


# Main class
class SteganoMainWindow(QMainWindow, Ui_Stegano, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Stegano')
        self.PixMap = QLabel(self)
        self.PixMap.move(20, 20)
        self.PixMap.resize(300, 300)
        # All buttons in the application
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
        # Connect buttons to the actions when they are chosen
        for button in self.buttons:
            button.toggled.connect(self.process_buttons)
        # Make button with file choice
        self.pushButton.clicked.connect(self.file)
        self.file_name, self.image, self.pixels, self.width, self.height = None, None, None, None, None
        self.file()

    # This function calls QFileDialog and propose to choose file
    def file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select image',
                                                '/', "Image files (*.jpg)")[0]
        if file_name != '':
            for button in self.buttons:
                button.setEnabled(True)
            self.file_name = file_name
            self.image = Image.open(self.file_name)
            self.pixels = self.image.load()
            self.width, self.height = self.image.size
            self.PixMap.resize(self.width, self.height + 60)
            self.process_buttons()
            self.verticalLayoutWidget.move(self.width + 50, 30)
        else:
            for button in self.buttons:
                button.setEnabled(False)

    def process_buttons(self):
        # Process all buttons
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

    # Make picture negative
    def get_xor_picture(self):
        im = self.image.copy()
        pix = im.load()
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = pix[i, j]
                r, g, b = 255 - r, 255 - g, 255 - b
                pix[i, j] = (r, g, b)
        return im

    # This function makes white-black picture by one of the RGB colors, if it is half completed
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

    # This function makes one of the RGB colors full(255)
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
    ex = SteganoMainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
