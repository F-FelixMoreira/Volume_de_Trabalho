def inserirDistancias():

    global DistMaxBaseGarra, DistMinBaseGarra

    DistMaxBaseGarra = float(input('\nInsira a distância máxima entre o centro da base e a ponta da garra: '))
    DistMinBaseGarra = float(input('\nInsira a distância mínima entre o centro da base e a ponta da garra: '))

    inserirCoordenadas()


def inserirCoordenadas():

    global x,y,z

    x = float(input('\nDigite um valor para x: '))
    y = float(input('Digite um valor para y: '))
    z = float(input('Digite um valor para z: '))

    calculoVolumeDeTrabalho()


def calculoVolumeDeTrabalho():

    tamanhoVetor = round( ((x)**2 + (y)**2 + (z)**2)**(1/2) , 2)      # Tamanho do vetor gerado pelas coordenadas inseridas

    print("\nTamanho do vetor obtido com essas coordenadas: ", tamanhoVetor,"mm.")

    if tamanhoVetor <= DistMaxBaseGarra and tamanhoVetor >= DistMinBaseGarra and z > 0 :

        print('\nValor do raio: %.2f'%tamanhoVetor)
        print('\nFaz parte do volume de trabalho')

    else:

        print('\nValor do raio: %.2f'%tamanhoVetor)
        print('\nNão faz parte do volume de trabalho')

    calcularNovamente = input("\nDeseja inserir novos valores? y/n: ")

    if calcularNovamente == "y":

        inserirDistancias()

    else:
        print("\nPrograma encerrado\n")



inserirDistancias()