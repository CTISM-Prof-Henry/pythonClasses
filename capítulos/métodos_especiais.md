# Métodos especiais

Considere o seguinte código-fonte base para entender os conceitos que serão explicados neste capítulo:

```python
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
```

## Métodos estáticos

Um método estático é um método que independe do atual estado do objeto. Ou seja, pouco importa quais os atuais valores 
dos atributos de um objeto; o método estático realizará seu processamento independente de seus valores.

Na classe `AnimalTerrestre`, o método `respira` pode ser estático, pois ele sempre retorna o mesmo valor. Podemos 
reescrevê-lo da seguinte forma:

```python
class AnimalTerrestre(Animal):
    def __init__(self, nome, idade, peso, n_patas):
        super().__init__(nome, idade, peso)
        self.n_patas = n_patas

    @staticmethod
    def respira():
        return 'respirando'
```

Perceba que usamos um [decorador](https://github.com/CTISM-Prof-Henry/pythonDecorators) para marcar que este método é 
estático, e que também o parâmetro `self` sumiu da assinatura do método.

## Métodos de classe

Um método de classe é utilizado para criar instâncias de um objeto de outra maneira, que não pelo uso de um 
construtor. Por exemplo: vamos supor que queremos criar uma cópia de um objeto da classe `Animal`. Um método **ruim** 
de fazer isso seria:

```python
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

primeiro = Animal('Frida', 1, 7.1)
segundo = Animal(primeiro.nome, primeiro.idade, primeiro.peso)
```

Com métodos de classe, modificamos a classe animal para ser

```python
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
```

E criamos um objeto-cópia com

```python
primeiro = Animal('Frida', 1, 7.1)
segundo = Animal.from_other(primeiro)
```

Repare novamente que um [decorador](https://github.com/CTISM-Prof-Henry/pythonDecorators) é usado para denotar que 
`from_other` é um método especial (no caso um método de classe), e que seu primeiro parâmetro não mais é `self` (que 
diz respeito a um objeto daquela classe), mas sim `cls` (que se refere à classe do método atual; no caso, `Animal`).

## Outros métodos importantes

Como dito anteriormente, toda classe em Python é herdeira da superclasse `object`. A classe `object` possui diversos 
métodos especiais que podem ser **sobrescritos** (ou seja, reimplementados) por uma classe filha. Cada um destes métodos
especiais possui um comportamento diferente, dependendo do seu uso. Abaixo, estes diversos métodos serão elencados e 
explicados. Você pode ver o **uso** destes métodos no arquivo [pessoas.py](../src/pessoas.py)

| Método (assinatura)   | Uso                      | Descrição                                                                                                               |
|:----------------------|:-------------------------|:------------------------------------------------------------------------------------------------------------------------|
| `__eq__(self, other)` | `p1 == p2`               | Define o comportamento do operador `==`, para verificar se dois objetos são iguais                                      |
| `__ne__(self, other)` | `p1 != p2`               | Igual a `__eq__`, mas para o operador `!=`, que verifica a diferença                                                    |
| `__str__`             | `print(p1)` ou `str(p1)` | Descreve textualmente o objeto                                                                                          |
| `__hash__`            | `hash(p1)`               | Identificador único do objeto. Nenhum outro objeto desta instância que for **diferente** deve ter o mesmo valor de hash |

Existem muitos outros métodos especiais além dos descritos aqui. Você pode aprender mais sobre eles nos 
[Exercícios](exercícios/README.md).