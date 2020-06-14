from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

import pages

# Only needed for access to command line arguments
from sys import argv


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, tf_path, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("TF2 Customization Manager")
        self.resize(900, 400)

        main_window_ptr = self

        main_vbox = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(main_vbox)

        # Stack
        stack = QStackedWidget()

        hud_layout = QVBoxLayout()
        hud_page = QWidget()
        hud_page.setLayout(hud_layout)

        cfg_layout = QVBoxLayout()
        cfg_page = QWidget()
        cfg_page.setLayout(cfg_layout)

        sounds_page = pages.SoundsPage(tf_path, main_window_ptr)

        stack.addWidget(hud_page)
        stack.addWidget(cfg_page)
        stack.addWidget(sounds_page)

        # Stack Switcher
        # TBH stack switcher is awful. TODO: Make new good stack switcher
        stack_switcher = QHBoxLayout()
        stack_switcher.setAlignment(Qt.AlignCenter)

        hud_page_btn = QPushButton('HUD')
        cfg_page_btn = QPushButton('CFG')
        sounds_page_btn = QPushButton('Sounds')

        hud_page_btn.clicked.connect(lambda: stack.setCurrentIndex(0))
        cfg_page_btn.clicked.connect(lambda: stack.setCurrentIndex(1))
        sounds_page_btn.clicked.connect(lambda: stack.setCurrentIndex(2))

        stack_switcher.addWidget(hud_page_btn)
        stack_switcher.addWidget(cfg_page_btn)
        stack_switcher.addWidget(sounds_page_btn)

        main_vbox.addLayout(stack_switcher)
        main_vbox.addWidget(stack)

        self.setCentralWidget(central_widget)


class RequestTFPathDialog(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setWindowTitle('TF path is not found')
        self.resize(500, 50)

        self.tf_path = ''

        main_vbox = QVBoxLayout()
        self.setLayout(main_vbox)

        label = QLabel("Sorry but this program couldn't found path to TF2. Please point it.")

        self.line_edit = QLineEdit()
        select_path_btn = QPushButton('Select TF2 path')
        ok_btn = QPushButton('OK')

        select_path_btn.clicked.connect(self.on_select_tf_path_btn_clicked)
        ok_btn.clicked.connect(self.on_ok_btn_clicked)

        hbox = QHBoxLayout()
        hbox.addWidget(self.line_edit)
        hbox.addWidget(select_path_btn)
        hbox.addWidget(ok_btn)

        main_vbox.addWidget(label)
        main_vbox.addLayout(hbox)

    def on_select_tf_path_btn_clicked(self):
        path = QFileDialog.getExistingDirectory(None, 'TF path selection')
        self.line_edit.setText(path)

    def on_ok_btn_clicked(self):
        try:
            if 'tf' in os.listdir(self.line_edit.text()):
                self.tf_path = self.line_edit.text()
                self.close()
        except FileNotFoundError:
            dialog = QErrorMessage(self)
            dialog.showMessage("Error! Wrong directory!")
            dialog.exec_()


def main():
    app = QApplication(argv)

    os_name = os.name

    # Let's try to find TF2 ourselves
    try:
        default_path = ""
        if os_name == "posix":
            default_path = os.path.expanduser("~/.steam/steam/steamapps/common/Team Fortress 2/")
        elif os_name == "nt":
            raise FileNotFoundError  # I dunno 'cause I don't use windows

        os.listdir(default_path)
        tf_path = default_path
    # Looks like, we can't find TF path
    # Let's ask the user to specify it
    except FileNotFoundError:
        # Request TF path Dialog
        rtfpd = RequestTFPathDialog()
        rtfpd.exec_()
        tf_path = rtfpd.tf_path

    window = MainWindow(tf_path)
    window.show()

    # Start the event loop.
    app.exec_()


if __name__ == '__main__':
    main()
