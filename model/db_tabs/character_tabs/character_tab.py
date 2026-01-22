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