dinheiro = float(input())
percentual = float(input())
formula = percentual/100
acrescimo = dinheiro + (formula * dinheiro)
desconto = dinheiro - (formula * dinheiro)
print(f'{acrescimo:.2f}')
print(f'{desconto:.2f}')