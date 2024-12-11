print('Testando versionamento com GIT')

x = input('Qual seu nome?')
print(x)




#Código utilizado na aula para debugar (acharmos o erro):

print('Olá')

def calcular_preco_combo(pizza, refrigerante):

    total = pizza + refrigerante #erro aqui int + str 
    print(total)

calcular_preco_combo(30, 'vinte reais')

print('Programa finalizado')