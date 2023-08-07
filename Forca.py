import random
import os 
import time


listaForcaObjeto = ["computador","xicara", "carro", "copo", "garrafa","celular","faca","Computador","forca" ]
listaForcaFruta = ['abacaxi','banana','manga','beringela','pitaia','melancia','jabuticaba','kiwi','lichia']
listaForcaMarcas = ['apple','sansung','nike',"adidas",'gucci','microsoft','Hocks','xaomi']
continuar = "s"

while continuar in "sS":

    print(5*"-=","FORCA",5*"-=")

    print("__________")
    print("|/       |")
    print("|")
    print("|")
    print("|")

    Palavra = []
    Letras_Erradas = []
    erros = 6

    
    print("escolha uma Tema: ")
    print("1 - frutas ")
    print("2 - objetos ")


    while True:   
        EscolhaClasse = int(input("digite uma das opções: "))    
    
        match EscolhaClasse:
            case 1:
                EscolhaRandom = random.choice(listaForcaFruta)
                break
            case 2:
                EscolhaRandom = random.choice(listaForcaObjeto)
                break
            case 3:
                EscolhaRandom = random.choice(listaForcaMarcas)
                break                

            case _:  #else do case
                print("voce não digitou uma das opções")

    print("voce deseja sortear novamente?")
    


    for i in EscolhaRandom:
        Palavra.append("_")
    print(*Palavra, sep="")


    cont = 1
    while cont ==1:
        tentativa = input(f"digite a letra: ").lower()
        if tentativa not in(Letras_Erradas) and tentativa not in Palavra:
                                                        #index mais prático
            for indice,valor in enumerate(EscolhaRandom): #enumerate pegará a posição(indice) e valor de cada item na lista
                if tentativa == valor:            
                    Palavra.pop(indice)
                    Palavra.insert(indice,tentativa)
                    
            print(*Palavra, sep="")

            if tentativa not in EscolhaRandom:
                
                erros = erros - 1
                Letras_Erradas.append(tentativa)
                print("======= você errou ======")
                match erros:
                    case 5:
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|")
                        print("|")
                    case 4:
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|        |")
                        print("|")
                    case 3:
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|       /|")
                        print("|")
                    case 2: 
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|       /|\\")
                        print("|")
                    case 2: 
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|       /|\\")
                        print("|       /")
                    case 1:
                        print("__________")
                        print("|/       |")
                        print("|        O")       
                        print("|       /|\\")
                        print("|       / \\")

                print(f"======= você tem {erros} chances")
                print(f"======= Letras ja usadas: {Letras_Erradas}")
        else:
            print("essa letra ja foi usada")

        if "_" not in Palavra:
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠛⣙⠛⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣰⠋⣰⣿⠿⠿⢷⣦⡈⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⢠⣦⠀⣴⣿⠃⠀⣶⣦⣤⣁⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⢀⡾⢀⣿⠃⢰⣿⣿⠀⠀⠙⠿⠿⣿⡧⢸⡇⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⣼⠀⣼⡏⢀⣿⣿⣿⣷⣤⣀⣀⡀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⢿⠐⠿⠀⣼⣿⣿⣿⣿⣿⣿⣿⡿⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⢈⡷⠀⣶⣿⣿⠛⠿⣿⣿⣿⣿⠃⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⢸⡅⠸⢿⡿⢃⡄⢠⣤⣬⡿⢃⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠤⠴⢿⣄⠻⠿⢋⣠⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
            print(5*"=-","voce ganhou!!!",5*"=-")
            jogar_novamente2 = input("voce deseja jogar novamente? (S/n):  ")

            if jogar_novamente2 in "s,SS,S,ss,N,n,NN,nn":
                if jogar_novamente2 in "s,S,ss,SS":
                    continuar = "s"
                    cont = 1
                    erros = 6
                    os.system('cls') or None
        
                 
                if jogar_novamente2 in "n,N,nn,NN":
                    print("então tchau")
                    continuar = "n"
                    cont += 1

                    
            else:
                print("voce não digitou uma das opções...")
            break

        if erros == 0:
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣾⠟⡛⠿⠿⣭⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣽⡟⡏⢩⣦⡝⠋⢸⣶⠄⢲⡟⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⡳⣜⢿⣿⣿⣿⣿⣿⣿⣿")       
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡛⢌⢿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠙⠌⣸⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⡿⠉⠉⠉⠉⢿⣿⣿⣿⠏⠉⠉⠉⠉⠉⠆⠄⠁⠄⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⡗⠫⠿⠆⠄⠸⢿⣿⣿⠂⠒⠲⡿⠛⠛⠂⠄⠄⢠⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⡛⣧⡔⠢⠴⣃⣠⣼⣿⣧⡀⠘⢢⣀⠄⠄⠄⠄⠄⢈⠁⢿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠄⠄⠄⣸⠆⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣼⢿⣿⣿⣿⣿⡀⠄⠘⡀⢠⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⡌⠿⣫⣿⣦⠬⢭⣥⣶⣬⣾⣿⢿⣿⡟⠄⢀⣿⣶⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣧⠘⣉⠛⢻⣛⣛⣛⣻⡶⠮⠙⠃⣉⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⡆⠸⣿⣶⢾⣿⣯⣤⣄⣀⣾⡟⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⠟⠿⠿⠿⠿⢿⣷⠄⣿⣿⣎⣹⢻⣿⣿⡿⡿⠁⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⠄⠄⠄⠄⠄⠄⠄⣠⠘⣿⣿⣿⣿⣿⣿⡟⠁⣀⣀⣀⠄⠘⠿⣿⣿⣿⣿⣿⣿⣿")
            print("                                         ")
            print(4*"-=","VOCE PERDEU",4*"-=")
            jogar_novamente = input("voce deseja jogar novamente? (S/n):  ")

            if jogar_novamente in "s,SS,S,ss,N,n,NN,nn":
                if jogar_novamente in "s,S,ss,SS":
                    continuar = "s"
                    cont += 1
                    erros = 6
                    os.system('cls') or None
                if jogar_novamente in "n,N,nn,NN":
                    print("então tchau")
                    continuar = "n"
                    cont += 1

                    break
            else:
                print("voce não digitou uma das opções...")

            

 



    
            
