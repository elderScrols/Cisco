income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
    tax = income * 0.18 - 556.02
    # Escreve o resto do código aqui

tax = round(tax, 0)
print("A taxa é: ", tax, "thalers")
