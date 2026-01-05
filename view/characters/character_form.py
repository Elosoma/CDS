'''Formulario de creación de personaje'''
from PyQt6.QtWidgets import (
    QWidget, QTextEdit, QPushButton, QFormLayout, 
    QLineEdit, QSpinBox, QComboBox, QMessageBox
)

# Referencias.
#from view.characters.character_tab import CharacterTab
from model.user_db import (DatabaseManager, Characters)
from model.api_2014 import DnDAPI


class CharacterForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.db = DatabaseManager()
        self.api = DnDAPI()
        self.parent_tab = parent
        self.character_id = None

        self.build_ui()
        self.load_selectors()

    def build_ui(self):
        layout = QFormLayout()

        self.name = QLineEdit()
        self.race = QComboBox()
        self.subrace = QComboBox()
        self.subrace.setEnabled(False)

        self.char_class = QComboBox()
        self.background = QComboBox()
        self.alignment = QComboBox()

        self.story = QTextEdit()

        layout.addRow("Name", self.name)
        layout.addRow("Race", self.race)
        layout.addRow("Subrace", self.subrace)
        layout.addRow("Class", self.char_class)

        self.stats = {}
        for stat in ["str", "dex", "con", "int", "wis", "cha"]:
            spin = QSpinBox()
            spin.setRange(1, 20)
            spin.setValue(10)
            self.stats[stat] = spin
            layout.addRow(stat.upper(), spin)

        
        layout.addRow("Background", self.background)
        layout.addRow("Alingment", self.alignment)
        layout.addRow("History/Notes", self.story)

        self.save_btn = QPushButton("💾 Guardar")
        self.cancel_btn = QPushButton("❌ Cancelar")

        self.save_btn.clicked.connect(self.save_character)
        self.cancel_btn.clicked.connect(self.parent_tab.show_list)

        layout.addRow(self.save_btn, self.cancel_btn)
        self.setLayout(layout)

    def load_races(self):
        self.race.clear()
        data:dict = self.api.get_races()

        for r in data["results"]:
            self.race.addItem(r["name"], r["index"])

        self.race.currentIndexChanged.connect(self.load_subraces)

    def load_subraces(self):
        self.subrace.clear()
        self.subrace.setEnabled(False)

        race_index = self.race.currentData()
        if race_index is None:
            return
        race:dict = self.api.get_race(f'{race_index}')

        subraces = race.get("subraces", [])
        if not subraces:
            return

        self.subrace.setEnabled(True)
        for s in subraces:
            self.subrace.addItem(s["name"], s["index"])

    def load_classes(self):
        self.char_class.clear()
        data = self.api.get_classes()

        for c in data["results"]:
            self.char_class.addItem(c["name"], c["index"])

    def load_backgrounds(self):
        self.background.clear()
        data = self.api.get_backgrounds()

        for b in data["results"]:
            self.background.addItem(b["name"], b["index"])

    def load_alignments(self):
        self.alignment.clear()
        data = self.api.get_alignments()

        for a in data["results"]:
            self.alignment.addItem(a["name"], a["index"])

    def load_selectors(self):
        self.load_races()
        self.load_classes()
        self.load_backgrounds()
        self.load_alignments()

    def save_character(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "El nombre es obligatorio")
            return

        character = Characters(
            user_id=self.parent_tab.user,
            name=self.name.text(),
            race_index=self.race.currentData(),
            subrace_index=self.subrace.currentData(),
            class_index=self.char_class.currentData(),
            subclass_index=self.subrace.currentData(),
            level=1,
            hit_points=10,
            background_index=self.background.currentData(),
            background_story=self.story.toPlainText(),
            alignment=self.alignment.currentData()
        )

        self.db.add_character(character)
        self.parent_tab.show_list()











    def clear_form(self):
        self.name.clear()
        self.race.setCurrentIndex(0)
        self.char_class.setCurrentIndex(0)
        self.alignment.setCurrentIndex(0)
        self.background.setCurrentIndex(0)
        self.story.clear()

    def load_character(self, character_id=None):
        self.character_id = character_id
        self.clear_form()


