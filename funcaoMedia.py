def lernotas():
    n=float(input('Digite uma nota para o aluno: '))
    return n

def resultado(n1,n2):
    media=(n1+n2)/2
    print('Nota 1: ', n1)
    print('Nota 2: ', n2)
    """
    O uso do end="" é para o print não fazer
    a quebra de linha automaticamente, entao ele
    faz o print e não pula a proxima linha.
    Por isso o resultado do print vai ser
    
    Média:  7.5 Resultado: Aprovado
    """
    print('Média: ',media, 'Resultado: ', end="")
    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

a = lernotas()
b = lernotas()
resultado(a,b)