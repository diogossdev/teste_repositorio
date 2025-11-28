while True:
    numero = int(input("Digite um número:"))

    if(numero>=0 and numero<=100):
        if(numero>=70):
            print("Aprovado direto!")

        elif(numero>=40):
            print("Você têm direito a recuperação!")
            while True:
                recuperacao = int(input("Digite a nota da sua recuperação: "))
                if(recuperacao>=50):
                    print(f"Aprovado na final com nota {recuperacao}")
                    break
                else:
                    print(f"Infelizmente você tirou nota {recuperacao} e não passou!")
                    break

        else:
            print("Você reprovou direto!")
            break
        break
    print("Digite um número válido de 0 a 100")
