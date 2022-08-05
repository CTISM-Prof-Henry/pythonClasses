import pandas as pd


class Album(object):
    def __init__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __str__(self):
        return "Título do álbum não-definido"


def main():
    artista = 'Kanye West'

    nome_albuns = ['The College Dropout', 'Late Registration', 'Graduation', '808s & Heartbreak',
                   'My Beautiful Dark Twisted Fantasy', 'Watch the Throne', 'Yeezus', 'The Life of Pablo', 'ye',
                   'KIDS SEE GHOSTS', 'JESUS IS KING']

    rankings = [4, 5, 2, 10, 1, 8, 6, 3, 9, 7, 11]

    albuns = [Album() for nome, ranking in zip(nome_albuns, rankings)]
    ordenados = list(sorted(albuns))

    df = pd.DataFrame({'Ordem cronológica': albuns, 'Melhor ao pior': ordenados})
    print(df)


if __name__ == '__main__':
    main()
