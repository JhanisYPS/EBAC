import math

# Dados fornecidos
def new_func(aporte_mensal,rendimento_ano,valor_futuro):


# Taxa de juros mensal
    juros_mensal = (1 + rendimento_ano) ** (1/12) - 1

# Função para calcular o número de meses necessários
    n_meses = math.log((valor_futuro * juros_mensal / aporte_mensal) + 1) / math.log(1 + juros_mensal)

# Exibir o número de meses e anos
    anos = n_meses / 12
    meses = n_meses % 12
    return anos,meses

aporte_mensal = 5000 # valor do aporte mensal
rendimento_ano = 0.1530# rendimento anual

valor_futuro = 6000000  # valor objetivo de 6 milhões
anos, meses = new_func(aporte_mensal,rendimento_ano,valor_futuro)

print(f"Tempo necessário para atingir R$ 6 milhões: {int(anos)} anos e {int(meses)} meses.")
valor_futuro = 1000000  # valor objetivo de 6 milhões
anos, meses = new_func(aporte_mensal,rendimento_ano,valor_futuro)
print(f"Tempo necessário para atingir R$ 1 milhão: {int(anos)} anos e {int(meses)} meses.")
valor_futuro = 100000  # valor objetivo de 6 milhões
anos, meses = new_func(aporte_mensal,rendimento_ano,valor_futuro)
print(f"Tempo necessário para atingir R$ 100 mil: {int(anos)} anos e {int(meses)} meses.")
valor_futuro = 60000  # valor objetivo de 6 milhões
anos, meses = new_func(aporte_mensal,rendimento_ano,valor_futuro)
print(f"Tempo necessário para atingir R$ 60 mil: {int(anos)} anos e {int(meses)} meses.")
valor_futuro = 10000  # valor objetivo de 6 milhões
anos, meses = new_func(aporte_mensal,rendimento_ano,valor_futuro)
print(f"Tempo necessário para atingir R$ 10 mil: {int(anos)} anos e {int(meses)} meses.")