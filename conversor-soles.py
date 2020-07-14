sol = input (" ¿Cuántos soles peruanos tienes?: ")
sol = float(sol)
valor_dolar = 3.50
dolares = sol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")