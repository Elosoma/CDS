from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from view.characters.character_list import CharacterList
from view.characters.character_detail import CharacterDetail
from view.characters.character_form import CharacterForm

class CharacterTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.stack = QStackedWidget()

        self.list_view = CharacterList(controller, self)
        self.detail_view = CharacterDetail(controller, self)
        self.form_view = CharacterForm(controller, self)

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
