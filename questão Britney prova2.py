letra = 'Oh baby, baby Oh baby, baby, Ah, yeah, yeah OH baby, baby How was I supposed to know?'

letra = letra.replace(' ', ',')
letra = letra.lower()
letra = letra.split(',')

contadores = {}

for palavra in letra:
    if palavra in contadores.keys():
        contadores [palavra] = contadores[palavra] + 1

    else:
        contadores[palavra] = 1

for palavra in contadores.keys():
    print( 'A palavra ', palavra, ' foi repetida ', contadores[palavra], ' vezes')

