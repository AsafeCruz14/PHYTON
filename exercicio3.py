cliente = input("Digite o nome do cliente:")
valor = float(input("Digite o valor inicial:"))

def adicionar_taxa():
    global valor
    valor += 20
    adicionar_extra()

def adicionar_extra():
    global valor
    valor += 10

adicionar_taxa()

print(f"Nome: {cliente}")
print(f"Valor final: {valor}")