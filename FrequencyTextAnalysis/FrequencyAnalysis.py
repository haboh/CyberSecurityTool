# ╔══╦═══╦═══╦═══╦╗╔╦═══╦╗─╔╦══╦╗╔╦════╦═══╦══╗╔══╦════╦══╦╗─╔╦══╦╗─╔╗╔╦══╦══╦══╗
# ║╔═╣╔═╗║╔══╣╔═╗║║║║╔══╣╚═╝║╔═╣║║╠═╗╔═╣╔══╩═╗║║╔═╩═╗╔═╣╔╗║╚═╝║╔╗║║─║║║║╔═╩╗╔╣╔═╝
# ║╚═╣╚═╝║╚══╣║─║║║║║╚══╣╔╗─║║─║╚╝║─║║─║╚══╗─║╚╝║───║║─║╚╝║╔╗─║╚╝║║─║╚╝║╚═╗║║║╚═╗
# ║╔═╣╔╗╔╣╔══╣║╔╝║║║║╔══╣║╚╗║║─╚═╗║─║║─║╔══╝─║╔╗║───║║─║╔╗║║╚╗║╔╗║║─╚═╗╠═╗║║║╚═╗║
# ║║─║║║║║╚══╣╚╝─║╚╝║╚══╣║─║║╚═╗╔╝║─║║─║╚══╦═╝║║╚═╗─║║─║║║║║─║║║║║╚═╗╔╝╠═╝╠╝╚╦═╝║
# ╚╝─╚╝╚╝╚═══╩═══╩══╩═══╩╝─╚╩══╝╚═╝─╚╝─╚═══╩══╝╚══╝─╚╝─╚╝╚╩╝─╚╩╝╚╩══╝╚═╩══╩══╩══╝ by haboh

from PyQt5.QtWidgets import QPushButton, QLabel, QApplication, QMainWindow, QHBoxLayout, QLineEdit, QCheckBox
from PyQt5 import QtGui, QtWidgets
from FrequencyTextAnalysis.FrequencyAnalysisUi import Ui_MainWindow
import sys

LETTERS_IN_ALPHABET = 26
ROWS_IN_GRID = 7
COLUMNS_IN_GRID = 4


def safety_increase_in_dictionary(d, k):
    d[k] = 1 if k not in d else d[k] + 1


class FrequencyAnalysisMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Text frequency analysis')
        self.changeWidgets = {}

        # Fill grid with widgets
        for i in range(LETTERS_IN_ALPHABET):
            letter = chr(ord('a') + i)
            new_layout = QHBoxLayout()

            # Create label with the only one letter
            label = QLabel(letter)
            label.setMinimumSize(20, 15)
            label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Normal))
            new_layout.addWidget(label)

            # Create input place
            line_edit = QLineEdit()
            new_layout.addWidget(line_edit)

            # Create checkbox with need of change
            checkbox = QCheckBox('Change')
            new_layout.addWidget(checkbox)

            # Make little margin on the right
            vertical_spacer = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
            new_layout.addItem(vertical_spacer)

            # Add layout to grid
            self.changeWidgets[letter] = (line_edit, checkbox)
            x, y = i % ROWS_IN_GRID, i / ROWS_IN_GRID
            self.gridWithLetters.addLayout(new_layout, x, y)

        # Create two buttons in the right corner
        self.analyzeButton = QPushButton('Analyze')
        self.commitChangesButton = QPushButton('Commit changes')
        self.gridWithLetters.addWidget(self.analyzeButton, ROWS_IN_GRID - 2,
                                       COLUMNS_IN_GRID - 1)
        self.gridWithLetters.addWidget(self.commitChangesButton, ROWS_IN_GRID - 1,
                                       COLUMNS_IN_GRID - 1)

        # Connect buttons with necessary methods
        self.analyzeButton.clicked.connect(self.process_analyze)
        self.commitChangesButton.clicked.connect(self.process_commit)

    def process_analyze(self):
        # Collect information
        text_for_analyze = self.sourceText.toPlainText()
        letters = {}
        letters_amount = 0
        for c in text_for_analyze:
            if c.isalpha():
                safety_increase_in_dictionary(letters, c)
                letters_amount += 1

        # Display information
        self.lettersAmount.clear()
        for letter, amount in sorted(letters.items()):
            percent = round(float(amount / letters_amount * 100), 2)
            self.lettersAmount.addItem(letter + ' - ' + str(percent) + '%')

    def process_commit(self):
        changes = {}
        for letter, widgets in self.changeWidgets.items():
            if widgets[1].isChecked():
                changing_letter = widgets[0].text()
                changes[letter] = changing_letter
        self.update_modified_text(changes)

    def update_modified_text(self, changes):
        new_text = ''
        for c in self.sourceText.toPlainText():
            new_text += changes[c] if c.isalpha() and c in changes else c
        self.ModifiedText.setPlainText(new_text)


def main():
    application = QApplication(sys.argv)
    widget = FrequencyAnalysisMainWindow()
    widget.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
