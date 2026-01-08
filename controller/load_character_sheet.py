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
    def __init__(self, db:DatabaseManager, api:DnDAPI, character_id):
        super().__init__()
        self.db = db
        self.api = api
        self.character_id = character_id


    def get_main_format(self):
        '''Pestaña info general del personaje'''
        lines = []
        character = self.db.get_character(self.character_id)

        try:
            # General
            race_name = self.api.get_race(character.race_index)['name']
            class_name = self.api.get_class(character.class_index)['name']
            lines.append(f'{character.name}\n{race_name}  {class_name} Lvl: {character.level}')
        except:
            lines.append("API INFO ERROR")

        try:
            # Stats
            stats = self.db.get_character_stats(self.character_id)
            lines.append(f'STR {stats.str_stat}| DEX {stats.dex_stat}| CON {stats.con_stat}| INT {stats.int_stat}| WIS {stats.wis_stat}| CHA {stats.cha_stat}')
        except:
            lines.append("DB STATS ERROR")


        try:
            # Datos de clase
            lines.append(f"\n\n{class_name}")
            lines.append(self.get_classlvl_format(character.class_index, character.subclass_index, character.level))
        except:
            lines.append("API CLASS ERROR")

        try:
            # Datos raciales
            lines.append(f"\n\n{race_name}")
            lines.append(self.get_racial_format(character.race_index, character.subrace_index))
        except:
            lines.append("API RACE ERROR")

        try:
            # Datos de trasfondo
            bg_name = self.api.get_background(character.background_index)["name"]
            lines.append(f"\n\n{bg_name}")
            lines.append(self.get_background_format(character.background_index, character.background_story))
        except:
            lines.append("API BACKGROUND ERROR")
        return "\n".join(lines)


    def get_classlvl_format(self, ch_class, ch_subclass, ch_lvl):
        '''Da formato a los datos de clase y subclase'''
        lines = []

        for i in range(ch_lvl):
            lvl = i+1
            lines.append(f'Lvl: {lvl}\n')
            lvl_features = self.api.get_class_level(ch_class,lvl)["features"]
            if lvl_features:
                for feature in lvl_features:
                    feat = self.api.get_feature(feature["index"])
                    lines.append(f'   -{feat["name"]}')
                    for des in feat.get('desc'):
                        lines.append(f"  {des}")
                    lines.append("")
            
            if ch_subclass != None:
                sublvl_features = self.api.get_subclass_level(ch_subclass,lvl)["features"]
                if sublvl_features:
                    for feature in sublvl_features:
                        feat = self.api.get_feature(feature["index"])
                        lines.append(f'   -{feat["name"]}')
                        for des in feat.get('desc'):
                            lines.append(f"  {des}")
                        lines.append("")

        return "\n".join(lines)
    
    def get_racial_format(self, ch_race, ch_subrace):
        '''Da formato a los datos de raza y subraza'''
        lines = []

        race_traits = self.api.get_race(ch_race)["traits"]
        if race_traits:
            for trait in race_traits:
                feat = self.api.get_trait(trait["index"])
                lines.append(f'   -{feat["name"]}')
                for des in feat.get('desc'):
                    lines.append(f"  {des}")
                lines.append("")
        
        if ch_subrace != None and ch_subrace != "":
            subrace_traits = self.api.get_subrace(ch_subrace)["racial_traits"]
            if subrace_traits:
                for trait in subrace_traits:
                    feat = self.api.get_trait(trait["index"])
                    lines.append(f'   -{feat["name"]}')
                    for des in feat.get('desc'):
                        lines.append(f"  {des}")
                    lines.append("")

        return "\n".join(lines)
    
    def get_background_format(self, ch_background, ch_story):
        '''Da formato a los datos de raza y subraza'''
        lines = []

        background_desc = self.api.get_background(ch_background)["desc"]
        if background_desc:
            for desc in background_desc:
                lines.append(f"  {desc}")
            lines.append("")
        
        if ch_story != None and ch_story != "":
            lines.append("Story/Notes")
            lines.append(ch_story)
            lines.append("")

        return "\n".join(lines)
    