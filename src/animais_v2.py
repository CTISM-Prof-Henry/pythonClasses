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

    @classmethod
    def from_other(cls, other):
        return cls(other.nome, other.idade, other.peso)


class AnimalTerrestre(Animal):
    def __init__(self, nome, idade, peso, n_patas):
        super().__init__(nome, idade, peso)
        self.n_patas = n_patas

    @staticmethod
    def respira():
        return 'respirando'


def main():
    primeiro = Animal('Frida', 1, 7.1)
    segundo = Animal.from_other(primeiro)
    primeiro.print()
    segundo.print()
    print(primeiro.respira())


if __name__ == '__main__':
    main()
