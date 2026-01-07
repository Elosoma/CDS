'''Gestiona los datos referentes a los usuarios de la aplicación'''
import sqlite3

'''
   ####   ####       ##      #####   #######   #####
  ##  ##   ##       ####    ##   ##   ##   #  ##   ##
 ##        ##      ##  ##   #         ## #    #
 ##        ##      ##  ##    #####    ####     #####
 ##        ##   #  ######        ##   ## #         ##
  ##  ##   ##  ##  ##  ##   ##   ##   ##   #  ##   ##
   ####   #######  ##  ##    #####   #######   #####
'''

class Users:
    '''Clase Usuarios, gestiona la creación, edición e interacción de las cuentas dentro de la aplicación.'''
    def __init__(self,username:str,
                 mail:str,
                 password:str,

                 object_id=''):
        '''
        El cada usuario será identificado mediante el correo único.

        :param username: Nombre de usuario de la cuenta.
        :type username: str
        :param mail: Correo asociado a la cuenta.
        :type mail: str, formato correo
        :param password: Contraseña de acceso.
        :type password: str, encriptado por protección de datos

        :param object_id: Clave primaria única.
        '''
        self.username = username
        self.mail = mail
        self.password = password

        self.object_id = object_id


class Characters:
    '''Clase Personajes, gestiona la creación, edición e interacción de los personajes asociados a un usuario.'''
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

class Character_stats:
    '''Almacena las estadísticas de cada personaje.'''
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

        :param str_stat: Fuerza del personaje.
        :type str_stat: int
        :param dex_stat: Destreza del personaje.
        :type dex_stat: int
        :param con_stat: Constitución del personaje.
        :type con_stat: int
        :param int_stat: Inteligencia del personaje.
        :type int_stat: int
        :param wis_stat: Sabiduria del personaje.
        :type wis_stat: int
        :param cha_stat: Carisma del personaje.
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

class Character_spells:
    '''Almacena los conjuros del personaje.'''
    def __init__(self,
                 spell_index:str,
                 character_id=''):
        '''
        Almacena los conjuros del personaje.

        :param spell_index: Referencia al conjuro del personaje.
        :type spell_index: int

        :param character_id: Referencia al personaje.
        '''
        self.spell_index = spell_index
        self.character_id = character_id

class Character_feats:
    '''Almacena los rasgos del personaje.'''
    def __init__(self,
                 feat_index:str,
                 character_id=''):
        '''
        Almacena los rasgos del personaje.

        :param feat_index: Referencia al rasgo del personaje.
        :type feat_index: str (Index API)

        :param character_id: Referencia al personaje.
        '''
        self.feat_index = feat_index
        self.character_id = character_id

class Character_equipment:
    '''Almacena el equipo de cada personaje.'''
    def __init__(self,
                 equipment_index:str,
                 quantity:int=1,
                 character_id=''):
        '''
        Almacena el equipo de cada personaje.

        :param equipment_index: Referencia al objeto/equipamiento.
        :type equipment_index: str (Index API)
        :param quantity: Cantidad.
        :type quantity: int

        :param character_id: Referencia al personaje.
        '''
        self.equipment_index = equipment_index
        self.quantity = quantity
        self.character_id = character_id


class Campaigns:
    '''Clase Campañas, gestiona la creación, edición e interacción de las campañas hechas por un usuario.'''
    def __init__(self,name:str,
                 description:str='',

                 user_id='',
                 object_id=''):
        '''
        Cada campaña será identificada por un id único generado en su creación.
        
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

class Campaign_characters:
    '''Clase personajes de campaña, almacena los datos relativos a personajes añadidos a una campaña.'''
    def __init__(self,health_points:int=0,
                 notes:str='',
                 
                 campaign_id='',
                 character_id=''):
        '''
        Reune los datos de cada personaje dentro de la campaña.
        
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

'''
 ######     ##     ######   ####       ##      #####
 # ## #    ####     ##  ##   ##       ####    ##   ##
   ##     ##  ##    ##  ##   ##      ##  ##   #
   ##     ##  ##    #####    ##      ##  ##    #####
   ##     ######    ##  ##   ##   #  ######        ##
   ##     ##  ##    ##  ##   ##  ##  ##  ##   ##   ##
  ####    ##  ##   ######   #######  ##  ##    #####
'''

