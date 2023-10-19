import random
import os
from errores import intentos


def normalizar(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def run():
    with open('./DATA.txt' , 'r' , encoding='utf-8') as data:
        lista = [i.strip() for i in data]
 
    palabra = random.choice(lista) 
    palabra = normalizar(palabra)
    palabra_oculta_lista = ['_' for i in range( len(palabra) )  ]
    string_palabra_oculta = "".join(palabra_oculta_lista)
    errores = 0

    mas_de_un_caracter = False
    numerico = False

    while palabra  != string_palabra_oculta and errores < 5:

        os.system("clear")
        print(f'Juguemos ahorcado, adivina la palabra')
        print(f'{intentos(errores)}   \n \n \n  ')
        print( "".join([i+'  ' for i in string_palabra_oculta]))
        print(f' \n \n \n') 
        

        if numerico == True:
            print('!!!!!!! No ingresar numeros !!!!!!!')
            numerico = False
        elif mas_de_un_caracter == True:
            print('!!!!!!! No ingresar mas de una letra por favor !!!!!!!')
            mas_de_un_caracter = False


        letra = input('Presiona una tecla y despues enter    ').lower().strip()


        if letra.isnumeric():
            numerico = True
            continue
        elif len(letra) != 1:
            mas_de_un_caracter = True
            continue


        iterador = 0
        for i in palabra:   
            if i == letra:
                palabra_oculta_lista[iterador] = i
            iterador += 1  
        
        version_anterior = string_palabra_oculta
        string_palabra_oculta = "".join(palabra_oculta_lista)

        if version_anterior == string_palabra_oculta:
            errores += 1



    if palabra == string_palabra_oculta:
        os.system("clear")
        print(f'{intentos(errores)}   \n \n \n  ')
        print(f'Felicidades la palabra  {string_palabra_oculta} es correcta')
    else:
        os.system("clear")
        print(intentos(errores))
        print(f'La palabra era  {palabra}')



if __name__ == '__main__':
    run()

