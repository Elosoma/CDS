from PyQt6.QtWidgets import (
    QWidget, QWidget, QVBoxLayout, 
    QTabWidget, QTabWidget
)

from model import DnDAPI
from view.contenet_view.content_detail import ContentDetail
from controller import (
    format_class, format_race, format_spell,
    format_skill, format_equipment
)
        

class ContentWidget(QWidget):
    '''Muestra listas con el contenido de la api, este puede ser presionado para mostrar una descripción'''
    def __init__(self, api:DnDAPI, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        resources = {
            "Classes": (api.get_classes, api.get_class, format_class),
            "Races": (api.get_races, api.get_race, format_race),
            "Spells": (api.get_spells, api.get_spell, format_spell),
            "Skills": (api.get_skills, api.get_skill, format_skill),
            "Equipment": (api.get_equipment, api.get_equip, format_equipment),
        }
        
        # Bucle de creación de tabs, para cada uno selecciona el nombre, metodos de la api y formato.
        for name, (list_func, detail_func, formatter) in resources.items():
            tab = ContentDetail(api, list_func, detail_func, formatter)
            self.tabs.addTab(tab, name)
