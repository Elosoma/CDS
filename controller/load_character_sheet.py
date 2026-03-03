from model import DatabaseManager, DnDAPI

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
            subclass_name = self.api.get_subclass(character.subclass_index)['name']
            lines.append(f'{character.name}\n{race_name}  {class_name} {subclass_name} Lvl: {character.level}')
        except:
            lines.append("API INFO ERROR")

        try:
            # Stats
            stats = self.db.get_character_stats(self.character_id)
            lines.append(f'STR {stats.str_stat}| DEX {stats.dex_stat}| CON {stats.con_stat}| INT {stats.int_stat}| WIS {stats.wis_stat}| CHA {stats.cha_stat}')
        except:
            lines.append("DB STATS ERROR")

        # Datos de trasfondo
        lines.append(self.get_background_format(character.background_index, character.background_story))

        return "\n".join(lines)

    def get_classlvl_format(self):
        '''Da formato a los datos de clase y subclase'''
        try:
            character = self.db.get_character(self.character_id)
            ch_class = character.class_index
            ch_subclass = character.subclass_index
            ch_lvl = character.level
            lines = []

            try:
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
            except:
                lines.append("[API CLASS ERROR]")
                
            try:
                if ch_subclass != None:
                    for i in range(ch_lvl):
                        lvl = i+1
                        try:
                            sublvl_features = self.api.get_subclass_level(ch_subclass,lvl)["features"]

                            if sublvl_features:
                                for feature in sublvl_features:
                                    feat = self.api.get_feature(feature["index"])
                                    lines.append(f'   -{feat["name"]}')
                                    for des in feat.get('desc'):
                                        lines.append(f"  {des}")
                                    lines.append("")
                        except:
                            lines.append("")
            except:
                lines.append("[API SUBCLASS ERROR]")

            return "\n".join(lines)
        except:
            return "[API ERROR]"

    def get_racial_format(self):
        '''Da formato a los datos de raza y subraza'''
        try:
            character = self.db.get_character(self.character_id)
            ch_race = character.race_index
            ch_subrace = character.subrace_index
            lines = []

            try:
                race_traits = self.api.get_race(ch_race)["traits"]
                if race_traits:
                    for trait in race_traits:
                        feat = self.api.get_trait(trait["index"])
                        lines.append(f'   -{feat["name"]}')
                        for des in feat.get('desc'):
                            lines.append(f"  {des}")
                        lines.append("")
            except:
                lines.append("[API RACE ERROR]")
            
            try:
                if ch_subrace != None and ch_subrace != "":
                    subrace_traits = self.api.get_subrace(ch_subrace)["racial_traits"]
                    if subrace_traits:
                        for trait in subrace_traits:
                            feat = self.api.get_trait(trait["index"])
                            lines.append(f'   -{feat["name"]}')
                            for des in feat.get('desc'):
                                lines.append(f"  {des}")
                            lines.append("")
            except:
                lines.append("[API SUBRACE ERROR]")

            return "\n".join(lines)
        except:
            return "[API ERROR]"
        
    def get_background_format(self, ch_background, ch_story):
        '''Da formato a los datos de raza y subraza'''
        lines = []

        try:
            bg_name = self.api.get_background(ch_background)["name"]
            lines.append(f"\n\n{bg_name}")
            background_des = self.api.get_background(ch_background)
            background_desc = background_des['feature']["desc"]
            if background_desc:
                for desc in background_desc:
                    lines.append(f"  {desc}")
                lines.append("")
        except:
            lines.append("API Background Error")
    

        lines.append("Story/Notes:")
        lines.append(ch_story)
        lines.append("")

        return "\n".join(lines)
    