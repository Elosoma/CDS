class Users:
    '''
    Clase Usuarios
    
    :method __init__: Crea un objeto Usuario con sus datos pertinentes.
    :method _print (Debug): Muestra por consola los datos del Usuario.
    '''

    def __init__(self,mail:str,
                 username:str,
                 password:str,
                 
                 object_id=''):
        '''
        Cada usuario será identificado mediante un correo único.

        :param mail: Correo asociado a la cuenta.
        :type mail: str

        :param username: Nombre de usuario de la cuenta.
        :type username: str

        :param password: Contraseña de acceso.
        :type password: str

        :param object_id: Clave primaria única.
        '''
        self.mail= mail
        self.username = username
        self.password = password
        self.object_id = object_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"MAIL: {self.mail}\n"
               f"USERNAME: {self.username}\n"
               f"PASSWORD: {self.password}\n"
               f"ID: {self.object_id}")

class Rulebooks:
    '''
    Clase Libros de reglas
    
    :method __init__: Crea un objeto Libro de reglas con sus datos pertinentes.
    :method _print (Debug): Muestra por consola los datos del Libro.
    '''

    def __init__(self,rulebook_name:str,
                 rulebook_desc:str='',

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
        Los libros de reglas serán identificados mediante un id.\n
        Podrán estar vinculados a un usuario mediante su id.\n
        Almacenan los datos en formato json.\n
        
        :param rulebook_name: Nombre del libro de reglas.
        :type rulebook_name: str
        :param rulebooks_description: Descripción del libro y su contenido.
        :type rulebooks_description: str

        :param user_id: Referencia al usuario dueño.
        :param object_id: Clave primaria única.
        '''
        self.rulebook_name = rulebook_name
        self.rulebooks_description = rulebook_desc

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

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"NOMBRE: {self.rulebook_name}\n"
               f"DESCRIPCION: {self.rulebooks_description}\n"
               
               f"ABILITY-SCORES: {self.ability_scores}\n"
               f"ALIGNMENTS: {self.alignments}\n"
               f"BACKGROUNDS: {self.backgrounds}\n"
               f"CLASSES: {self.classes}\n"
               f"CONDITIONS: {self.conditions}\n"
               f"DAMAGE-TYPES: {self.damage_types}\n"
               f"EQUIPMENT: {self.equipment}\n"
               f"EQUIPMENT-CATEGORIES: {self.equipment_categories}\n"
               f"FEATS: {self.feats}\n"
               f"FEATURES: {self.features}\n"
               f"LANGUAGES: {self.languages}\n"
               f"MAGIC-ITEMS: {self.magic_items}\n"
               f"MAGIC-SCHOOLS: {self.magic_schools}\n"
               f"MONSTERS: {self.monsters}\n"
               f"PROFICIENCIES: {self.proficiencies}\n"
               f"RACES: {self.races}\n"
               f"RULE-SECTIONS: {self.rule_sections}\n"
               f"RULES: {self.rules}\n"
               f"SKILLS: {self.skills}\n"
               f"SPELLS: {self.spells}\n"
               f"SUBCLASSES: {self.subclasses}\n"
               f"SUBRACES: {self.subraces}\n"
               f"TRAITS: {self.traits}\n"
               f"WEAPON-PROPERTIES: {self.weapon_properties}\n"
               
               f"DUEÑO: {self.user_id}\n"
               f"ID: {self.object_id}")

class Characters:
    '''
    Clase Personajes.
    
    :method __init__: Crea un objeto Personaje con sus datos pertinentes.
    :method _print (Debug): Muestra por consola los datos del Personaje.
    '''

    def __init__(self,name:str,
                 
                 race_index:str,
                 subrace_index:str,
                 class_index:str,
                 level:int,
                 subclass_index:str,
                 hit_points:int=1,

                 background_index:str='',
                 background_story:str='',
                 alignment:str='',
                 
                 user_id='',
                 object_id=''):
        '''
        Cada personaje será identificado por un id único generado en su creación.
        
        :param name: Nombre del personaje.
        :type name: str

        :param race_index: Raza del personaje.
        :type race_index: str (Index API)
        :param class_index: Clase del personaje.
        :type class_index: str (Index API)
        :param level: Nivel del personaje.
        :type level: int (1 -> 20)
        :param subclass_index: Subclase del personaje.
        :type subclass_index: str (Index API)
        :param hit_points: Puntos máximos de vida.
        :type hit_points: str (Index API)

        :param background_index: Trasfondo del personaje.
        :type background_index: str (Index API)
        :param background_story: Historia del personaje.
        :type background_story: str
        :param alignment: Alineamiento del personaje.
        :type alignment: str (Index API)

        :param user_id: Referencia al usuario dueño.
        :param object_id: Clave primaria única.
        '''
        self.name = name

        self.race_index = race_index
        self.subrace_index = subrace_index
        self.class_index = class_index
        self.level = level
        self.subclass_index = subclass_index
        self.hit_points = hit_points

        self.background_index = background_index
        self.background_story = background_story
        self.alignment = alignment
        
        self.user_id = user_id
        self.object_id = object_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"NOMBRE: {self.name}\n"
               f"RAZA: {self.race_index}\n"
               f"SUBRAZA: {self.subrace_index}\n"
               f"CLASE: {self.class_index}\n"
               f"SUBCLASE: {self.subclass_index}\n"
               f"VIDA-MAX: {self.hit_points}\n"
               f"TRASFONDO-INDEX: {self.background_index}\n"
               f"TRASFONDO-HISTORIA: {self.background_story}\n"
               f"ALINEAMIENTO: {self.alignment}\n"
               f"DUEÑO: {self.user_id}\n"
               f"ID: {self.object_id}")

class Character_stats:
    '''
    Clase Estadisticas del Personaje.
    
    :method __init__: Crea y almacena las estadisticas de cada personaje.
    :method _print (Debug): Muestra por consola las estadisticas.
    '''

    def __init__(self,
                 str_stat:int=10,
                 dex_stat:int=10,
                 con_stat:int=10,
                 int_stat:int=10,
                 wis_stat:int=10,
                 cha_stat:int=10,
                 
                 character_id=''):
        '''
        Almacena las estadísticas de cada personaje.

        :param str_stat: Fuerza.
        :type str_stat: int
        :param dex_stat: Destreza.
        :type dex_stat: int
        :param con_stat: Constitución.
        :type con_stat: int
        :param int_stat: Inteligencia.
        :type int_stat: int
        :param wis_stat: Sabiduria.
        :type wis_stat: int
        :param cha_stat: Carisma.
        :type cha_stat: int

        :param character_id: Referencia al personaje.
        '''
        self.str_stat = str_stat
        self.dex_stat = dex_stat
        self.con_stat = con_stat
        self.int_stat = int_stat
        self.wis_stat = wis_stat
        self.cha_stat = cha_stat

        self.character_id = character_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"CHARACTER-ID: {self.character_id}\n"
               f"FUERZA: {self.str_stat}\n"
               f"DESTREZA: {self.dex_stat}\n"
               f"CONSTITUCIÓN: {self.con_stat}\n"
               f"INTELIGENCIA: {self.int_stat}\n"
               f"SABIDURIA: {self.wis_stat}\n"
               f"CARISMA: {self.cha_stat}")

class Character_feats:
    '''
    Clase Rasgos de Personaje
    
    :method __init__: Crea una relación entre Personaje y Conjuros.
    :method _print (Debug): Muestra la relación por consola.
    '''

    def __init__(self,
                 feat_index:str,
                 character_id=''):
        '''
        Almacena los rasgos del personaje.

        :param feat_index: Referencia al rasgo del personaje.
        :type feat_index: str

        :param character_id: Referencia al personaje.
        '''
        self.feat_index = feat_index
        self.character_id = character_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"CHARACTER-ID: {self.character_id}\n"
               f"INDEX: {self.feat_index}")

class Character_spells:
    '''
    Clase Conjuros de Personaje.
    
    :method __init__: Crea una relación entre Personaje y Conjuros.
    :method _print (Debug): Muestra la relación por consola.
    '''

    def __init__(self,
                 spell_index:str,
                 character_id=''):
        '''
        Almacena los conjuros mediabte su index del api.

        :param spell_index: Referencia al conjuro del personaje.
        :type spell_index: int

        :param character_id: Referencia al personaje.
        '''
        self.spell_index = spell_index
        self.character_id = character_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"CHARACTER-ID: {self.character_id}\n"
               f"INDEX: {self.spell_index}")

class Character_equipment:
    '''
    Clase Equipamiento de Personaje.
    
    :method __init__: Crea una relación entre Personaje y Equipo.
    :method _print (Debug): Muestra la relación por consola.
    '''
    
    def __init__(self,
                 equipment_index:str,
                 quantity:int=1,
                 character_id=''):
        '''
        Almacena el equipo mediante su index del api.

        :param equipment_index: Referencia al objeto/equipamiento.
        :type equipment_index: str
        :param quantity: Cantidad.
        :type quantity: int

        :param character_id: Referencia al personaje.
        '''
        self.equipment_index = equipment_index
        self.quantity = quantity
        self.character_id = character_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"CHARACTER-ID: {self.character_id}\n"
               f"CANTIDAD: {self.quantity}\n"
               f"INDEX: {self.equipment_index}")

class Campaigns:
    '''
    Clase Campañas
    
    :method __init__: Crea un objeto Campaña con sus datos pertinentes.
    :method _print (Debug): Muestra por consola los datos de la Campaña.
    '''

    def __init__(self,name:str,
                 description:str='',

                 user_id='',
                 object_id=''):
        '''
        Cada campaña será identificada por un id.\n
        Están vinculados a un usuario mediante su id.\n

        :param name: Nombre de la campaña.
        :type name: str
        :param description: Descripcion de la campaña y notas.
        :type description: str

        :param user_id: Referencia al usuario dueño.
        :param object_id: Clave primaria única.
        '''
        self.name = name
        self.description = description

        self.user_id = user_id
        self.object_id = object_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"NOMBRE: {self.name}\n"
               f"DESCRIPCION: {self.description}\n"
               f"DUEÑO: {self.user_id}\n"
               f"ID: {self.object_id}")

class Campaign_characters:
    '''
    Clase Personajes de Campaña.
    
    :method __init__: Crea un objeto Personaje de Campaña con sus datos pertinentes.
    :method _print (Debug): Muestra por consola los datos del Perosnaje de Campaña.
    '''

    def __init__(self,health_points:int=0,
                 notes:str='',
                 
                 campaign_id='',
                 character_id=''):
        '''
        Reune los datos de cada personaje dentro de una campaña.\n
        Están vinculados a un usuario y campaña mediante su id.\n
        
        :param health_points: Puntos de vida actuales del personaje.
        :type health_points: int
        :param notes: Notas sobre objetos, estados, conjuros etc...
        :type notes: str

        :param campaign_id: Referencia a la campaña.
        :param character_id: Referencia al personaje.
        '''
        self.health_points = health_points
        self.notes = notes
        
        self.campaign_id = campaign_id
        self.character_id = character_id

    def _print(self):
        '''Debug, muestra los datos en consola ordenados y referenciados.'''
        print (f"PERSONAJE: {self.character_id}\n"
               f"CAMPAÑA: {self.campaign_id}\n"
               f"VIDA: {self.health_points}\n"
               f"NOTAS: {self.notes}")
