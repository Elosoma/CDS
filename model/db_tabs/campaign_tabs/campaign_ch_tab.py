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