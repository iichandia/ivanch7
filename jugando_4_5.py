class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        self.estomago = []

    def __call__(self, comida):
        self.estomago.append(comida)

    def asimilar(self):
        if len(self.estomago) > 0:
            return self.estomago.pop(0)

    def __str__(self):
        return ('Animal llamado: {}'.format(self.nombre))


gato = Animal('Cucho', 4)  # Hacemos un gato
perro = Animal('Boby', 4)  # Podemos hacer muchos animales
print(gato.nombre)
print(perro)  # aqui funciona el metodo __str__
gato('pescado')  # aqui le damos pescado al gato usando el metodo __call__
print(gato.estomago)
gato.asimilar()
print(gato.estomago)