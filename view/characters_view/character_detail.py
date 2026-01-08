from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QMessageBox,
    QPushButton, QTextEdit, QHBoxLayout
)

from controller import LoadCharacterSheet
from model import DatabaseManager


class CharacterDetail(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.api = parent.api
        self.parent_tab = parent
        self.character_id = None

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        self.edit_btn = QPushButton("✏️ Edit")
        self.delete_btn = QPushButton("🗑️ Delete")
        self.back_btn = QPushButton("⬅️ Back")

        self.edit_btn.clicked.connect(self.edit_character)
        self.delete_btn.clicked.connect(self.delete_character)
        self.back_btn.clicked.connect(self.parent_tab.show_list)

        buttons = QHBoxLayout()
        buttons.addWidget(self.edit_btn)
        buttons.addWidget(self.delete_btn)
        buttons.addWidget(self.back_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addLayout(buttons)
        self.setLayout(layout)

    def load_character(self, character_id):
        self.character_id = character_id
        character = self.db.get_character(character_id)
        sheet = LoadCharacterSheet(self.db, self.api, character_id)

        if not character:
            self.text.setPlainText("")
            return

        self.text.clear()
        lines = sheet.get_main_format()
        self.text.setPlainText(lines)
    
    def edit_character(self):
        self.parent_tab.show_form(self.character_id)

    def delete_character(self):
        reply = QMessageBox.question(
            self,
            "Delete character",
            "Are you sure you want to delete this character?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_character(self.character_id)
            self.parent_tab.show_list()
