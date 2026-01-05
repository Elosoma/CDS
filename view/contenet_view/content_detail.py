from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QListWidget, 
    QTextEdit, QMessageBox, QWidget
)


class ContentDetail(QWidget):
    '''Pestaña de contenido detallado, muestra los detalles del contenido seleccionado.'''
    def __init__(self, api, list_func, detail_func, formatter, parent=None):
        super().__init__(parent)

        # Variables de clase, api, funciones para la lista y el detalle y formato.
        self.api = api
        self.list_func = list_func
        self.detail_func = detail_func
        self.formatter = formatter

        # Layout horizontal y elementos en su interior, lista y descripción.
        self.layout:QHBoxLayout = QHBoxLayout(self)
        self.list_widget = QListWidget()
        self.detail_text = QTextEdit()
        self.detail_text.setReadOnly(True)

        self.layout.addWidget(self.list_widget, 1)
        self.layout.addWidget(self.detail_text, 2)

        # Conector para alternar datos de las descripciones.
        self.list_widget.itemClicked.connect(self.load_detail)
        self.load_list()

    def load_list(self):
        '''Obtiene y muestra una lista de...'''
        data:dict = self.list_func()
        if data is None:
            # En caso de haber un error en la api o la conexión con esta, devuelve None.
            QMessageBox.critical(self, "Error", "No se pudo cargar la lista")
            return

        # Crea una lista de... que son seleccionables para desplegar una descripción.
        self.list_widget.clear()
        for item in data.get("results", []):
            self.list_widget.addItem(item["name"])
            self.list_widget.item(
                self.list_widget.count() - 1
            ).setData(Qt.ItemDataRole.UserRole, item["index"])

    def load_detail(self, item):
        '''Utiliza el formato para mostrar los detalles del elemento...'''
        index = item.data(Qt.ItemDataRole.UserRole)
        data = self.detail_func(index)

        if data is None:
            QMessageBox.critical(self, "Error", "No se pudo cargar el detalle")
            return

        self.detail_text.setPlainText(self.formatter(data))
