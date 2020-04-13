# Osciloscope
<p align="center">
  <img  src="https://media.giphy.com/media/hSpEmBRHRTqrOHcCw2/giphy.gif" alt="Osciloscope" style="width: 480px; height: 196px; left: 0px; top: 0px; opacity: 0;">
</p>

# Servidor (Produtor)
No servidor temos uma função (**produce**) para produzir valores inteiros aleatórios entre 0 e 1, convertê-los para string e armazená-los num *buffer*.
<p align="center">
  <img  src="https://i.imgur.com/X5YRfnx.png" alt="Osciloscope" style="width: 480px">
</p>

Temos também uma função (**send**) para enviar os valores produzidos através de um *Socket* UDP, onde o buffer é consumido.
<p align="center">
  <img  src="https://i.imgur.com/jkGyOqy.png" alt="Osciloscope" style="width: 480px">
</p>

Na função principal (logo abaixo da função send), o *buffer* é alocado para um tamanho de 10.000 unidades e duas *threads* são alocadas para que as funções *send e produce* possam executar concorrentemente. 

# Cliente (Consumidor)
No cliente temos uma função para realizar a animação (**animate**) em que recebemos os dados do *Socket* UDP, adicionamos a uma lista e plotamos as informações do gráfico (*labels*, título, etc...). Para realizar a atualização do gráfico a função *animate* é chamada periodicamente através da função **FuncAnimation**, que recebe como parâmetro uma função e um intervalo de tempo, que em nosso caso foi ajustado para o menor possível.

<p align="center">
  <img  src="https://i.imgur.com/BVOmMts.png" alt="Osciloscope" style="width: 480px">
</p>

Como mencionado anteriormente, a comunicacao com o cliente é realizado através de um *Socket* UDP, como demonstrado abaixo:  

<p align="center">
  <img  src="https://i.imgur.com/2jWnM1T.png" alt="Osciloscope" style="width: 480px">
</p>

## Dependências
Faça o download da Linguagem de programação **Go** no [site](https://golang.org/) oficial, Siga os passos para instalação através deste [link](https://golang.org/doc/install).  

Siga as instruções para instalação do matplotlib:

```
$ python -m pip install -U pip
$ python -m pip install -U matplotlib
```

## Instruções para execução
```
$ python cliente.py
$ go build server.go
$ ./server
```
# Tecnologias utilizadas
<p align="center">
  <img  src="https://golang.org/lib/godoc/images/footer-gopher.jpg" alt="Osciloscope">
</p>

<p align="center">
  <img  src="https://www.python.org/static/img/python-logo.png" alt="Osciloscope">
</p>

# Contribuidores 
<a href="https://github.com/FalsoMoralista/osciloscope/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=FalsoMoralista/osciloscope" />
</a>

Made with [contributors-img](https://contributors-img.web.app).
