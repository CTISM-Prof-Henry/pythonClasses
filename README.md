# Classes

## Sumário

* [Introdução](#introdução)
* [Estrutura da classe](capítulos/estrutura.md)
    * [Construtores](capítulos/estrutura.md#construtores)
    * [Atributos e métodos](capítulos/estrutura.md#atributos-e-métodos)
* [Herança](capítulos/herança.md)
* [Métodos especiais](capítulos/métodos_especiais.md)
  * [Métodos Estáticos](capítulos/métodos_especiais.md#métodos-estáticos)
  * [Métodos de Classe](capítulos/métodos_especiais.md#métodos-de-classe)
  * [Outros métodos importantes](capítulos/métodos_especiais.md#outros-métodos-importantes)
* [Código-fonte](#código-fonte)
* [Instruções](#instruções)
* [Exercícios](capítulos/exercícios/README.md)
* [Referências](#referências)

## Introdução

Você muito provavelmente já sabe programar no [paradigma 
imperativo](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_imperativa). 
O paradigma imperativo diz, na forma de ordens (daí o nome 
imperativo), exatamente o que o computador precisa fazer. Um
exemplo de algoritmo imperativo é

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
objeto, queremos dizer que estamos concretizando uma ideia.

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


## Código-fonte

Os códigos-fonte usado nos tutoriais deste repositório estão disponíveis nos seguintes arquivos:

* [animais.py](src/animais.py)
* [animais_v2.py](src/animais_v2.py)
* [pessoas.py](src/pessoas.py)

## Instruções

Você precisará seguir esse passo-a-passo para fazer alguns dos [Exercícios](capítulos/exercícios/README.md). 

1. Clone este repositório na sua máquina
2. [Crie um ambiente virtual do anaconda para trabalhar](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-pela-linha-de-comando)
3. Após ter criado o ambiente virtual e ativado-o, instale
   a biblioteca `twitter`: `pip install twitter==1.19.3`
4. Para executar os códigos-fontes, [abra a pasta deste repositório no Pycharm.](
   https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#usando-pelo-pycharm)


## Referências

* Documentação oficial sobre classes em Python (em português): [link](https://docs.python.org/pt-br/3/tutorial/classes.html)