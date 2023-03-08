input("""Hola! Voy a ayudarte a generar una situación imaginaria divertida. Pulsa [ENTER] para continuar.""")

def pregunta(question):
    while True:
        respuesta = input(question) 
        if respuesta == '':
            print('Lo siento, no puedes dejar una pregunta en blanco.')
        else:
            break
    return respuesta

sport = pregunta('Nombra un deporte (verbo).')
famous_person = pregunta('Nombra una persona famosa.')
drunk_verb = pregunta('Nombra algo que harías si estuvieses borracho/a (verbo).')
place = pregunta('Nombra un lugar en el que celebrar una boda (no país).')
transport = pregunta('Nombra un medio de transporte (sustantivo).')
relationship = pregunta('Nombra un tipo de parentesco o relación con alguien.')
movie_trilogy = pregunta('Nombra una trilogía de películas.')
extreme_sport = pregunta('Finalmente, nombra un deporte extremo (verbo en gerundio).')

input('Bien, ya tengo tus resultados! Pulsa [ENTER] para verlos.')

print("""Esta tarde no he ido a {} porque {} dijo que iba a {} en {} y lo quería ver.
 Pero, cuando estuve allí, tuve que irme en {} con mucha urgencia porque a mi {} se le
 había ocurrido ver {} mientras estaba {}, y había acabado en el hospital."""
.format(sport, famous_person, drunk_verb, place, transport, relationship, movie_trilogy, extreme_sport))
 