MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):

    lista = []    #Lista que almacenará los caracteres traducidos
    contador = 0    #Contador de los espacios seguidos. Al tercero añade un espacio en "lista"
    codigo = list(code)
    print("codigo = " + str(codigo))   #Separamos el código morse en caracteres individuales
    string = ""     #String que almacenará los puntos y rayas que forman una letra

    for char in codigo:
        print("caracter = " + char)
        print(contador)
        if char != " ":
            string = string + str(char)    #Si el caracter es un punto o raya, lo almacena temporalmente en "string" hasta formar una letra
            contador = 0    #Reseteamos el contador de espacios
        else:
            contador = contador + 1    #Contabilizamos el espacio
            if contador == 1:    #Si es el primer espacio, la letra ya está formada
                lista.append(string)
                string = ""    #Reseteamos "String" para que almacene la próxima letra
            elif contador == 2:    #Si es el segundo espacio,no se hace nada, se espera al tercero
                pass
            else:
                lista.append(" ")    #Al ser el tercer expacio, comienza una palabra nueva
                contador = 0    #Reseteamos el contador de espacios
    lista.append(string)
    #return code
    print(lista)
    print("testing 1")

#Este bloque traducirá los caracteres a letras y espacios
    telegrama = []    #Esta lista almacenará el código morse traducido letra a letra

    for unit in lista:
        if str(unit) in MORSE:
            telegrama.append(MORSE[str(unit)])
        else:
            telegrama.append(" ")
    print(telegrama)
    print("testing 2")

#Este bloque convertirá la lista de letras y espacios en una cadena de texto
    cadena = ""

    if telegrama[0].isalpha():
        telegrama[0] = telegrama[0].upper()
    print(telegrama[0])
    for char in telegrama:
        cadena = cadena + char
    print(cadena)
morse_decoder("... --- -- .   - . -..- -")
