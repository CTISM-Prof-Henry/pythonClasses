# Herança

Um recurso interessante do paradigma orientado a 
objetos é a herança. Com ela, podemos reaproveitar
trechos de código-fonte entre diversas subclasses.

Considere as classes Animal e AnimalTerrestre, dos 
exemplos anteriores. Se quiséssemos que AnimalTerrestre 
possuísse os mesmos atributos de Animal (i.e. _nome,
idade, peso_), e mais um atributo _número de patas_,
um código-fonte ingênuo seria o seguinte:

```python
class Animal(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

class AnimalTerrestre(object):
    def __init__(self, nome, idade, peso, n_patas):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.n_patas = n_patas
```

Perceba como estamos repetindo código-fonte que, a rigor,
não precisaria ser repetido. Toda vez que cometemos
este erro, estamos aumentando a probabilidade de que
problemas aconteçam no nosso código!

Felizmente, usando herança, podemos reescrever este
código da seguinte forma:

```python
class Animal(object):
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

class AnimalTerrestre(Animal):
    def __init__(self, nome, idade, peso, n_patas):
        super().__init__(nome, idade, peso)
        self.n_patas = n_patas
```

Perceba como estamos reaproveitando o `__init__` de
Animal dentro do `__init__` de AnimalTerrestre, através
do uso de `super().__init__(nome, idade, peso)`.

Para instanciar um novo objeto da classe AnimalTerrestre,
usamos o seguinte código-fonte:

```python
var2 = AnimalTerrestre('Frida', 1, 7.1, 4)
print('Nome: %s Patas: %d' % (var2.nome, var2.n_patas))
```

A saída do código acima é

```bash
Nome: Frida Patas: 4
```