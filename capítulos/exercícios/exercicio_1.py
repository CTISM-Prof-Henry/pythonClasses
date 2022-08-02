class Infinito(object):

    def __init__(self, inicio=0, fim=None, passo=None):  # não mexa nesta linha
        """
        Construtor da classe Infinito. Não mexa na assinatura deste método!

        :param inicio: O valor inicial do iterador.
        :param fim: Opcional: o valor final do iterador. Se não for passado, deve assumir que o valor passado para
                    início é o valor final, e que o valor inicial é zero.
        :param passo: Opcional: de quantos em quantos números o iterador irá pular. Se não for passado, deve assumir
                      que passo = 1.
        """
        # TODO apague isto e implemente seu código aqui
        raise NotImplementedError('apague isto e implemente seu código aqui')
        # TODO apague isto e implemente seu código aqui

    def __iter__(self):
        """
        Retorna o iterador deste objeto, que é ele mesmo.
        """
        return self

    def __next__(self):
        # TODO apague isto e implemente seu código aqui
        raise NotImplementedError('apague isto e implemente seu código aqui')
        # TODO apague isto e implemente seu código aqui


def main():
    iterador = Infinito(0, 4, 1)
    count = 0
    while count < 10:
        proximo = next(iterador)
        print(proximo)
        count += 1


if __name__ == '__main__':
    main()
