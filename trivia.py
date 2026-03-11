'''# trivia
# es juego de triviaaa!
# Challenge: Mini Trivia en Python

## Debes crear:
Un archivo llamado `trivia.py`

## Tu programa debe:
- pedir el nombre del jugador
- mostrar una bienvenida
- hacer 4 preguntas
- sumar 1 punto por cada respuesta correcta
- mostrar el nombre y el puntaje final

## Resultado final
- si `puntaje == 4` → **Excelente**
- si `puntaje >= 2` → **Muy bien**
- si no → **Puedes mejorar**

## Recuerda
- trabaja paso a paso
- no hace falta terminar perfecto
- usa Git durante el proceso
- haz varios commits pequeños '''

nombre = input('dime tu nombre: ')
print('bienvenido a esta trivia', nombre) 
preguntas = ['cual es la capital de paraguay?', 'cual es la capital de argentina?', 'cual es la capital de brasil?', 'cual es la capital de uruguay?']

suma = 0
respuesta1 = input(preguntas[0])
if respuesta1 == 'asuncion':
    suma += 1
respuesta2 = input(preguntas[1])
if respuesta2 == 'buenos aires':
    suma += 1
respuesta3 = input(preguntas[2])
if respuesta3 == 'brasilia':
    suma += 1
respuesta4 = input(preguntas[3])
if respuesta4 == 'montevideo':
    suma += 1
if suma == 4: 
    print('Excelente')
elif suma >= 2:
    print('Muy bien')
else:
    print('Puedes mejorar')