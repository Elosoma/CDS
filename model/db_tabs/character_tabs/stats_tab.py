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