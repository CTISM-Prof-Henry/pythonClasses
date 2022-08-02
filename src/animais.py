class Animal(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def print(self):
        print('Nome: %s Idade: %d Peso: %f' % (
                self.nome, self.idade, self.peso
            )
        )


class AnimalTerrestre(Animal):
    def __init__(self, nome, idade, peso, n_patas):
        super().__init__(nome, idade, peso)
        self.n_patas = n_patas

    def respira(self):
        return 'respirando'


def main():
    var1 = AnimalTerrestre('Frida', 1, 7.1, 4)
    var1.print()
    print(var1.respira())
    print('número de patas:', var1.n_patas)


if __name__ == '__main__':
    main()
