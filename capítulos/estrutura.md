# Estrutura da classe

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

## Construtores

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

## Atributos e métodos

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
adicionando um novo método `respira`:

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