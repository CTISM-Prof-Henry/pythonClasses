# pythonClasses

## Sumário

* [Introdução](#introdução)
* [Estrutura da classe](#estrutura-da-classe)
    * [Construtores](#construtores)
    * [Atributos e métodos](#atributos-e-métodos)
* [Herança](#herança)
* [Resumo](#resumo)
* [Código-fonte](#código-fonte)
* [Referências](#referências)

## Introdução

Você muito provavelmente já sabe programar no [paradigma 
imperativo](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_imperativa). 
O paradigma imperativo diz, na forma de ordens (daí o nome 
imperativo), exatamente o que o computador precisa fazer. Um
exemplo de algoritmo imperativo é o seguinte:

```python
nome_animal = 'Frida'
idade_animal = 1
peso_animal = 7.1

print('Nome: %s Idade: %d Peso: %f' % (nome_animal, idade_animal, peso_animal))
```

No caso de, ao invés de apenas um animal, tivéssemos vários 
animais para guardar informações, poderíamos utilizar listas 
para cada uma das características que estamos armazenando:

```python
nomes_animais = ['Frida', 'Poly']
idades_animais = [1, 9]
pesos_animais = [7.1, 15.0]

for i in range(2):
    print(
        'Nome: %s Idade: %d Peso: %f' % (
            nomes_animais[i], 
            idades_animais[i], 
            pesos_animais[i]
        )
    )
```

Perceba que este código não é muito elegante, pois muitas 
informações estão armazenadas em muitos lugares (nomes, idades
e pesos). Além disso, é necessário saber que o índice 0 é usado
para o primeiro animal, o 1 para o segundo, e assim por diante.
O código, portanto, aumenta a probabilidade de que erros ocorram
caso quiséssemos modificar as informações de um animal.

Para tornar o código-fonte mais limpo e eficiente, foi proposto
o [paradigma orientado a objetos](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos).
A orientação a objetos utiliza classes para organizar o 
código-fonte em objetos.

Uma classe é como um tipo genérico. No exemplo acima, podemos 
considerar que existe uma classe Animal. A classe é uma 
entidade abstrata; como se fosse uma ideia. Os objetos são 
**instâncias** de uma determinada classe, são coisas concretas.
Portanto, quando dizemos que estamos instanciando um novo 
objeto, queremos dizer que estamos tornando concreta uma ideia.

O código-fonte acima no paradigma orientado a objetos ficaria
da seguinte forma:

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

animais = [
    Animal('Frida', 1, 7.1),
    Animal('Poly', 9, 15.0),
]

for animal in animais:
    animal.print()
```

Você não precisa entender tudo o que está acontecendo no 
código-fonte agora; apenas repare como o código está mais 
genérico, com menos repetições.

## Estrutura da classe

Uma classe **mínima** tem a seguinte estrutura:

```python
class AnimalTerrestre(object):
    pass
```

Esta classe não faz nada, ela apenas existe. Não é uma classe
muito interessante, mas algumas coisas já podem ser 
interpretadas:

1. Define-se uma nova classe com a palavra reservada `class`
2. O nome da classe deve seguir a convenção [CamelCase](https://pt.wikipedia.org/wiki/CamelCase),
	com a primeira letra de uma nova palavra em maiúscula
3. Entre parênteses, colocados a superclasse da classe atual
(neste exemplo, a classe `object`). 

Uma superclasse é como se fosse uma classe mãe da 
classe atual. Ela possui informações que são **herdadas** pela
subclasse (a classe filha). Em Python, se a classe que estamos
definindo não for herdeira de nenhuma outra, então ela será
herdeira da classe `object`, que é o tipo mais primitivo de 
dados que existe em Python.

### Construtores

Uma classe um pouco menos trivial seria:

```python
class AnimalTerrestre(object):
    def __init__(self, nome):
    	self.nome = nome
```

Aqui nós temos o **construtor** da classe, que é o **método**
`__init__`. Um construtor é responsável por iniciar todos os 
**atributos** de um objeto. Esta classe possui apenas um 
**atributo**, que é o nome do animal terrestre. Nós definimos
o nome de um novo **objeto da classe AnimalTerrestre** passando
o nome desejado por **parâmetro** para o **método** `__init__`:

```python
var1 = AnimalTerrestre('Frida')
print(var1.nome)
```

A saída do código acima é

```bash
Frida
```

### Atributos e métodos

Classes possuem duas entidades: **atributos** e 
**métodos**. Um atributo é uma informação relevante 
que queremos guardar sobre uma classe. Já um método é 
uma forma da classe realizar uma operação sobre aqueles 
atributos. Os equivalentes imperativos de atributos e 
métodos são, respectivamente, variáveis e funções.

O **construtor** é um tipo especial de **método**, 
responsável por inicializar os **atributos** de uma 
classe.

Algumas linguagens de programação, como C++, possuem
também um **destrutor**, responsável por liberar a 
memória que foi previamente alocada para armazenar os 
atributos. Como Python faz uso de um 
[garbage collector](https://pt.wikipedia.org/wiki/Coletor_de_lixo_(inform%C3%A1tica)),
esse recurso não é necessário.

Uma classe pode ter quantos atributos e métodos for 
desejado. Podemos estender a classe AnimalTerrestre
adicionando um novo método, `respira`:

```python
class AnimalTerrestre(object):
    def __init__(self, nome):
        self.nome = nome

    def respira(self):
        return 'respirando'
```

Repare que a sintaxe é diferente para usar o método
`respira`, do que era para usar o construtor:

```python
var1 = AnimalTerrestre('Frida')
print(var1.nome)
print(var1.respira())
```

A saída do código acima é

```bash
Frida
respirando
```

Métodos podem ter um ou mais parâmetros. O primeiro 
parâmetro de um método sempre é `self`, que é o próprio
objeto que estamos trabalhando no momento atual, se 
estivermos dentro do escopo da classe.

Pense no parâmetro `self` como se fosse alguém 
empurrando um barco, para logo depois pular dentro
deste mesmo barco. No exemplo acima, `var1` no escopo
**fora** da classe é o `self` de **dentro** do escopo
da classe. Ou seja, `var1` não apenas chama o método
`respira`, como se passa como parâmetro para este 
mesmo método.

## Herança

Um recurso interessante do paradigma orientado a 
objetos é a herança. Com ela, podemos reaproveitar
trechos de código-fonte entre diversas subclasses.

Considere as classes Animal e AnimalTerrestre, dos 
exemplos anteriores. Se quiséssemos que AnimalTerrestre 
possuísse os mesmos atributos de Animal (i.e. nome,
idade, peso), e mais um atributo número de patas,
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
        super(Animal, self).__init__()
        self.n_patas = n_patas
```

Perceba como estamos reaproveitando o `__init__` de
Animal dentro do `__init__` de AnimalTerrestre, através
do uso de `super(Animal, self).__init__()`.

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

## Resumo

## Código-fonte

## Referências

* Documentação oficial sobre classes em Python (em português): [link](https://docs.python.org/pt-br/3/tutorial/classes.html)