import random
oportunidades = 5

#saludar al usuario
def bienvenida():
    print('Bienvenid@ al juego del ahorcado, trata de adivinar la palabra!\nNo se permiten asentos, números ni símbolos.')

#mostrar cantidad de lineas de palabra
def empezar_juego(lemario):
    palabra = random.choice(lemario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []

# mostrar monito
#def mostrar_escenario(errores):
#    monito = escenario
#    for i in range(0, len(simbolos)):
#       simbolo = simbolos[i] if i < errores else ' '
#       monito = monito.replace(str(i), simbolo)
#   print(monito)

# mostrar letras incorrectas
def mostrar_errores(tablero, letras_incorrectas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()        
    if len(letras_incorrectas) > 0:
        print('Letras incorrectas:', *letras_incorrectas,',')
        print()

# pedir 1 letra al usuario
def pedir_letra(tablero, letras_incorrectas):
    acierto = False
    while not acierto:
        letra = input('Ingresa una letra de la "a" a la "z": ').lower()
        acierto = 'a' <= letra <= 'z' and len(letra) == 1
        if not acierto:
            print('Error!!! \nLa letra tiene que estar entre la "a" y la "z".\nNo se permiten asentos, números ni símbolos.')
        else:
            acierto = letra not in tablero + letras_incorrectas
            if not acierto:
                print('Lo siento, esta letra ya la ingresaste, intenta con otra.')
    return letra

# analizar la letra ingresada
def checar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('Muy bien! Has adivinado esa letra.')
        actualizar_palabra(letra, palabra, tablero)
    else:
        print('Lo siento, esta letra ya la ingresaste, intenta con otra.')
        letras_erroneas.append(letra)

# va de la mano con analizar la letra
def actualizar_palabra(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra

# compueba la palabra/letra
def comprobar_palabra(tablero):
    return '_' not in tablero

# datos que muestra al inicio al usuario
def jugar_al_ahorcado(lemario):

    tablero, palabra, letras_incorrectas = empezar_juego(lemario)
    while len(letras_incorrectas) <= oportunidades:
        #mostrar_escenario(len(letras_incorrectas))
        mostrar_errores(tablero, letras_incorrectas)
        letra = pedir_letra(tablero, letras_incorrectas)
        checar_letra(letra, palabra, tablero, letras_incorrectas)
        if comprobar_palabra(tablero):
            print('Felicidades! Has adivinado la palabra.')
            break
    else:
        print(f'¡Lo siento, has perdido! La palabra era {palabra.upper()}.')
        #mostrar_escenario(len(letras_erroneas))
    mostrar_errores(tablero, letras_incorrectas)

def jugar_otra_vez():
    return input('Gracias por jugar a este juego del ahorcado. \nSi deseas jugar otra vez escribe "s", en caso de no escribe cualquier otra cosa: ')

if __name__ == '__main__':
    lemario = ['abaco','abadernar','abalanzar','abanderado','abanderamiento','abanderar','abastimiento',
    'abecedario','abeja','abejorro','abierto','abobado','abono','abracadabra','abrazar','abreboca','abrelatas',
    'abreviatura','absoluto','abuelo','abundante','arrodillamiento','artesanal','artifice','arzobispo','asador',
    'asamblea','ascenso','bambu','bandera','banquillo','barbacoa','barboquejo','barita','baronesa','bascula',
    'batidora','baya','cicatrizar','cientifico','conciencia','cortapapeles','cosmografico','costilla',
    'desabotonar','despreciar','diecinueve','dialecto','efectivamente','egocentrismo','ejercitante','electrizacion',
    'endivia','espanglish','expulsar','eyector','fachada','fosforo',"fotosintetico","fraguador","galfarro",
    "gallito","gustillo","habitualmente","huitlacoche","intelectualoide","inventariar","jalbegador","kilogrametro",
    "laboralista","ladrillero","litofotograficamente","mango","maniqui","morral","no","noventayochista","olivicultura",
    "omnipotentemente","oscar","pasa","pedagogico","quitacalzon","recaudar","regenerar","salsera","segundo",
    "sudoku","telefax","tijerazo","tintorera","un","urape","vaciedad","vagamundear","vocal","xerografia","xochil",
    "y","yersey","zabullir","zacatecoluquense","zamba","zampon","zapateado",]
    bienvenida()
    while True:
        jugar_al_ahorcado(lemario)
        if jugar_otra_vez() != 's': break