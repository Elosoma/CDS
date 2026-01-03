from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton

class CharacterList(QWidget):
    def __init__(self, controller, parent):
        super().__init__()
        self.controller = controller
        self.parent_tab = parent

        self.list = QListWidget()
        self.new_btn = QPushButton("➕ Nuevo personaje")

        self.list.itemDoubleClicked.connect(self.open_character)
        self.new_btn.clicked.connect(self.new_character)

        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.new_btn)
        self.setLayout(layout)

    def refresh(self):
        self.list.clear()
        characters = self.controller.get_user_characters()

        for c in characters:
            self.list.addItem(f"{c.name} (Nivel {c.level} {c.class_index})")
            self.list.item(self.list.count() - 1).setData(1, c.id)

    def open_character(self, item):
        character_id = item.data(1)
        self.parent_tab.show_detail(character_id)

    def new_character(self):
        self.parent_tab.show_form()
