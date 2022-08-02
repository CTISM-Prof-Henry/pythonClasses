class Pessoa(object):

    def __init__(self, nome, idade, profissao):
        """
        Construtor da classe Pessoa.

        :param nome: O nome da pessoa.
        :param idade: A idade da pessoa.
        :param profissao: A sua profissão.
        """
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __eq__(self, other):
        """
        Este método é invocado quando usamos o sinal == entre dois objetos da classe Pessoa,
        ou então entre um objeto da classe pessoa e outro objeto qualquer (e.g. int, float).

        :param other: Item que será comparado com a instância atual.
        :return: True se os dois objetos forem iguais, False em caso contrário
        """
        if isinstance(other, Pessoa):
            return \
                (self.nome == other.nome) and \
                (self.idade == other.idade) and \
                (self.profissao == other.profissao)
        return False

    def __ne__(self, other):
        """
        Este método é invocado quando usamos o sinal != entre dois objetos da classe Pessoa,
        ou então entre um objeto da classe pessoa e outro objeto qualquer (e.g. int, float).

        :param other: Item que será comparado com a instância atual.
        :return: True se os dois objetos forem diferentes, False em caso contrário
        """
        if isinstance(other, Pessoa):
            return \
                (self.nome != other.nome) or \
                (self.idade != other.idade) or \
                (self.profissao != other.profissao)
        return True

    def __str__(self):
        """
        Este método é invocado quando usamos str(instancia) ou então print(instancia)
        :return: A string que descreve a instãncia atual
        """
        return 'Nome: {0}\t Idade: {1}\t Profissão: {2}'.format(self.nome, self.idade, self.profissao)

    def __hash__(self) -> int:
        """
        Este método é invocado quando usamos hash(instancia). É um identificador único deste objeto. Se dois objetos
        da classe Pessoa forem diferentes, eles devem obrigatoriamente ter valores de hash diferentes.
        :return: Um número inteiro com a hash do objeto atual.
        """
        return hash(self.nome + str(self.idade) + self.profissao)


def main():
    p1 = Pessoa('henry', 30, 'professor')
    p2 = Pessoa('joselito', 30, 'vagabundo')
    p3 = Pessoa('henry', 30, 'professor')

    print('p1: ', p1)
    print('p2: ', p2)
    print('p3: ', p3)
    print()
    print('             p1 == p2?', p1 == p2)  # usa o método __eq__
    print('             p1 != p2?', p1 != p2)  # usa o método __ne__
    print('              hash(p1)', hash(p1))
    print('               str(p1)', str(p1))
    print('hash(p1) == hash(p2)? ', hash(p1) == hash(p2))
    print('hash(p1) == hash(p3)? ', hash(p1) == hash(p3))


if __name__ == '__main__':
    main()
