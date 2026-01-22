class Rulebooks:
    '''Clase Libros de reglas, gestiona la creación, edición e interacción de los libros de reglas y como estos se vinculan a la api online.'''
    def __init__(self,rulebook_name:str,
                 rulebooks_description:str='',

                 ability_scores:str='',alignments:str='',backgrounds:str='',
                 classes:str='',conditions:str='',damage_types:str='',
                 equipment:str='',equipment_categories:str='',feats:str='',
                 features:str='',languages:str='',magic_items:str='',
                 magic_schools:str='',monsters:str='',proficiencies:str='',
                 races:str='',rule_sections:str='',rules:str='',
                 skills:str='',spells:str='',subclasses:str='',
                 subraces:str='',traits:str='',weapon_properties:str='',

                 user_id='',
                 object_id=''):
        '''
        Libros de reglas y su contenido. Almacenado todo mediante textos con formato json.
        
        :param rulebook_name: Nombre del libro de reglas.
        :type rulebook_name: str
        :param rulebooks_description: Descripción del libro y su contenido.
        :type rulebooks_description: str

        :param user_id: Referencia al usuario dueño.
        :param object_id: Clave primaria única.
        '''
        self.rulebook_name = rulebook_name
        self.rulebooks_description = rulebooks_description

        self.ability_scores = ability_scores
        self.alignments = alignments
        self.backgrounds = backgrounds
        self.classes = classes
        self.conditions = conditions
        self.damage_types = damage_types
        self.equipment = equipment
        self.equipment_categories = equipment_categories
        self.feats = feats
        self.features = features
        self.languages = languages
        self.magic_items = magic_items
        self.magic_schools = magic_schools
        self.monsters = monsters
        self.proficiencies = proficiencies
        self.races = races
        self.rule_sections = rule_sections
        self.rules = rules
        self.skills = skills
        self.spells = spells
        self.subclasses = subclasses
        self.subraces = subraces
        self.traits = traits
        self.weapon_properties = weapon_properties
        
        self.user_id = user_id
        self.object_id = object_id