class DatabaseManager:
    def __init__(self, db_name="model/cds.db"):
        '''
        Inicia la conexión con la base de datos.
        
        :param db_name: Nombre del archivo en el que se crea la conexión con la db y las tablas.
        :type db_name: Default path="model/cds.db"
        '''
        self.connection = sqlite3.connect(db_name)

    def create_table_users(self):
        cursor = self.connection.cursor()

        #Users()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            mail TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_characters(self):
        cursor = self.connection.cursor()

        #Characters()
        cursor.execute('''CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,

            name TEXT NOT NULL,

            race_index TEXT NOT NULL,
            subrace_index TEXT,
            class_index TEXT NOT NULL,
            level INTEGER NOT NULL,
            subclass_index TEXT,
            hit_points INTEGER NOT NULL,
            
            background_index TEXT,
            background_story TEXT,
            alignment TEXT,

            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_character_stats(self):
        cursor = self.connection.cursor()

        #Character_stats()
        cursor.execute('''CREATE TABLE IF NOT EXISTS character_stats (
            character_id INTEGER PRIMARY KEY,
            str INTEGER,
            dex INTEGER,
            con INTEGER,
            int INTEGER,
            wis INTEGER,
            cha INTEGER,
            FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_character_spells(self):
        cursor = self.connection.cursor()

        #Character_spells()
        cursor.execute('''CREATE TABLE IF NOT EXISTS character_spells (
            character_id INTEGER,
            spell_index TEXT,
            PRIMARY KEY (character_id, spell_index),
            FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_character_feats(self):
        cursor = self.connection.cursor()

        #Character_feats()
        cursor.execute('''CREATE TABLE IF NOT EXISTS character_feats (
            character_id INTEGER,
            feat_index TEXT,
            PRIMARY KEY (character_id, feat_index),
            FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_character_equipment(self):
        cursor = self.connection.cursor()

        #Character_equipment()
        cursor.execute('''CREATE TABLE IF NOT EXISTS character_equipment (
            character_id INTEGER,
            equipment_index TEXT,
            quantity INTEGER DEFAULT 1,
            PRIMARY KEY (character_id, equipment_index),
            FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_campaigns(self):
        cursor = self.connection.cursor()

        #Campaigns()
        cursor.execute('''CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_campaign_characters(self):
        cursor = self.connection.cursor()

        #Campaign_characters()
        cursor.execute('''CREATE TABLE IF NOT EXISTS campaign_characters (
            campaign_id INTEGER,
            character_id INTEGER,
            health_points INTEGER,
            notes TEXT,
            PRIMARY KEY (campaign_id, character_id),
            FOREIGN KEY (campaign_id) REFERENCES campaigns(id) ON DELETE CASCADE,
            FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_table_rulebooks(self):
        cursor = self.connection.cursor()

        #Rulebooks()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rulebooks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                rulebook_name TEXT,
                rulebooks_description TEXT,
                       
                ability_scores TEXT,
                alignments TEXT, 
                backgrounds TEXT, 
                classes TEXT, 
                conditions TEXT, 
                damage_types TEXT, 
                equipment TEXT, 
                equipment_categories TEXT, 
                feats TEXT, 
                features TEXT, 
                languages TEXT, 
                magic_items TEXT, 
                magic_schools TEXT, 
                monsters TEXT, 
                proficiencies TEXT, 
                races TEXT, 
                rule_sections TEXT, 
                rules TEXT, 
                skills TEXT, 
                spells TEXT, 
                subclasses TEXT, 
                subraces TEXT, 
                traits TEXT, 
                weapon_properties TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )''')
  
        self.connection.commit()
        cursor.close()

    def create_tables(self):
        '''Crea las tablas en caso de que no existan.'''
        self.create_table_users()

        self.create_table_characters()
        self.create_table_character_stats()
        self.create_table_character_spells()
        self.create_table_character_feats()
        self.create_table_character_equipment()

        self.create_table_campaigns()
        self.create_table_campaign_characters()
        
        self.create_table_rulebooks() 

    '''
##   ##  #######  ######    #####   #####     #####    #####
### ###   ##   #  # ## #   ##   ##   ## ##   ##   ##  ##   ##
#######   ## #      ##     ##   ##   ##  ##  ##   ##  #
#######   ####      ##     ##   ##   ##  ##  ##   ##   #####
## # ##   ## #      ##     ##   ##   ##  ##  ##   ##       ##
##   ##   ##   #    ##     ##   ##   ## ##   ##   ##  ##   ##
##   ##  #######   ####     #####   #####     #####    #####
    '''

    def close(self):
        '''Cierra conexión con la db'''
        self.connection.close()

    def delete_all(self):
        '''Borra todos los datos de la db'''
        cursor = self.connection.cursor()
        # En orden de dependencias.
        cursor.execute('''DROP TABLE IF EXISTS campaign_characters''')
        cursor.execute('''DROP TABLE IF EXISTS campaigns''')

        cursor.execute('''DROP TABLE IF EXISTS character_equipment''')
        cursor.execute('''DROP TABLE IF EXISTS character_feats''')
        cursor.execute('''DROP TABLE IF EXISTS character_spells''')
        cursor.execute('''DROP TABLE IF EXISTS character_stats''')
        cursor.execute('''DROP TABLE IF EXISTS characters''')

        cursor.execute('''DROP TABLE IF EXISTS rulebooks''')
        cursor.execute('''DROP TABLE IF EXISTS users''')
        
        self.connection.commit()
        cursor.close()
    
    '''
    #     #  #####  ####### ######   #####  
    #     # #     # #       #     # #     # 
    #     # #       #       #     # #       
    #     #  #####  #####   ######   #####  
    #     #       # #       #   #         # 
    #     # #     # #       #    #  #     # 
    #####   #####  ####### #     #  #####  
    '''

    def add_user(self, user:Users):
        '''Coamndo, SQL INSERT INTO users.'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, mail, password) 
            VALUES (?, ?, ?)
        ''', (user.username, user.mail, user.password))
        self.connection.commit()
        cursor.close()

    def update_user(self, user:Users):
        '''Comando, UPDATE users'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE users
            SET username = ?, password = ?
            WHERE id = ?
        ''', (user.username, user.password, user.object_id))
        self.connection.commit()
        cursor.close()

    def delete_user(self, object_id):
        '''Comando, DELETE FROM users, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()


    def get_mail_user(self, mail):
        '''Comando, SELECT FROM users, mediante el mail dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM users WHERE mail = ?''', (mail,))

        # Lo convierte y lo devuelve.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Users(row[1], row[2], row[3], row[0]) for row in rows]

    def get_all_users(self):
        '''Comando, SELECT * FROM users'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM users''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Users(row[1], row[2], row[3], row[0]) for row in rows]

    '''
    #####  #     #    #    ######     #     #####  ####### ####### ######   #####  
    #     # #     #   # #   #     #   # #   #     #    #    #       #     # #     # 
    #       #     #  #   #  #     #  #   #  #          #    #       #     # #       
    #       ####### #     # ######  #     # #          #    #####   ######   #####  
    #       #     # ####### #   #   ####### #          #    #       #   #         # 
    #     # #     # #     # #    #  #     # #     #    #    #       #    #  #     # 
    #####  #     # #     # #     # #     #  #####     #    ####### #     #  #####  
    '''

    def add_character(self, character:Characters):
        '''INSERT INTO characters'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO characters (
                user_id, name, race_index, subrace_index, class_index, level, subclass_index,
                hit_points, background_index, background_story, alignment
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            character.user_id,
            character.name,
            character.race_index,
            character.subrace_index,
            character.class_index,
            character.level,
            character.subclass_index,
            character.hit_points,
            character.background_index,
            character.background_story,
            character.alignment
        ))
        self.connection.commit()
        character_id = cursor.lastrowid
        cursor.close()
        return character_id

    def update_character(self, character:Characters):
        '''UPDATE characters'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE characters
            SET name = ?, race_index = ?, subrace_index = ?, class_index = ?, level = ?, subclass_index = ?,
                hit_points = ?, background_index = ?, background_story = ?, alignment = ?
            WHERE id = ?
        ''', (
            character.name,
            character.race_index,
            character.subrace_index,
            character.class_index,
            character.level,
            character.subclass_index,
            character.hit_points,
            character.background_index,
            character.background_story,
            character.alignment,
            character.object_id
        ))
        self.connection.commit()
        cursor.close()

    def delete_character(self, object_id):
        '''DELETE FROM characters'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM characters WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()


    def get_character(self, object_id):
        '''SELECT character by id'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM characters WHERE id = ?''', (object_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is []:
            return None

        return Characters(
            user_id=row[1],
            name=row[2],
            race_index=row[3],
            subrace_index=row[4],
            class_index=row[5],
            level=row[6],
            subclass_index=row[7],
            hit_points=row[8],
            background_index=row[9],
            background_story=row[10],
            alignment=row[11],
            object_id=row[0]
        )

    def get_user_characters(self, user_id):
        '''SELECT characters by user'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM characters WHERE user_id = ?''', (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        if rows is []:
            return None

        return [
            Characters(
                user_id=row[1],
                name=row[2],
                race_index=row[3],
                subrace_index=row[4],
                class_index=row[5],
                level=row[6],
                subclass_index=row[7],
                hit_points=row[8],
                background_index=row[9],
                background_story=row[10],
                alignment=row[11],
                object_id=row[0]
            )for row in rows
        ]

    def get_all_characters(self):
        '''Comando, SELECT * FROM characters'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM characters''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()
        if rows is []:
            return None

        return [
            Characters(
                user_id=row[1],
                name=row[2],
                race_index=row[3],
                subrace_index=row[4],
                class_index=row[5],
                level=row[6],
                subclass_index=row[7],
                hit_points=row[8],
                background_index=row[9],
                background_story=row[10],
                alignment=row[11],
                object_id=row[0]
            )for row in rows
        ]




    def add_character_stats(self, stats:Character_stats):
        '''INSERT INTO character_stats'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO character_stats
            (character_id, str, dex, con, int, wis, cha)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            stats.character_id,
            stats.str_stat,
            stats.dex_stat,
            stats.con_stat,
            stats.int_stat,
            stats.wis_stat,
            stats.cha_stat
        ))
        self.connection.commit()
        cursor.close()

    def update_character_stats(self, stats:Character_stats):
        '''UPDATE character_stats'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE character_stats
            SET str = ?, dex = ?, con = ?, int = ?, wis = ?, cha = ?
            WHERE character_id = ?
        ''', (
            stats.str_stat,
            stats.dex_stat,
            stats.con_stat,
            stats.int_stat,
            stats.wis_stat,
            stats.cha_stat,
            stats.character_id
        ))
        self.connection.commit()
        cursor.close()

    def get_character_stats(self, character_id):
        '''SELECT character_stats'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM character_stats WHERE character_id = ?''', (character_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Character_stats(
            character_id=int(row[0]),
            str_stat=int(row[1]),
            dex_stat=int(row[2]),
            con_stat=int(row[3]),
            int_stat=int(row[4]),
            wis_stat=int(row[5]),
            cha_stat=int(row[6])
        )




    def add_character_feat(self, character_id, feat_index):
        '''INSERT INTO character_feats'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO character_feats (character_id, feat_index)
            VALUES (?, ?)
        ''', (character_id, feat_index))
        self.connection.commit()
        cursor.close()

    def remove_character_feat(self, character_id, feat_index):
        '''DELETE FROM character_feats'''
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM character_feats
            WHERE character_id = ? AND feat_index = ?
        ''', (character_id, feat_index))
        self.connection.commit()
        cursor.close()

    def get_character_feats(self, character_id):
        '''SELECT feats by character'''
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT feat_index FROM character_feats WHERE character_id = ?
        ''', (character_id,))
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Character_feats(row[0],character_id) for row in rows]




    def add_character_spell(self, character_id, spell_index):
        '''INSERT INTO character_spells'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO character_spells (character_id, spell_index)
            VALUES (?, ?)
        ''', (character_id, spell_index))
        self.connection.commit()
        cursor.close()

    def remove_character_spell(self, character_id, spell_index):
        '''DELETE FROM character_spells'''
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM character_spells
            WHERE character_id = ? AND spell_index = ?
        ''', (character_id, spell_index))
        self.connection.commit()
        cursor.close()

    def get_character_spells(self, character_id):
        '''SELECT spells by character'''
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT spell_index FROM character_spells WHERE character_id = ?
        ''', (character_id,))
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Character_spells(row[0], character_id) for row in rows]




    def add_character_equipment(self, character_id, equipment_index, quantity=1):
        '''INSERT INTO character_equipment'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO character_equipment
            (character_id, equipment_index, quantity)
            VALUES (?, ?, ?)
        ''', (character_id, equipment_index, quantity))
        self.connection.commit()
        cursor.close()

    def update_character_equipment(self, character_id, equipment_index, quantity):
        '''UPDATE character_equipment'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE character_equipment
            SET quantity = ?
            WHERE character_id = ? AND equipment_index = ?
        ''', (quantity, character_id, equipment_index))
        self.connection.commit()
        cursor.close()

    def remove_character_equipment(self, character_id, equipment_index):
        '''DELETE FROM character_equipment'''
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM character_equipment
            WHERE character_id = ? AND equipment_index = ?
        ''', (character_id, equipment_index))
        self.connection.commit()
        cursor.close()

    def get_character_equipment(self, character_id):
        '''SELECT equipment by character'''
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT equipment_index, quantity
            FROM character_equipment
            WHERE character_id = ?
        ''', (character_id,))
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Character_equipment(row[0], row[1], character_id) for row in rows]

    '''
    #####     #    #     # ######     #    ###  #####  #     #  #####  
    #     #   # #   ##   ## #     #   # #    #  #     # ##    # #     # 
    #        #   #  # # # # #     #  #   #   #  #       # #   # #       
    #       #     # #  #  # ######  #     #  #  #  #### #  #  #  #####  
    #       ####### #     # #       #######  #  #     # #   # #       # 
    #     # #     # #     # #       #     #  #  #     # #    ## #     # 
    #####  #     # #     # #       #     # ###  #####  #     #  #####  
    '''

    def add_campaign(self, campaign:Campaigns):
        '''Coamndo, SQL INSERT INTO campaigns'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO campaigns (user_id, name, description) 
            VALUES (?, ?, ?)
        ''', (campaign.user_id, campaign.name, campaign.description))
        self.connection.commit()
        cursor.close()

    def update_campaigns(self, campaign:Campaigns):
        '''Comando, UPDATE campaigns'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE campaigns
            SET name = ?, description = ?
            WHERE id = ?
        ''', (campaign.name, campaign.description, campaign.object_id))
        self.connection.commit()
        cursor.close()

    def delete_campaign(self, object_id):
        '''Comando, DELETE FROM campaigns, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM campaigns WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()


    def get_campaign(self, object_id):
        '''Comando, SELECT FROM campaigns, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM campaigns WHERE id = ?''', (object_id,))

        # Lo convierte y lo devuelve.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Campaigns(row[2], row[3], row[1], row[0]) for row in rows]

    def get_user_campaigns(self, user_id):
        '''Comando, SELECT FROM campaigns, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM campaigns WHERE user_id = ?''', (user_id,))

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None
        
        return [Campaigns(row[2], row[3], row[1], row[0]) for row in rows]

    def get_all_campaigns(self):
        '''Comando, SELECT * FROM campaigns'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM campaigns''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Campaigns(row[2], row[3], row[1], row[0]) for row in rows]




    def add_campaign_character(self, campaign_id, character_id, health_points, notes=None):
        '''INSERT INTO campaign_characters'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO campaign_characters
            (campaign_id, character_id, health_points, notes)
            VALUES (?, ?, ?, ?)
        ''', (campaign_id, character_id, health_points, notes))
        self.connection.commit()
        cursor.close()

    def update_campaign_character(self, campaign_id, character_id, health_points, notes):
        '''UPDATE campaign_characters'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE campaign_characters
            SET health_points = ?, notes = ?
            WHERE campaign_id = ? AND character_id = ?
        ''', (health_points, notes, campaign_id, character_id))
        self.connection.commit()
        cursor.close()

    def delete_campaign_character(self, campaign_id, character_id):
        '''DELETE FROM campaign_characters'''
        cursor = self.connection.cursor()
        cursor.execute('''
            DELETE FROM campaign_characters
            WHERE campaign_id = ? AND character_id = ?
        ''', (campaign_id, character_id))
        self.connection.commit()
        cursor.close()


    def get_campaign_character(self, campaign_id, character_id):
        '''SELECT one campaign_character'''
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM campaign_characters
            WHERE campaign_id = ? AND character_id = ?
        ''', (campaign_id, character_id))
        row = cursor.fetchone()
        cursor.close()
        
        if row is None:
            return None

        return Campaign_characters(
            campaign_id = campaign_id,
            character_id = character_id,
            health_points = row[2] or 0,
            notes = row[3] or ""
        )

    def get_campaign_characters(self, campaign_id):
        '''SELECT characters in a campaign'''
        cursor = self.connection.cursor()
        id = int(campaign_id)
        cursor.execute('''
            SELECT * FROM campaign_characters
            WHERE campaign_id = ?
        ''', (id,))
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Campaign_characters(
            campaign_id = campaign_id,
            character_id = row[1],
            health_points = row[2] or 0,
            notes = row[3] or ""
        )for row in rows]

    def get_character_campaigns(self, character_id):
        '''SELECT campaigns where character is present'''
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT campaign_id, health_points, notes
            FROM campaign_characters
            WHERE character_id = ?
        ''', (character_id,))
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [
            {
                "campaign_id": row[0],
                "health_points": row[1],
                "notes": row[2]
            }
            for row in rows
        ]

    '''
    ######  #     # #       ####### ######  ####### ####### #    #  #####  
    #     # #     # #       #       #     # #     # #     # #   #  #     # 
    #     # #     # #       #       #     # #     # #     # #  #   #       
    ######  #     # #       #####   ######  #     # #     # ###     #####  
    #   #   #     # #       #       #     # #     # #     # #  #         # 
    #    #  #     # #       #       #     # #     # #     # #   #  #     # 
    #     #  #####  ####### ####### ######  ####### ####### #    #  #####  
    '''

    def add_rulebook(self, rulebook:Rulebooks):
        '''Coamndo, SQL INSERT INTO rulebooks'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO rulebooks (user_id, rulebook_name, rulebooks_description, ability_scores, alignments, 
                       backgrounds, classes, conditions, damage_types, equipment, equipment_categories, 
                       feats, features, languages, magic_items, magic_schools, monsters, 
                       proficiencies, races, rule_sections, rules, skills, spells, 
                       subclasses, subraces, traits, weapon_properties)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (rulebook.user_id, rulebook.rulebook_name, rulebook.rulebooks_description, rulebook.ability_scores, rulebook.alignments,
              rulebook.backgrounds, rulebook.classes, rulebook.conditions, rulebook.damage_types, rulebook.equipment, rulebook.equipment_categories,
              rulebook.feats, rulebook.features, rulebook.languages, rulebook.magic_items, rulebook.magic_schools, rulebook.monsters,
              rulebook.proficiencies, rulebook.races, rulebook.rule_sections, rulebook.rules, rulebook. skills, rulebook.spells,
              rulebook.subclasses, rulebook.subraces, rulebook.traits, rulebook.weapon_properties))
        self.connection.commit()
        cursor.close()

    def update_rulebook(self, rulebook:Rulebooks):
        '''Comando, UPDATE rulebooks'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE rulebooks
            SET rulebook_name = ?,
            SET rulebooks_description = ?,
                       
            SET ability_scores = ?, SET alignments = ?, SET backgrounds = ?, 
            SET classes = ?, SET conditions = ?, SET damage_types = ?, 
            SET equipment = ?, SET equipment_categories = ?, SET feats = ?, 
            SET features = ?, SET languages = ?, SET magic_items = ?, 
            SET magic_schools = ?, SET monsters = ?, SET proficiencies = ?, 
            SET races = ?, SET rule_sections = ?, SET rules = ?, 
            SET skills = ?, SET spells = ?, SET subclasses = ?, 
            SET subraces = ?, SET traits = ?, SET weapon_properties = ? 
       
            WHERE id = ?
        ''', (rulebook.rulebook_name, rulebook.rulebooks_description, rulebook.ability_scores, rulebook.alignments,
              rulebook.backgrounds, rulebook.classes, rulebook.conditions, rulebook.damage_types, rulebook.equipment, rulebook.equipment_categories,
              rulebook.feats, rulebook.features, rulebook.languages, rulebook.magic_items, rulebook.magic_schools, rulebook.monsters,
              rulebook.proficiencies, rulebook.races, rulebook.rule_sections, rulebook.rules, rulebook. skills, rulebook.spells,
              rulebook.subclasses, rulebook.subraces, rulebook.traits, rulebook.weapon_properties, rulebook.object_id))
        self.connection.commit()
        cursor.close()

    def delete_rulebook(self, object_id):
        '''Comando, DELETE FROM rulebooks, mediante el id del libro dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM rulebooks WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()


    def get_id_rulebook(self, object_id):
        '''Comando, SELECT FROM rulebooks, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM rulebooks WHERE id = ?''', (object_id))

        # Lo convierte y lo devuelve.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Rulebooks(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                          row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],
                          row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27], row[1], row[0]) for row in rows]
    
    def get_user_rulebooks(self, user_id):
        '''Comando, SELECT FROM rulebooks, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM rulebooks WHERE user_id = ?''', (user_id))

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Rulebooks(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                          row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],
                          row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27], row[1], row[0]) for row in rows]

    def get_all_rulebooks(self):
        '''Comando, SELECT * FROM rulebooks'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM rulebooks''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        if rows is []:
            return None

        return [Rulebooks(row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],
                          row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],
                          row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27], row[1], row[0]) for row in rows]

'''
 #####    #######  ######   ##   ##    ####
  ## ##    ##   #   ##  ##  ##   ##   ##  ##
  ##  ##   ## #     ##  ##  ##   ##  ##
  ##  ##   ####     #####   ##   ##  ##
  ##  ##   ## #     ##  ##  ##   ##  ##  ###
  ## ##    ##   #   ##  ##  ##   ##   ##  ##
 #####    #######  ######    #####     #####
