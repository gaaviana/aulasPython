codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True
separador = '--------------------------------------------------------'
tipo = type(salario)

print(salario)
print(tipo)
print(separador)

# tipos de concatenação
print("Código: ", codigo, "|Nome: ", nome, "|O salario atual é de ", salario)
"""no caso da concatenação com sinal de + é 
nescessario converter o valor que não é string 
para o tipo string usando (str)"""
print("Codigo: "+ str (codigo))