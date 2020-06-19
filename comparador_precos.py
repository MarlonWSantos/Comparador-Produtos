#
#
#
#   Comparador de preços - Compara valores de produtos
#   Copyright (C) 2020 Marlon W. Santos <marlon.santos.santos@icen.ufpa.br>
#
#
#	
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>


import matplotlib.pyplot as plt
import numpy as np
import sys

cont = 0
preco = []
frete = []
entrega = []
eixoX = []
lista_produtos = []

 #Abre o arquivo
f=open(str(sys.argv[1]),"r")

 #Le linha por linha
for line in f:
  lista = []
  cont += 1
  eixoX.append(cont)
  lista_produtos.append("Produto "+str(cont))
 
  lista = line.strip().split(";")

   #Armazena em listas
  preco.append(float(lista[0].replace(",",".")))
  frete.append(float(lista[1].replace(",",".")))
  entrega.append(float(lista[2].replace(",",".")))

 #Fecha o arquivo
f.close()

 #Converte em array
precos=np.array(preco)
fretes=np.array(frete)
prazos=np.array(entrega)

 #Constroi as barras
plt.bar(eixoX,precos,align="center",color="green")
plt.bar(eixoX,fretes,align="center",color="red",bottom = precos)
plt.bar(eixoX,prazos,align="center",color = "blue", bottom = precos+fretes)

 #Gera as informações no gráfico
plt.xticks(eixoX,lista_produtos)
plt.ylabel("Valor em Dinheiro R$ + Prazo de Entrega")
plt.xlabel("Produtos")
plt.title("Gráfico Comparador de Preços")
plt.legend(("Preço","Frete","Prazo_Entrega"))
plt.show()

