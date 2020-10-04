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
1.Carregando a imagem original. Resultado.

![imagem original](https://github.com/EduardoRonchi/CountingCoins/blob/master/real_original.jpg)

2.Converter a imagem para escala de cinza:

![Escala de cinza](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_gray.jpg)

3.Aplicar um filtro para borrar a imagem:

![Imagem borrada](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_blurred.jpg)

4.Resultado da aplicação da função HoughCircles:

![Aplicando HoughCircle](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_counter_py.jpg)

5.Resultado final:

![imagem original](https://github.com/EduardoRonchi/CountingCoins/blob/master/image_result/real_result.jpg)

#### Contando Moedas de Dolar

Programa desenvolvido para detectar, destacar e contabilizar o número de moedas de dolar de uma determinada imagem.
O programa foi dividido em 7 etapas: leitura da imagem, conversão para escala de cinza, conversão para padrão binário, aplicação de filtros morfológicos,
aplicação da função SimpleBlobDetector, imprimir a quantidade de moedas detectadas e aplicar a função Circle para desenhar o contorno e o centro de cada moeda.

## Running the program
Existem duas opções para rodar o programa dolar_counter.py, com ou sem imprimir todas as transformações morfológicas usadas para chegar no melhor resultado.
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
1.Leitura da imagem original.

![imagem original](https://github.com/EduardoRonchi/CountingCoins/blob/master/dolar_original.png)

2.Conversão para escala de cinza.

![Escala de cinza](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_gray_image.png)

3.Aplicação de threshold. Aqui foi usado a função cv2.threshold() com valor de threshold de 38. Nesta etapa foram necessárias várias tentativas para encontrar o melhor valor de threshold. O valor de 38 foi o melhor para o restante do programa.

![Imagem Binaria](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_mask_image.png)

4.Aplicar filtros morfológicos. Nessa etapa foram testados diversos filtros morfológicos e foram necessários diversos ajustes no programa para encontrar a melhor solução. Foi a etapa mais desafiadora. Foram testadas diversas transformações morfológicas como, erosion, dilation, opening, closing, tophat e morphological gradient. O melhor resultado foi para dilation com kernel de 5x5 e com três interações.

![Após filtro morfológico](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_dilation.png)

5.Aplicação da função SimpleBlobDetector. Foi necessário aplicar diversos parâmetros para a correta identificação das moedas, parâmetros como area, circularity, convexity e inertia.

![SimpleBlobDetector](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_blob_counter.png)

6.A quantidade de moedas contadas é impressa no terminal, conforme a imagem abaixo.

![Coins Detected](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_python_py.jpg)

7.Aplicação da função Circle para desenhar os centros e contornos das moedas. Para isso foi necessário salvar algums parâmetros da variável keypoints ao rodar a função SimpleBlobDetector.

![Desenho final](https://github.com/EduardoRonchi/CountingCoins/blob/master/image_result/dolar_result.png)
