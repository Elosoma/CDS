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