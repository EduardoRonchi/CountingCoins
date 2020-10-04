## Contando Moedas 
### Desafio de Visão Computacional
#### Contando Moedas de Real
Programa desenvolvido para detectar, destacar e contar o número de moedas apresentadas em uma imagem.
 O programa é dividido em 5 etapas: Leitura da imangem, converção para escala de cinza, aplicação de um filtro para borrar a imagem, aplicar a função HoughCircles para contar as moedas e desenhar na imagem original o contorno e o centro.

## Rodando o programa
```
$ python real_counter.py
```
##Resultados obtidos:
1. Carregando a imagem original. Resultado:
'colocar imagem aqui'

2. Converter a imagem para escala de cinza:
'colocar imagem aqui'

3. Aplicar um filtro para borrar a imagem:
'colocar imagem aqui'

4. Resultado da aplicação da função HoughCircles:
'colocar imagem aqui'

5. Resultado final:
'Colocar Imagem aqui'

#### Contando Moedas de Dolar

Programa desenvolvido para detectar, destacar e contabilizar o número de moedas de dolar de uma determinada imagem.
O programa foi dividido em 7 etapas: leitura da imagem, conversão para escala de cinza, conversão para padrão binário, aplicação de filtros morfológicos,
aplicação da função SimpleBlobDetector, imprimir a quantidade de moedas detectadas e aplicar a função Circle para desenhar o contorno e o centro de cada moeda.

## Running the program
Existem duas opções para rocar o programa dolar_counter.py, com ou sem imprimir todas as transformações morfológicas usadas para chegar no melhor resultado.
Executar:
```
$ python dolar_counter.py
```
para imprimir na tela somente a melhor transformação morfológica ou 
```
$ python real_counter.py morph
```
para imprimir na tela todas as transformações morfológicas.

##Resultados obtidos:
1. Leitura da imagem:
![imagem original](http://url/to/img.png)

2. Conversão para escala de cinza:
'inserir imagem'

3. Aplicação de threshold. Aqui foi usado a função '''cv2.threshold''' com valor de threshold de 38.
'imagem do resultsss'

4. Aplicar filtros morfológicos. Nessa etapa foram testados diversos filtros morfológicos e foram necessários diversos ajustes no programa para encontrar a melhor solução. Foi a etapa mais desafiadora do desafio.
'inserir imagem'

5. Aplicação da função SimpleBlobDetector:
'insrir imagem'

6. Imprimir no terminal a contagem das moedas:
'inserir imagem do terminal'

7. Aplicação da função Circle para desenhar os centros e contornos das moedas:
'inserir imagem' 
