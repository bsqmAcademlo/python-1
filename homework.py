phrase = open('text.txt', 'r', encoding="utf-8").read().lower()
song = open('songPerreoSola.txt', 'r', encoding="utf-8").read().lower()

str_none = ",;:!'.\n()"

# ! Esta funcion se encarga de contar las palabras de un texto
def home_work_1(param):
    
    # Recorre mi string de caracteres no deseados, y por cada caracter
    # lo que hago es reemplazar en mi string original por espacio vacios
    for char in str_none:
        param = param.replace(char, '')

    #vuelvo mi frase en una lista de string
    words = param.split(' ')

    #creo un dict donde guardare la palabra como key y la cantidad de palabras 
    #que coinciden como value 
    dict_words = {}

    #for que se encarga de llenar mi dict, si existe le suma una al valor,
    #sino lo que hace es crear la llave y el valor 
    for word in words:
        if word in dict_words:
            dict_words[word] +=1
        else:
            dict_words[word] =1

    #for que se encarga de pintar en mi consola
    for key in dict_words:
        value = dict_words[key]
        print(f'{key}:{value}')

# ! Esta funcion se encarga de contar cuantos ey hay en la cancion
def home_work_2(param):
    
    # se podria solucionar con un simple => print(param.count('ey'))
    
    # Recorre mi string de caracteres no deseados, y por cada caracter
    # lo que hago es reemplazar en mi string original por espacio vacios
    for char in str_none:
        param = param.replace(char, ' ')
    
    #vuelvo mi frase en una lista de string
    words = param.split(' ')

    #creo el dict, pero ahora con valores adentro, ya que la logica 
    #al recorrer es diferente
    dict_words = {
        'ey': 0
    }
    
    #palabra a buscar 
    find_pharse = 'ey'

    #en el momento en que la iteracion (word) hace match con find_pharse
    #se le suma uno al value del dict 
    for word in words:
        if(word.strip() == find_pharse):
            dict_words[find_pharse] += 1
    
    #imprimimos por consola 
    print(dict_words)

#MANDAR A LLAMAR LAS FUNCIONES 