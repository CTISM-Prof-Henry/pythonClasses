# Exercícios

## Instruções

Para cada exercício, existe um arquivo _template_ na pasta 
[pythonClasses/capítulos/exercícios](.), com o nome `exercício_<número>.py`, onde `<número>` é o número
do exercício (por exemplo, `exercício_1.py` para o primeiro exercício). Da mesma forma, existe um arquivo com o 
**gabarito** daquele exercício n o arquivo `gabarito_<número>.py` (por exemplo, `gabarito_1.py` para o gabarito do 
primeiro exercício).

Você **pode e deve** modificar os arquivos _template_, pois isto faz parte da resolução dos exercícios, mas deve deixar 
os gabaritos inalterados.

## Enunciados

1. Usando o [código-fonte disponibilizado](exercicio_1.py), crie um iterator infinito. O iterador infinito recebe três 
   parâmetros:
   * um valor inteiro de início; 
   * um valor inteiro de fim; 
   * e um passo (também inteiro). 
   
   O iterador infinito irá percorrer os números inteiros do início ao fim, pulando `passo` números. Uma vez que o 
   valor-fim for alcançado, os números deverão "dar a volta", como demonstrado no exemplo abaixo.

   A saída esperada para o código-fonte que está em [exercício_1.py](exercicio_1.py) é
   
   ```
   0
   1
   2
   3
   0
   1
   2
   3
   0
   1
   ```

2. Usando os métodos `__enter__` e `__exit__`, e o [código-fonte disponibilizado](exercicio_3.py), crie um **contexto**. 
   Um contexto é usado junto com o comando `with` para manipular corretamente a abertura e fechamento. Neste exercício, 
   você fará uso de uma biblioteca auxiliar para baixar os tweets do mestre Ye nos últimos 5 dias.
3. Crie uma classe `Album`. A classe álbum deverá possuir **no mínimo** os atributos `nome` e `artista`. Crie 11 
   instâncias da classe `Album`, uma para cada Álbum do Kanye West. Sobrescreva os métodos `__ne__`, `__eq__`, `__ge__`, 
   `__gt__`, `__le__`, `__lt__`, e `__str__`. Quando rodar o código de [exercicio_3.py](exercicio_3.py), a saída na tela
   deverá ser a seguinte:

   ```
                        Ordem cronológica                     Melhor ao pior
    0                 The College Dropout  My Beautiful Dark Twisted Fantasy
    1                   Late Registration                         Graduation
    2                          Graduation                  The Life of Pablo
    3                   808s & Heartbreak                The College Dropout
    4   My Beautiful Dark Twisted Fantasy                  Late Registration
    5                    Watch the Throne                             Yeezus
    6                              Yeezus                    KIDS SEE GHOSTS
    7                   The Life of Pablo                   Watch the Throne
    8                                  ye                                 ye
    9                     KIDS SEE GHOSTS                  808s & Heartbreak
    10                      JESUS IS KING                      JESUS IS KING
   ```