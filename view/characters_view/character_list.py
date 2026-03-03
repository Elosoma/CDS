'''Pestaña, lista de personajes del usuario.'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,QListWidget, 
    QPushButton, QListWidgetItem, QLineEdit
)

from model import DatabaseManager


class CharacterList(QWidget):
    '''Muestra la lista de personajes de un usuario y permite crear nuevos u acceder a la pestaña con sus datos.'''
    def __init__(self, db:DatabaseManager, parent):
        '''Crea la lista y el botón de creación de personaje.'''
        super().__init__()
        self.db = db
        self.parent_tab = parent

        layout = QVBoxLayout()

        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("Buscar nombre...")
        layout.addWidget(self.buscador)

        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.open_character)
        layout.addWidget(self.list)

        self.new_btn = QPushButton("➕ New character")
        self.new_btn.clicked.connect(self.new_character)
        layout.addWidget(self.new_btn)

        self.buscador.textChanged.connect(self.search_bar)
        self.setLayout(layout)

    def __get_list(self):
        return self.db.get_user_characters(self.parent_tab.user)

    def search_bar(self, texto):
        texto = texto.lower()
        filtrados = [
            nombre for nombre in self.__get_list()
            if texto in nombre.name.lower()
        ]
        self.refresh(filtrados)

    def refresh(self, characters=0):
        '''Limpia la lista y la refresca con datos actualizados.'''
        self.list.clear()
        if characters == 0: characters = self.__get_list()

        for ch in characters:
            item = QListWidgetItem(
                f"{ch.name} (Nivel {ch.level} {ch.class_index})"
            )
            item.setData(Qt.ItemDataRole.UserRole, ch.object_id)
            self.list.addItem(item)

    def open_character(self, item:QListWidgetItem):
        '''Abre la pestaña con los detalles del personaje seleccionado.'''
        character_id = item.data(Qt.ItemDataRole.UserRole)
        self.parent_tab.show_detail(character_id)

    def new_character(self):
        '''Llama al metodo que cambia la pestaña al formulario de creación.'''
        self.parent_tab.show_form()
