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