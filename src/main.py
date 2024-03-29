from display import MainWindow

import sys
import os

import qdarktheme
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import ( QGuiApplication, QIcon )

# Workaround to show icon on windows taskbar.
# Took from https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
import ctypes
myappid = 'mutemini.booktranslatorapp'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
os.environ['MEMORY_ALLOCATED'] = '0.1'

if __name__ == '__main__':

    app = QApplication(sys.argv)

    qdarktheme.setup_theme("auto")
    
    max_size = QGuiApplication.primaryScreen().availableSize()
    max_size.scale(800, 600, Qt.AspectRatioMode.KeepAspectRatio)

    window = MainWindow()
    window.resize(max_size)
    window.setWindowTitle('Book Wiper')
    window.setWindowIcon(QIcon('icon.ico'))
    window.show()

    sys.exit(app.exec())