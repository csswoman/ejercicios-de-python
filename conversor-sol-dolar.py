menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == '1':


sol = input (" ¿Cuántos soles peruanos tienes?: ")
sol = float(sol)
valor_dolar = 3.50
dolares = sol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")