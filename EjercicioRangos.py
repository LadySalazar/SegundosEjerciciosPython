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
    print(ejercicioRango(2,21,3))
if __name__ == '__main__':
    main()