'''

class Debug():

    def __init__(self):
        self.db = DatabaseManager()

    def close(self):
        self.db.close()

    def seed_users(self):
        users = [
            Users("admin", "admin@cds.com", "admin123"),
            Users("player1", "player1@cds.com", "player123"),
            Users("player2", "player2@cds.com", "player123")
        ]

        for user in users:
            self.db.add_user(user)


    def seed_characters(self):
        characters = [
            Characters(
                user_id=1,
                name="Thorin",
                race_index="dwarf",
                subrace_index="hill-dwarf",
                class_index="barbarian",
                level=3,
                subclass_index=None,
                hit_points=38,
                background_index="soldier",
                background_story="Veterano de mil batallas",
                alignment="Lawful Neutral"
            ),
            Characters(
                user_id=1,
                name="Eldrin",
                race_index="elf",
                subrace_index="",
                class_index="wizard",
                level=5,
                subclass_index="school-of-evocation",
                hit_points=26,
                background_index="sage",
                background_story="Estudioso arcano",
                alignment="Neutral Good"
            )
        ]

        for character in characters:
            self.db.add_character(character)

    def seed_character_stats(self):
        stats = [
            Character_stats(16, 14, 15, 8, 10, 12, 1),
            Character_stats(8, 14, 12, 18, 13, 10, 2)
        ]

        for stat in stats:
            self.db.add_character_stats(stat)

    def seed_character_spells(self):
        spells = [
            (2, "fireball"),
            (2, "magic-missile")
        ]

        for character_id, spell_index in spells:
            self.db.add_character_spell(character_id, spell_index)

    def seed_character_feats(self):
        feats = [
            (1, "great-weapon-master"),
            (2, "war-caster")
        ]

        for character_id, feat_index in feats:
            self.db.add_character_feat(character_id, feat_index)

    def seed_character_equipment(self):
        equipment = [
            (1, "greataxe", 1),
            (1, "explorers-pack", 1),
            (2, "spellbook", 1)
        ]

        for character_id, equipment_index, quantity in equipment:
            self.db.add_character_equipment(character_id, equipment_index, quantity)


    def seed_campaigns(self):
        campaigns = [
            Campaigns("La mina perdida", "Exploración de ruinas antiguas", 1),
            Campaigns("Sombras del norte", "Amenaza creciente", 2)
        ]

        for campaign in campaigns:
            self.db.add_campaign(campaign)

    def seed_campaign_characters(self):
        c1 = Campaign_characters (
            health_points=34, 
            notes="100 - Gold", 
            campaign_id=1,
            character_id=1)
        c2 = Campaign_characters (
            health_points=26, 
            notes="Spellbook and backpack",
            campaign_id=1,
            character_id=2)
        campaign_characters = [c1,c2]

        for char in campaign_characters:
            self.db.add_campaign_character(char.campaign_id, char.character_id, char.health_points, char.notes)


    def seed_rulebooks(self):
        rulebooks = [
            Rulebooks(
                user_id=1,
                rulebook_name="Prueba",
                rulebooks_description= "Ejemplo"
            )
        ]

        for rulebook in rulebooks:
            self.db.add_rulebook(rulebook)


    def seed_all(self):
        self.seed_users()
        self.seed_characters()
        self.seed_character_stats()
        self.seed_character_spells()
        self.seed_character_feats()
        self.seed_character_equipment()
        self.seed_campaigns()
        self.seed_campaign_characters()
        self.seed_rulebooks()


    '''-----------------------------------------------------------------------'''

    def test_users(self):
            data:list = self.db.get_all_users()
            for u in data:
                u:Users
                print (f'{u.object_id} - {u.username} - {u.mail} - {u.password}') 
            print ("-" * 40)
            print ()

    def test_characters(self):
            data:list = self.db.get_all_characters()
            for u in data:
                u:Characters
                print (f'{u.object_id} - {u.name}')

                print (f'\nStats')
                carac1:Character_stats = self.db.get_character_stats(u.object_id)
                print (f' -FUE {carac1.str_stat}\n -DEX {carac1.dex_stat}\n -CON {carac1.con_stat}\n -SAB {carac1.wis_stat}\n -INT {carac1.int_stat}\n -CHA {carac1.cha_stat}')

                print (f'\nSpells')
                carac2:list = self.db.get_character_spells(u.object_id)
                for x2 in carac2:
                    x2:Character_spells
                    print (f' -{x2.spell_index}')

                print (f'\nFeats')
                carac3:list = self.db.get_character_feats(u.object_id) 
                for x3 in carac3:
                    x3:Character_feats
                    print (f' -{x3.feat_index}')

                print (f'\nEquip')
                carac4:list = self.db.get_character_equipment(u.object_id) 
                for x4 in carac4:
                    x4:Character_equipment
                    print (f' -{x4.equipment_index} {x4.quantity}')
                print ("/" * 40)
                print ()
            print ("-" * 40)
            print ()
        
    def test_campaigns(self):
            data:list = self.db.get_all_campaigns()
            for u in data:
                u:Campaigns
                print (f'{u.object_id} - {u.name}')
                camp = self.db.get_campaign_characters(u.object_id)

                for c in camp:
                    c:Campaign_characters
                    ch:Characters = self.db.get_character(c.character_id)
                    print (f'{ch.name} |{c.character_id}| hp:{c.health_points} - nt:{c.notes}\n')
                print ("/" * 40)
                print ()
            print ("-" * 40)
            print ()

    def test_rulebooks(self):
            data:list = self.db.get_all_rulebooks()
            for u in data:
                u:Rulebooks
                print (f'{u.object_id} - {u.rulebook_name}')
            print ("-" * 40)
            print ()

    def dispaly_all(self):
        self.test_users()
        self.test_characters()
        self.test_campaigns()
        self.test_rulebooks()

# DEBUG, Inicia la db y permite realizar acciones aisladas tales como añadir o eliminar datos de prueba
if __name__ == "__main__":
    db = DatabaseManager()
    dg = Debug()
    
    db.delete_all()
    db.create_tables()
    dg.seed_all()
    dg.dispaly_all()

    #db.create_table_users()
    #dg.seed_users()
    #dg.test_users()

    #--------------------
    #db.create_table_characters()
    #db.create_table_character_stats()
    #db.create_table_character_spells()
    #db.create_table_character_feats()
    #db.create_table_character_equipment()

    #dg.seed_characters()
    #dg.seed_character_stats()
    #dg.seed_character_spells()
    #dg.seed_character_feats()
    #dg.seed_character_equipment()
    
    #dg.test_characters()

    #--------------------
    #db.create_table_campaigns()
    #db.create_table_campaign_characters()

    #dg.seed_campaigns()
    #dg.seed_campaign_characters()

    #dg.test_campaigns()

    #--------------------

    #db.create_table_rulebooks()
    #dg.seed_rulebooks()
    #dg.test_rulebooks()
