'''Archivo ejecutable, actua como una raíz para imports y referencias'''
# Librerias
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# Referencias
from view.ui import GestorRol
from model.api_2014 import DnDAPI


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        # Detalles de pestaña.
        self.setWindowTitle("CDS")
        self.resize(1000, 700)

        self.api = DnDAPI()
        self.explorer = GestorRol(self.api)

        self.setCentralWidget(self.explorer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
