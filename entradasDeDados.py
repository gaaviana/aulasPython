fruta = input('Digite o nome de uma fruta: ')
print(fruta)

"""o input sempre vai ser do tipo string, caso
queira uma entrada de dados de outro tipo, temos
que declarar o tipo antes"""

codigo = int(input('Digite o codigo do funcionario: '))
nome = input('Digite o nome do funcionario: ')
salario = float(input('Informe o salario: '))
ativo = True

print("Código: %d "% codigo)
print("Nome: %s "% nome)
print("Salário: %.2f "% salario)
print("Ativo: %r "% ativo)
