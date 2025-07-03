arquivo = open('arqText.txt', 'w')
arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica \n')
arquivo.close()

#leitura do arquivo texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

arquivo = open('arqText.txt', 'a+')
arquivo.write('Testeeee')
print(arquivo.read())
arquivo.close()
