class PalabraSecreta:
    ''' Clase que guarda un string sin mucha seguridad.
    '''
    def __init__(self, palabra_clave, frase_secreta):
        self.__palabra_clave = palabra_clave
        self.__frase_secreta = frase_secreta

    def decriptar(self, frase_secreta):
        ''' Solo si la frase_secreta es correcta'''
        if frase_secreta == self.__frase_secreta:
            return self.__palabra_clave
        else:
            return ''

s = PalabraSecreta("animal", "tiene patas")
print(s.decriptar("tiene patas"))
#ASI SI FUNCIONA

s._PalabraSecreta__palabra_clave

