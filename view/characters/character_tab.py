'''Pestaña con tabs que cambian entre diferentes datos de personajes.'''
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QStackedWidget)

# Referencias
from view.characters.character_list import CharacterList
from view.characters.character_detail import CharacterDetail
from view.characters.character_form import CharacterForm
from model.user_db import DatabaseManager
from model.api_2014 import DnDAPI

class CharacterTab(QWidget):
    def __init__(self, database, api, current_user = 1):
        '''Crea los diferentes tabs con la información de los personajes y cambia entre pestañas.'''
        super().__init__()
        self.db:DatabaseManager = database
        self.api:DnDAPI = api
        self.user = current_user

        self.stack = QStackedWidget()

        self.list_view = CharacterList(database, self)
        self.detail_view = CharacterDetail(database, self)
        self.form_view = CharacterForm(self)

        self.stack.addWidget(self.list_view)
        self.stack.addWidget(self.detail_view)
        self.stack.addWidget(self.form_view)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.show_list()

    def show_list(self):
        self.list_view.refresh()
        self.stack.setCurrentWidget(self.list_view)

    def show_detail(self, character_id):
        self.detail_view.load_character(character_id)
        self.stack.setCurrentWidget(self.detail_view)

    def show_form(self, character_id=None):
        self.form_view.load_character(character_id)
        self.stack.setCurrentWidget(self.form_view)
