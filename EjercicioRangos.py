def ejercicioRango(LimiteInf, LimiteSup, numero):
    list=[]
    cont=0
    for i in range(LimiteInf,LimiteSup+1):
        if numero<=i:
            resto = i%numero
            if resto==0:
                list.append(i)
                cont = cont + 1
    return list
def main ():
    print("Bienvenido al programa de la ejercicio de rango")
    LimiteInf = -1
    while LimiteInf < 0:
        LimiteInf = int(input("por favor ingrese el limite inferior:  "))

    LimiteSup = -1
    while LimiteSup < 0 or LimiteSup<LimiteInf:
        LimiteSup = int(input("por favor ingrese el limite Superior:  "))

    numero=-1
    while LimiteInf>numero or numero>LimiteSup:
        numero = int(input("por favor ingrese el numero:  "))

    print(ejercicioRango(LimiteInf,LimiteSup,numero))

if __name__ == '__main__':
    main()