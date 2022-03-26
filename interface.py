import sys
import os
import re
from PyQt5 import QtWidgets, uic, QtCore


def convert_string(string):
    # Remove any line with a { or }
    string = re.sub(r".*(\{|\}).*(\n|\Z)", "", string)
    # Remove unnessary newlines
    string = re.sub(r"\n([^:])", r"\1", string)
    return string


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Load ui
        uic.loadUi(open("Gui.ui"), self)
        self.setWindowTitle("MT940 Converter")

        # Button functions
        self.fileselectbrowsebutton.clicked.connect(self.file_select)
        self.convertbutton.clicked.connect(self.convert_and_save)
        # self.clear_button.clicked.connect(self.textedit.clear)
        # self.add_button.clicked.connect(self.add_button_clicked)

    def file_select(self):
        """Opens File Dialog box to select file. Displays path/to/file as well."""
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            filter="MT940 files(*.940)")
        self.fileselectlineEdit.setText(self.filename)
        self.donelabel_2.setText("")

    def convert_and_save(self):
        with open(self.filename, 'r') as f:
            content = f.read()

        content = convert_string(content)
        path, ext = os.path.splitext(self.filename)
        with open(path + " converted" + ext, 'w') as f:
            f.write(content)

        self.donelabel_2.setText("Done!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())
