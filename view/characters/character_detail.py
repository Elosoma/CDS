from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout

class CharacterDetail(QWidget):
    def __init__(self, controller, parent):
        super().__init__()
        self.controller = controller
        self.parent_tab = parent
        self.character_id = None

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        self.edit_btn = QPushButton("✏️ Editar")
        self.delete_btn = QPushButton("🗑️ Eliminar")
        self.back_btn = QPushButton("⬅️ Volver")

        self.edit_btn.clicked.connect(self.edit)
        self.delete_btn.clicked.connect(self.delete)
        self.back_btn.clicked.connect(self.parent_tab.show_list)

        btns = QHBoxLayout()
        btns.addWidget(self.edit_btn)
        btns.addWidget(self.delete_btn)
        btns.addWidget(self.back_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addLayout(btns)
        self.setLayout(layout)

    def load_character(self, character_id):
        self.character_id = character_id
        character = self.controller.get_character(character_id)

        self.text.setPlainText(self.controller.build_character_sheet(character))

    def edit(self):
        self.parent_tab.show_form(self.character_id)

    def delete(self):
        self.controller.delete_character(self.character_id)
        self.parent_tab.show_list()
