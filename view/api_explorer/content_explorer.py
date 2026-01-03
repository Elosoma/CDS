'''Pantalla de contenido, recoge los datos de la api y los muestra.'''
# Librerias
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QListWidget, QTextEdit, 
    QMessageBox, QWidget, QVBoxLayout, QTabWidget, QTabWidget)

# Referencias
from model.api_2014 import DnDAPI
from .description_formater import (
    format_class, format_race, format_spell,
    format_skill, format_equipment)


class content_detail(QWidget):
    def __init__(self, api, list_func, detail_func, formatter, parent=None):
        '''
        :param api: Clase api derivada de api_2014
        :param list_func: Solicitud a la api de una lista de...
        :param detail_func: Solicitud a la api de la descripción de...
        '''
        super().__init__(parent)

        # Variables de clase.
        self.api = api
        self.list_func = list_func
        self.detail_func = detail_func
        self.formatter = formatter
        self.layout:QHBoxLayout = QHBoxLayout(self)

        # Pestaña de lista y descripción.
        self.list_widget = QListWidget()
        self.detail_text = QTextEdit()
        self.detail_text.setReadOnly(True)

        self.layout.addWidget(self.list_widget, 1)
        self.layout.addWidget(self.detail_text, 2)

        # Conectores para alternar datos de descripciones.
        self.list_widget.itemClicked.connect(self.load_detail)
        self.load_list()

    # <---> <---> <---> <---> <---> <--->

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

    # <---> <---> <---> <---> <---> <--->

    def load_detail(self, item):
        '''Utiliza el formato para mostrar los detalles del elemento...'''
        index = item.data(Qt.ItemDataRole.UserRole)
        data = self.detail_func(index)

        if data is None:
            QMessageBox.critical(self, "Error", "No se pudo cargar el detalle")
            return

        self.detail_text.setPlainText(self.formatter(data))



class content_list(QWidget):
    def __init__(self, api:DnDAPI, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Pestañas y sus metodos asociados.
        resources = {
            "Classes": (api.get_classes, api.get_class, format_class),
            "Races": (api.get_races, api.get_race, format_race),
            "Spells": (api.get_spells, api.get_spell, format_spell),
            "Skills": (api.get_skills, api.get_skill, format_skill),
            "Equipment": (api.get_equipment, api.get_equip, format_equipment),
        }

        # Bucle de creación de tabs.
        for name, (list_func, detail_func, formatter) in resources.items():
            tab = content_detail(api, list_func, detail_func, formatter)
            self.tabs.addTab(tab, name)
