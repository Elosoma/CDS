'''Gestiona los datos referentes a los usuarios de la aplicación'''
import sqlite3, json
from PyQt6.QtCore import QDateTime,QDate,QTime

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
        :param object_id: Referencia interna para la db local.
        '''
        self.username = username
        self.mail = mail
        self.password = password
        self.object_id = object_id

class Characters:
    '''Clase Personajes, gestiona la creación, edición e interacción de los personajes asociados a un usuario.'''
    def __init__(self,name:str,
                 race:str,
                 _class:str,
                 feats:str,
                 stats:str,
                 equipment:str,
                 background:str,
                 spells:str,
                 lvl:int,
                 health_points:str,
                 user_id='',
                 object_id=''):
        '''
        Cada personaje será identificado por un id único generado en su creación.
        
        :param name: Nombre del personaje de rol.
        :type name: str
        :param race: Raza del personaje de rol, humano, elfo, enano...
        :type race: str (ID API)
        :param _class: Clase del personaje de rol, barbaro, guerrero, mago...
        :type _class: str (ID API)
        :param feats: Rasgos del personaje, visión en la oscuridad, resistencia enana...
        :type feats: str, json con ID API
        :param stats: Atributos/Estadisticas del personaje, fuerza, destreza, carisma...
        :type stats: str, json con esquema fijo
        :param equipment: Equipamiento del personaje, objetos, armas, armaduras ect.
        :type equipment: str, json con esquema escalable
        :param background: Description del trasfondo del personaje, historia, notas, descripcioón...
        :type background: str, json con esquema fijo
        :param spells: Lista de conjuros del personaje (en caso de que tenga)
        :type spells: str, json con esquema escalable
        :param lvl: Nivel del personaje.
        :type lvl: int
        :param health_points: Numero de puntos de vida (hecho en json para controlar vida temporal y dados de muerte)
        :type health_points: str, json con esquema fijo
        :param user_id: Referencia interna para la db local.
        :param object_id: Referencia interna para la db local.
        '''
        self.id = ''
        self.name = name
        self.race = race
        self._class = _class
        self.feats = feats
        self.stats = stats
        self.equipment = equipment
        self.background = background
        self.spells = spells
        self.lvl = lvl
        self.health_points = health_points
        self.user_id = user_id
        self.object_id = object_id

class Campaigns:
    '''Clase Campañas, gestiona la creación, edición e interacción de las campañas hechas por un usuario y accedidas por otros.'''
    def __init__(self,name:str,
                 description:str,
                 characters:str,
                 user_id='',
                 object_id=''):
        '''
        Cada campaña será identificada por un id único generado en su creación.
        
        :param name: Nombre de la campaña.
        :type name: str
        :param description: Descripcion de la campaña y notas
        :type description: str, json con esquema fijo
        :param characters: Lista de personajes dentro de la campaña y referencias a estos.
        :type characters: str, json con esquema fijo
        :param user_id: Referencia interna para la db local.
        :param object_id: Referencia interna para la db local.
        '''
        self.id = ''
        self.name = name
        self.description = description
        self.characters = characters
        self.user_id = user_id
        self.object_id = object_id

class Rulebooks:
    '''Clase Libros de reglas, gestiona la creación, edición e interacción de los libros de reglas y como estos se vinculan a la api online.'''
    def __init__(self,name:str,
                 user_id='',
                 object_id=''):
        '''WIP :('''
        self.name = name
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
    def __init__(self, db_name="res/cds.db"):
        '''
        Inicia la conexión con la base de datos.
        
        :param db_name: Nombre del archivo en el que se crea la conexión con la db y las tablas.
        :type db_name: Default path="res/cds.db"
        '''
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        '''Crea las tablas en caso de que no existan.'''
        cursor = self.connection.cursor()

        #Users()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                mail TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')

        #Characters()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                race TEXT NOT NULL,
                _class TEXT NOT NULL,
                feats TEXT NOT NULL,
                stats TEXT NOT NULL,
                equipment TEXT,
                background TEXT,
                spells TEXT,
                lvl INTEGER NOT NULL,
                health_points TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )''')
        
        #Campaigns()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS campaigns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT,
                characters TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )''')
        
        #Rulebooks()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rulebooks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )''')

        # Commit
        self.connection.commit()
        cursor.close()

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
        cursor.execute('''DROP TABLE IF EXISTS characters''')
        cursor.execute('''DROP TABLE IF EXISTS campaigns''')
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

    def get_all_users(self):
        '''Comando, SELECT * FROM users'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM users''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        return [Users(row[1], row[2], row[3], row[0]) for row in rows]
    
    def update_user(self, user:Users):
        '''Comando, UPDATE users, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE users
            SET username = ?, mail = ?, password = ?
            WHERE id = ?
        ''', (user.username, user.mail, user.password, user.object_id))
        self.connection.commit()
        cursor.close()

    def delete_user(self, object_id):
        '''Comando, DELETE FROM users, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM users WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()

    def get_user_mail(self, mail):
        '''Comando, SELECT FROM users, mediante el mail del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM users WHERE mail = ?''', (mail,))

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

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
        '''Coamndo, SQL INSERT INTO characters.'''
        Characters()    
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO characters (user_id, name, race, _class, feats, stats, equipment, background, spells, lvl, health_points) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (character.user_id, character.name, character.race, character._class, character.feats, character.stats, 
              character.equipment, character.background, character.spells, character.lvl, character.health_points))
        self.connection.commit()
        cursor.close()

    def get_all_characters(self):
        '''Comando, SELECT * FROM characters'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM characters''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        return [Characters(row[2], row[3], row[4], row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[1], row[0]) for row in rows]
    
    def update_character(self, character:Characters):
        '''Comando, UPDATE characters, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE characters
            SET name = ?, race = ?, _class = ?, feats = ?, stats = ?, equipment = ?, background = ?, spells = ?, lvl = ?, health_points = ?
            WHERE id = ?
        ''', (character.name, character.race, character._class, character.feats, character.stats, character.equipment, 
              character.background, character.spells, character.lvl, character.health_points, character.object_id))
        self.connection.commit()
        cursor.close()

    def delete_character(self, object_id):
        '''Comando, DELETE FROM characters, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM characters WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()

    def get_user_characters(self, user_id):
        '''Comando, SELECT FROM characters, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM characters WHERE user_id = ?''', (user_id))

        # Los convierte y los devuelve como una lista de usuarios
        rows = cursor.fetchall()
        cursor.close()

        return [Characters(row[2], row[3], row[4], row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[1], row[0]) for row in rows]

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
            INSERT INTO campaigns (user_id, name, description, characters) 
            VALUES (?, ?, ?, ?)
        ''', (campaign.user_id, campaign.name, campaign.description, campaign.characters))
        self.connection.commit()
        cursor.close()

    def get_all_campaigns(self):
        '''Comando, SELECT * FROM campaigns'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM campaigns''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        return [Campaigns(row[2], row[3], row[4], row[1], row[0]) for row in rows]
    
    def update_campaigns(self, campaign:Campaigns):
        '''Comando, UPDATE campaigns, mediante el id de la campaña dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE campaigns
            SET name = ?, description = ?, characters = ?
            WHERE id = ?
        ''', (campaign.name, campaign.description, campaign.characters, campaign.object_id))
        self.connection.commit()
        cursor.close()

    def delete_campaign(self, object_id):
        '''Comando, DELETE FROM campaigns, mediante el id de la campaña dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM campaigns WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()

    def get_user_campaigns(self, user_id):
        '''Comando, SELECT FROM campaigns, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM campaigns WHERE user_id = ?''', (user_id))

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        return [Campaigns(row[2], row[3], row[4], row[1], row[0]) for row in rows]

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
            INSERT INTO rulebooks (user_id, name) 
            VALUES (?, ?)
        ''', (rulebook.user_id, rulebook.name))
        self.connection.commit()
        cursor.close()

    def get_all_rulebooks(self):
        '''Comando, SELECT * FROM rulebooks'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM rulebooks''')

        # Los convierte y los devuelve como una lista.
        rows = cursor.fetchall()
        cursor.close()

        return [Rulebooks(row[2], row[1], row[0]) for row in rows]
    
    def update_rulebook(self, rulebook:Rulebooks):
        '''Comando, UPDATE rulebooks, mediante el id dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''
            UPDATE rulebooks
            SET name = ?
            WHERE id = ?
        ''', (rulebook.name, rulebook.object_id))
        self.connection.commit()
        cursor.close()

    def delete_rulebook(self, object_id):
        '''Comando, DELETE FROM rulebooks, mediante el id del libro dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM rulebooks WHERE id = ?''', (object_id,))
        self.connection.commit()
        cursor.close()

    def get_user_rulebooks(self, user_id):
        '''Comando, SELECT FROM rulebooks, mediante el id del user dado.'''
        cursor = self.connection.cursor()
        cursor.execute('''SELECT FROM rulebooks WHERE user_id = ?''', (user_id))

        # Los convierte y los devuelve como una lista de usuarios
        rows = cursor.fetchall()
        cursor.close()

        return [Rulebooks(row[2], row[1], row[0]) for row in rows]

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

    def data_users(self):
        self.db.add_user(Users("Vacio","vacioa@gmail.com","vacio"))
        self.db.add_user(Users("Ejemplo","ejemplo@gmail.com","ejemplo"))
        self.db.add_user(Users("Eloy","eloysolermainar@gmail.com","eloy"))

    def data_characters(self):
            self.db.add_character(Characters("Comprar","Comprar bateria portatil"))
            self.db.add_character(Characters("Terminar TFG :(","Añadir bibliografia"))
            self.db.add_character(Characters("Ejemplo","Descripción"))

    def data_campaigns(self):
            self.db.add_campaign(Campaigns("Cine","2025-04-02 20:15"))
            self.db.add_campaign(Campaigns("Clases de piano","2025-04-04 18:00"))
            self.db.add_campaign(Campaigns("Desayuno","2025-04-11 08:30"))

    def data_rulebooks(self):
            self.db.add_rulebook(Rulebooks("Cumapleaños Carla","2025-03-08"))
            self.db.add_rulebook(Rulebooks("Cumapleaños Daniel","2025-09-11"))
            self.db.add_rulebook(Rulebooks("Cumapleaños Ruben","2025-02-23"))

    def test_data(self):
        self.data_users()
        self.data_characters()
        self.data_campaigns()
        self.data_rulebooks()

    '''-----------------------------------------------------------------------'''

    def test_users(self):
            data:list = self.db.get_all_users()
            for u in data:
                u:Users
                print (f'{u.object_id} - {u.username} - {u.mail} - {u.password}')
            print ("\n\n\n") 

    def test_characters(self):
            data:list = self.db.get_all_characters()
            for u in data:
                u:Characters
                print (f'{u.object_id} - {u.name}')
            print ("\n\n\n")
        

    def test_campaigns(self):
            data:list = self.db.get_all_campaigns()
            for u in data:
                u:Campaigns
                print (f'{u.object_id} - {u.name}')
            print ("\n\n\n")
        
    
    def test_rulebooks(self):
            data:list = self.db.get_all_rulebooks()
            for u in data:
                u:Rulebooks
                print (f'{u.object_id} - {u.name}')
            print ("\n\n\n")

    def dispaly_all(self):
        self.test_users()
        self.test_characters()
        self.test_campaigns()
        self.test_rulebooks()

# DEBUG, Inicia la db y permite realizar acciones aisladas tales como añadir o eliminar datos de prueba
if __name__ == "__main__":
    import model.api_2014 as api_2014
    api = api_2014.API()
    response = api.request('/api/2014/classes')
    print(response)