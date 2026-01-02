'''Archivo ejecutable, actua como una raíz para imports y referencias'''
# Librerias
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# Referencias
from view.api_explorer.content_explorer import content_list
from model.api_2014 import DnDAPI


class Application(QMainWindow):
    def __init__(self):
        super().__init__()

        # Detalles de pestaña.
        self.setWindowTitle("CDS")
        self.resize(1000, 700)

        self.api = DnDAPI()
        self.explorer = content_list(self.api)

        self.setCentralWidget(self.explorer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
