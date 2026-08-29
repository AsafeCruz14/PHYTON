'''realizar o valor total de horas de um estacionamento, sabedo que o valor por hora é 8 reais'''
Nome_cliente = (input("Digite o nome do usuário:"))
Quantidade_horas = int (input("Informe a quantidade de horas:"))
'''Processo para sabermos o resultado total que o usuário irá pagar para o estacionamento'''
Valor_total = Quantidade_horas * 8
if  Quantidade_horas > 5:
    desconto = Valor_total * 0.10
    Valor_final = Valor_total - desconto
else:
    desconto = 0 
    Valor_final = Valor_total
'''Agora será a saída de todo o nosso algorítimo'''
print("Nome do Usuaário:", Nome_cliente)
print(" Valor total:", Valor_total)
print("Valor final", Valor_final)

    
