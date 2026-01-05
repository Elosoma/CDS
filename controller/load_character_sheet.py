from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget, QMessageBox,
    QListWidget, QPushButton, QTextEdit, QFormLayout,
    QHBoxLayout, QLineEdit, QComboBox, QSpinBox,QListWidgetItem
)

# Referencias
#from view.characters.character_tab import CharacterTab
from model.user_db import DatabaseManager, Characters
from model.api_2014 import DnDAPI


class LoadCharacterSheet():
    def __init__(self, character_index):
        super().__init__()

        self.api = DnDAPI()
        self.db = DatabaseManager()
        self.character_index = character_index


    def get_main_format(self):
        '''Pestaña info general'''
        lines = []
        character = self.db.get_character(self.character_index)

        lines.append(character.name)

        class_name = self.api.get_class(character.class_index)['name']
        race_name = self.api.get_race(character.race_index)['name']
        subrace_name = self.api.get_subrace(character.subrace_index)['name']
        lines.append(f'{class_name} {race_name} {subrace_name}')
        lines.append()
        
        stats = self.db.get_character_stats(self.character_index)
        lines.append(f'STR {stats.str_stat}| DEX {stats.dex_stat}| CON {stats.con_stat}| INT {stats.int_stat}| WIS {stats.wis_stat}| CHA {stats.cha_stat}')
        lines.append()


    def get_feats_format(self):
        '''Pestaña rasgos'''
        lines = []
        feats = self.db.get_character_feats(self.character_index)

        lines.append(f'FEATS')
        for feat in feats:
            feat_api = self.api.get_feat(feat.feat_index)
            lines.append(f'-{feat_api['name']}')

            desc = feat_api['desc']
            for line in desc:
                lines.append(line)
        lines.append()

        race_index = self.db.get_character(self.character_index).race_index
        race = self.api.get_race(race_index)

        lines.append(f'RACIAL TRAITS')
        for trait_list in race['traits']:
            lines.append(f'-{trait_list['name']}')

            desc = self.api.get_trait(trait_list['index'])['desc']
            for line in desc:
                lines.append(line)
        lines.append()

        class_index = self.db.get_character(self.character_index).class_index
        level = self.db.get_character(self.character_index).level
        _class = self.api.get_class(class_index)

        lines.append(f'CLASS TRAITS')
        for trait_list in _class['traits']:
            lines.append(f'{trait_list['name']}')

            desc = self.api.get_trait(trait_list['index'])['desc']
            for line in desc:
                lines.append(line)
        lines.append()



    def get_spells_format(self):
        # Pestaña conjuros
        self.db.get_character_spells(self.character_index)



    def get_equipment_format(self):
        # Pestaña conjuros
        lines = []
        spells = self.db.get_character_spells(self.character_index)

        lines.append(f'SPELLS')
        for spell in spells:
            spell_api = self.api.get_spell(spell.spell_index)
            lines.append(f'-{spell_api['name']}')

            desc = spell_api['desc']
            for line in desc:
                lines.append(line)

        





class CharacterDetail(QWidget):
    def __init__(self, db:DatabaseManager, parent):
        super().__init__()
        self.db = db
        self.parent_tab = parent
        self.character_id = None

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        self.edit_btn = QPushButton("✏️ Editar")
        self.delete_btn = QPushButton("🗑️ Eliminar")
        self.back_btn = QPushButton("⬅️ Volver")

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

        if not character:
            return

        self.text.setPlainText(
            self.db.build_character_sheet(character)
        )
    
    def edit_character(self):
        self.parent_tab.show_form(self.character_id)

    def delete_character(self):
        reply = QMessageBox.question(
            self,
            "Eliminar personaje",
            "¿Seguro que deseas eliminar este personaje?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_character(self.character_id)
            self.parent_tab.show_list()

    def save_character(self):
        if self.character_id is None:
            self.create_character()
        else:
            self.update_character()

    def load_character(self, character_id=None):
        self.character_id = character_id

        if character_id is None:
            self.clear_form()
            return

        c = self.db.get_character(character_id)

        self.name.setText(c.name)
        self.race.setText(c.race_index)
        self.char_class.setText(c.class_index)
        self.subclass.setText(c.subclass_index or "")
        self.level.setValue(c.level)
        self.hp.setValue(c.hit_points)
        self.background.setText(c.background_index or "")
        self.story.setPlainText(c.background_story or "")
        self.alignment.setText(c.alignment or "")


    def update_character(self):
        character = Characters(
            user_id=self.parent_tab.user,
            name=self.name.text(),
            race_index=self.race.text(),
            class_index=self.char_class.text(),
            level=self.level.value(),
            subclass_index=self.subclass.text() or None,
            hit_points=self.hp.value(),
            background_index=self.background.text(),
            background_story=self.story.toPlainText(),
            alignment=self.alignment.text(),
            object_id=self.character_id
        )

        self.db.update_character(character)
        self.parent_tab.show_detail(self.character_id)





    def load_character(self, character_id):
        self.character_id = character_id
        self.db:DatabaseManager
        
        character:Characters = self.db.get_character(character_id)

        if not character:
            self.text.setPlainText("Personaje no encontrado.")
            return

        # Versión simple, SIN API
        content = (
            f"Nombre: {character.name}\n"
            f"Clase: {character.class_index}\n"
            f"Raza: {character.race_index}\n"
            f"Nivel: {character.level}\n"
            f"PV: {character.hit_points}\n\n"
            f"Alineamiento: {character.alignment}\n"
            f"Trasfondo: {character.background_index}\n"
        )

        self.text.setPlainText(content)




















