from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QMessageBox,
    QPushButton, QTextEdit, QHBoxLayout, QTabWidget
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
        
        self.tabs = QTabWidget()
        self.tabs.addTab(self.general_tab(), "General")
        self.tabs.addTab(self.class_tab(), "Class")
        self.tabs.addTab(self.race_tab(), "Race")

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
        layout.addWidget(self.tabs)
        layout.addLayout(buttons)
        self.setLayout(layout)

    def load_character(self, character_id):
        self.character_id = character_id
        character = self.db.get_character(character_id)
        self.sheet = LoadCharacterSheet(self.db, self.api, character_id)

        if not character:
            self.general_text.setPlainText("Eror, personaje no existente.")
            self.class_text.setPlainText("")
            self.race_text.setPlainText("")
            return

        self.general_text.setPlainText(self.sheet.get_main_format())
        self.class_text.setPlainText(self.sheet.get_classlvl_format())
        self.race_text.setPlainText(self.sheet.get_racial_format())

    def general_tab(self):
        layout = QVBoxLayout()
        widget = QWidget()

        self.general_text = QTextEdit()
        self.general_text.setReadOnly(True)
        layout.addWidget(self.general_text)

        widget.setLayout(layout)
        return widget
    
    def class_tab(self):
        layout = QVBoxLayout()
        widget = QWidget()

        self.class_text = QTextEdit()
        self.class_text.setReadOnly(True)
        layout.addWidget(self.class_text)

        widget.setLayout(layout)
        return widget
    
    def race_tab(self):
        layout = QVBoxLayout()
        widget = QWidget()
        
        self.race_text = QTextEdit()
        self.race_text.setReadOnly(True)
        layout.addWidget(self.race_text)

        widget.setLayout(layout)
        return widget
    
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
