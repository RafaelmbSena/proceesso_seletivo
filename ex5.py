def inverter(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado


s = input("Digite uma string para inverter: ")

print("String invertida: ", inverter(s))