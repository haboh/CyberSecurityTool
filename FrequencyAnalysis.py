from PyQt5.QtWidgets import QPushButton, QPlainTextEdit, QLabel, QApplication, QWidget, \
    QMainWindow, QDialog, QHBoxLayout, QLineEdit, QCheckBox
from PyQt5 import QtGui, QtWidgets
from FrequencyAnalysisUi import Ui_MainWindow
import sys

LETTERS_IN_ALPHABET = 26
ROWS_IN_GRID = 7
COLUMNS_IN_GRID = 4


def safety_increase_in_dictionary(d, k):
    d[k] = 1 if k not in d else d[k] + 1


class FrequencyAnalysis(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Text frequency analysis')
        self.changeWidgets = {}

        for i in range(LETTERS_IN_ALPHABET):
            letter = chr(ord('a') + i)
            new_layout = QHBoxLayout()

            label = QLabel(letter)
            label.setMinimumSize(20, 15)
            label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Normal))
            new_layout.addWidget(label)

            line_edit = QLineEdit()
            new_layout.addWidget(line_edit)

            checkbox = QCheckBox('Lock')
            new_layout.addWidget(checkbox)

            vertical_spacer = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
            new_layout.addItem(vertical_spacer)

            self.changeWidgets[letter] = (line_edit, checkbox)
            x, y = i % ROWS_IN_GRID, i / ROWS_IN_GRID
            self.gridWithLetters.addLayout(new_layout, x, y)

        self.analyzeButton = QPushButton('Analyze')
        self.commitChangesButton = QPushButton('Commit changes')
        self.gridWithLetters.addWidget(self.analyzeButton, ROWS_IN_GRID - 2,
                                       COLUMNS_IN_GRID - 1)
        self.gridWithLetters.addWidget(self.commitChangesButton, ROWS_IN_GRID - 1,
                                       COLUMNS_IN_GRID - 1)

        self.analyzeButton.clicked.connect(self.process_analyze)
        self.commitChangesButton.clicked.connect(self.process_commit)

    def process_analyze(self):
        text_for_analyze = self.sourceText.toPlainText()
        letters = {}
        letters_amount = 0
        for c in text_for_analyze:
            if c.isalpha():
                safety_increase_in_dictionary(letters, c)
                letters_amount += 1
        self.lettersAmount.clear()
        for letter, amount in sorted(letters.items()):
            percent = round(float(amount / letters_amount * 100), 2)
            self.lettersAmount.addItem(letter + ' - ' + str(percent) + '%')

    def process_commit(self):
        pass


if __name__ == '__main__':
    application = QApplication(sys.argv)
    widget = FrequencyAnalysis()
    widget.show()
    sys.exit(application.exec_())
