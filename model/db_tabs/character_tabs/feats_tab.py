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