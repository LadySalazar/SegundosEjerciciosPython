def saberPalindromo(palabra):
    if str(palabra) == str(palabra)[::-1]:
        resultado=True
    else:
        resultado = False
    return resultado
def main():
    print("Bienvenido al programa por favor ingres una palabra")
    palabra=input("por favor ingrese la palabra:  ")
    if saberPalindromo(palabra)==True:
        print("Es un palidromo")
    else:
        print("No es un palidromo")

if __name__ == '__main__':
    main()