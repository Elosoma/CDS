'''Archivo ejecutable, actua como una raíz para imports y referencias'''
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from view import ViewWidget


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1000, 700)
        self.setWindowTitle("CDS")
   
        self.explorer = ViewWidget()
        self.setCentralWidget(self.explorer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
