nomeCliente = (input("Digite o nome do cliente:"))
valorProduto = float (input("Digite o valor do produto:"))
quantidadeProduto = int (input("Digite a quantidade do produto:"))
valorTotal = valorProduto * quantidadeProduto
if valorTotal >= 500:
   desconto = valorTotal * 0.15
   ValorFinal = valorTotal - desconto
else:
   desconto = 0
   ValorFinal = valorTotal
print("Nome:",nomeCliente)
print("Valor total:",valorTotal)
print("Valor do desconto:",desconto)
print("Valor final:",ValorFinal)   
   
    