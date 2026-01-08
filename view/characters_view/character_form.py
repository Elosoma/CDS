'''Formulario de creación de personaje'''
from PyQt6.QtWidgets import (
    QWidget, QTextEdit, QPushButton, QFormLayout, 
    QLineEdit, QSpinBox, QComboBox, QMessageBox
)

from model import (DatabaseManager, Characters, Character_stats, DnDAPI)


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
        '''Construlle la interfaz del formulario'''
        layout = QFormLayout()

        # Nombre del personaje.
        self.name = QLineEdit()
        layout.addRow("Name", self.name)

        # Selectores de raza y subraza.
        self.race = QComboBox()
        self.subrace = QComboBox()
        self.subrace.setEnabled(False)
        layout.addRow("Race", self.race)
        layout.addRow("Subrace", self.subrace)

        # Nivel del personaje.
        self.spinlvl = QSpinBox()
        self.spinlvl.setRange(1, 20)
        self.spinlvl.setValue(1)
        layout.addRow("Level", self.spinlvl)

        # Selectores de clase y subclase.
        self.char_class = QComboBox()
        self.char_subclass = QComboBox()
        self.char_subclass.setEnabled(False)
        layout.addRow("Class", self.char_class)
        layout.addRow("Subclass", self.char_subclass)

        # Estadísticas.
        self.stats = {}
        for stat in ["str", "dex", "con", "int", "wis", "cha"]:
            spin = QSpinBox()
            spin.setRange(1, 20)
            spin.setValue(10)
            self.stats[stat] = spin
            layout.addRow(stat.upper(), spin)

        # Trasfondo alineamiento y notas/historia.
        self.background = QComboBox()
        self.alignment = QComboBox()
        self.story = QTextEdit()
        layout.addRow("Background", self.background)
        layout.addRow("Alingment", self.alignment)
        layout.addRow("History/Notes", self.story)

        # Botones de guardar o cancelar y layout setter.
        self.save_btn = QPushButton("💾 Save")
        self.cancel_btn = QPushButton("❌ Cancel")
        self.save_btn.clicked.connect(self.save_character)
        self.cancel_btn.clicked.connect(self.parent_tab.show_list)
        layout.addRow(self.save_btn, self.cancel_btn)
        self.setLayout(layout)




    def load_races(self):
        '''Cargar las razas'''
        self.race.clear()
        data:dict = self.api.get_races()

        for r in data["results"]:
            self.race.addItem(r["name"], r["index"])

        self.race.currentIndexChanged.connect(self.load_subraces)

    def load_subraces(self):
        '''Cargar las subrazas'''
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
        '''Cargar las clases'''
        self.char_class.clear()
        data = self.api.get_classes()

        for c in data["results"]:
            self.char_class.addItem(c["name"], c["index"])

        self.char_class.currentIndexChanged.connect(self.load_subclasses)

    def load_subclasses(self):
        '''Cargar las subclases'''
        self.char_subclass.clear()
        self.char_subclass.setEnabled(False)

        class_index = self.char_class.currentData()
        if class_index is None:
            return
        subclass:dict = self.api.get_class(f'{class_index}')

        char_subclass = subclass.get("subclasses", [])
        if not char_subclass:
            return

        self.char_subclass.setEnabled(True)
        for s in char_subclass:
            self.char_subclass.addItem(s["name"], s["index"])




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
        self.load_subraces()
        self.load_classes()
        self.load_subclasses()
        self.load_backgrounds()
        self.load_alignments()




    def save_character(self):
        if not self.name.text().strip():
                QMessageBox.warning(self, "Error", "Name can't be blank")
                return
        
        character = Characters(
            object_id=self.character_id,
            user_id=self.parent_tab.user,
            name=self.name.text(),

            race_index=self.race.currentData(),
            subrace_index=self.subrace.currentData(),
            class_index=self.char_class.currentData(),
            subclass_index=self.char_subclass.currentData(),

            level=self.spinlvl.value(),
            hit_points=10,

            background_index=self.background.currentData(),
            background_story=self.story.toPlainText(),
            alignment=self.alignment.currentData()
        )

        char_stats = Character_stats(
            str_stat=self.stats["str"].value(),
            dex_stat=self.stats["dex"].value(),
            con_stat=self.stats["con"].value(),
            int_stat=self.stats["int"].value(),
            wis_stat=self.stats["wis"].value(),
            cha_stat=self.stats["cha"].value(),
            character_id=self.character_id
        )

        if self.character_id is None:
            self.db.add_character(character)
            last_char = self.db.get_user_characters(self.parent_tab.user)
            char_stats.character_id = last_char[-1].object_id
            self.db.add_character_stats(char_stats)
            self.parent_tab.show_list()
            return
        
        self.db.update_character(character)
        self.db.update_character_stats(char_stats)
        self.parent_tab.show_list()
        
        
        

    def clear_form(self):
        if self.character_id is None:
            self.name.clear()
            self.race.setCurrentIndex(0)
            self.subrace.setCurrentIndex(0)
            self.spinlvl.setValue(1)
            self.char_class.setCurrentIndex(0)
            self.char_subclass.setCurrentIndex(0)

            for spin in self.stats:
                spin.setValue(10)

            self.background.setCurrentIndex(0)
            self.alignment.setCurrentIndex(0)
            self.story.clear()
            return
        
        char = self.db.get_character(self.character_id)
        char_stats = self.db.get_character_stats(self.character_id)

        self.name.setText(char.name)
        self.race.setCurrentText(self.api.get_race(char.race_index)["name"])
        if char.subrace_index != None:
            try:
                self.subrace.setCurrentText(self.api.get_subrace(char.subrace_index)["name"])
            except:
                self.subrace.setCurrentIndex(0)
        else:
            self.subrace.setCurrentIndex(0)

        self.spinlvl.setValue(char.level)
        self.char_class.setCurrentText(self.api.get_class(char.class_index)["name"])
        if char.subclass_index != None:
            try:
                self.char_subclass.setCurrentText(self.api.get_subclass(char.subclass_index)["name"])
            except:
                self.char_subclass.setCurrentIndex(0)
        else:
            self.char_subclass.setCurrentIndex(0)

        self.stats["str"].setValue(char_stats.str_stat)
        self.stats["dex"].setValue(char_stats.dex_stat)
        self.stats["con"].setValue(char_stats.con_stat)
        self.stats["int"].setValue(char_stats.int_stat)
        self.stats["wis"].setValue(char_stats.wis_stat)
        self.stats["cha"].setValue(char_stats.cha_stat)
        
        try:
            self.background.setCurrentText(self.api.get_background(char.background_index)["name"])
            self.alignment.setCurrentText(self.api.get_alignment(char.alignment)["name"])
        except:
            self.background.setCurrentIndex(0)
            self.alignment.setCurrentIndex(0)
        self.story.setPlainText(char.background_story)

    def load_character(self, character_id=None):
        self.character_id = character_id
        self.clear_form()
