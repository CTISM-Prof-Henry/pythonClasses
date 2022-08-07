class Ye(object):
    def __init__(self):
        print('colocando ideias na cabeça do Ye')

    def __enter__(self):
        print('entrando na cabeça do Ye')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('saindo na cabeça do Ye')


def main():
    with Ye() as ye:
        print('*Ye está pensando coisas*')
    print('*Ye parou de pensar coisas*')


if __name__ == '__main__':
    main()
