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