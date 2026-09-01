preco_final = 0

for pedido in range(1, 4):
    numero_produto = int(input("Digite o número do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    preco_unitario = float(input("Digite o preço do produto: "))

    valor_ped = quantidade * preco_unitario
    preco_final = preco_final + valor_ped

print(f"Preço final: R$ {preco_final}")