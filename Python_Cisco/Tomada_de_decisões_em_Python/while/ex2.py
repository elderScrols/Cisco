#armazene o maior número atual aqui.
largest_number = -999999999999

#Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))

#Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        #Sim, atualize o maior_npumero
        largest_number = number
    #Insira o próximo número
    number = int(input("Digite um número ou digite -1 para parar: "))
    #Imprima o maior número.
    print("O maior núemro é: ", largest_number) 