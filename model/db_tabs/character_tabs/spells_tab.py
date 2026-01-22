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