'''Cuenta con una clase API que realiza solicitudes mediante la función request'''
import requests


class DnDAPI:
    BASE_URL = "https://www.dnd5eapi.co/api/2014"

    def __init__(self):
        self.headers = {
            "Accept": "application/json"
        }

    def _get(self, endpoint: str):
        try:
            response = requests.get(
                f"{self.BASE_URL}{endpoint}",
                headers=self.headers,
                timeout=5
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"[API ERROR] {e}")
            return None
    

    # CLASES : classes, subclasses
    def get_classes(self):
        return self._get("/classes")
    
    def get_class(self, index: str):
        return self._get(f"/classes/{index}")

    def get_subclasses(self):
        return self._get("/subclasses")
    
    def get_subclass(self, index: str):
        return self._get(f"/subclasses/{index}")
    
    def get_class_levels(self, class_index: str):
        return self._get(f"/classes/{class_index}/levels")
    
    def get_class_level(self, class_index: str, level: int):
        return self._get(f"/classes/{class_index}/levels/{level}")
    
    def get_subclass_levels(self, class_index: str):
        return self._get(f"/subclasses/{class_index}/levels")
    
    def get_subclass_level(self, class_index: str, level: int):
        return self._get(f"/subclasses/{class_index}/levels/{level}")


    # RAZAS : races, subraces
    def get_races(self):
        return self._get("/races")

    def get_race(self, index: str):
        return self._get(f"/races/{index}")

    def get_subraces(self):
        return self._get("/subraces")

    def get_subrace(self, index: str):
        return self._get(f"/subraces/{index}")


    # CONJUROS : spells, magic-schools
    def get_spells(self):
        return self._get("/spells")

    def get_spell(self, index: str):
        return self._get(f"/spells/{index}")

    def get_magic_schools(self):
        return self._get("/magic-schools")

    def get_magic_school(self, index: str):
        return self._get(f"/magic-schools/{index}")


    # EQUIPAMIENTO : equipment, equipment-categories, magic-items
    def get_equipment(self):
        return self._get("/equipment")

    def get_equip(self, index: str):
        return self._get(f"/equipment/{index}")
    
    def get_equipment_categories(self):
        return self._get("/equipment-categories")

    def get_equipment_category(self, index: str):
        return self._get(f"/equipment-categories/{index}")
    
    def get_magic_items(self):
        return self._get("/magic-items")

    def get_magic_item(self, index: str):
        return self._get(f"/magic-items/{index}")


    # TRASFONDO : backgrounds, alignments, languages
    def get_backgrounds(self):
        return self._get("/backgrounds")

    def get_background(self, index: str):
        return self._get(f"/backgrounds/{index}")
    
    def get_alignments(self):
        return self._get("/alignments")

    def get_alignment(self, index: str):
        return self._get(f"/alignments/{index}")
    
    def get_languages(self):
        return self._get("/languages")

    def get_language(self, index: str):
        return self._get(f"/languages/{index}")
    

    # CARACTERÍSTICAS : features, feats
    def get_features(self):
        return self._get("/features")

    def get_feature(self, index: str):
        return self._get(f"/features/{index}")
    
    def get_feats(self):
        return self._get("/feats")

    def get_feat(self, index: str):
        return self._get(f"/feats/{index}")


    # RASGOS : traits, skills
    def get_traits(self):
        return self._get("/traits")

    def get_trait(self, index: str):
        return self._get(f"/traits/{index}")
    
    def get_skills(self):
        return self._get("/skills")

    def get_skill(self, index: str):
        return self._get(f"/skills/{index}")


    # MONSTRUOS : monsters
    def get_monsters(self):
        return self._get("/monsters")

    def get_monster(self, index: str):
        return self._get(f"/monsters/{index}")


    # REGLAS : rules, rule-sections
    def get_rules(self):
        return self._get("/rules")

    def get_rule(self, index: str):
        return self._get(f"/rules/{index}")
    
    def get_rule_sections(self):
        return self._get("/rule-sections")

    def get_rule_section(self, index: str):
        return self._get(f"/rule-sections/{index}")


    # DAÑO-CONDICIONES : conditions, damage-types
    def get_conditions(self):
        return self._get("/conditions")

    def get_condition(self, index: str):
        return self._get(f"/conditions/{index}")
    
    def get_damage_types(self):
        return self._get("/damage-types")

    def get_damage_type(self, index: str):
        return self._get(f"/damage-types/{index}")


    # PROPIEDADES : proficiencies, ability-scores, weapon-properties
    def get_proficiencies(self):
        return self._get("/proficiencies")

    def get_proficiency(self, index: str):
        return self._get(f"/proficiencies/{index}")
    
    def get_ability_scores(self):
        return self._get("/ability-scores")

    def get_ability_score(self, index: str):
        return self._get(f"/ability-scores/{index}")
    
    def get_weapon_properties(self):
        return self._get("/weapon-properties")

    def get_weapon_property(self, index: str):
        return self._get(f"/weapon-properties/{index}")
    