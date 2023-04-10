#CHUTE#
''''
# quais as variaveis?
 - VALOR ALEATORIO DE 01 A 10
 - INPUT NUMERO CHUTE
# o que fazer com as variaveis
 - COMPARAR O CHUTE COM O ALETATORIO E EXIBIR SE ESTA ACIMA, ABAIXO OU IGUAL
# quais restrições?
 - O VALOR DEVE SER DE 1 A 10
# qual resultado esperado?
 - INFORMAR SE O USUARIO CHUTOU ACIMA, ABAIXO OU IGUAL AO VALOR ALEATORIO GERADO
#qual a sequencia de passos a ser feito?
'''
import random
valoraleatorio=random.randint(1,10)
acertou=False
while acertou == False:
  chute=int(input("chute valor "))
  if chute>10:
    print("valor invalido")
  elif chute<0:
    print("valor invalido")
  elif chute > valoraleatorio:
    print("valor maior")
  elif chute < valoraleatorio: 
    print("valor menor")
  elif chute == valoraleatorio:
    acertou = True
    print("bem vindo")
