from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys

from view import ViewWidget

class Application(QMainWindow):
    '''Crea la aplicación y le situa el Widget central de contenido'''
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('utils/log.png'))
        self.init = ViewWidget(self)
        self.setCentralWidget(self.init)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("utils/style_sheet.css","r") as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    
    window = Application()
    window.show()
    sys.exit(app.exec())
