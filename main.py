pessoa = {
    'Nome':'Michael Oliveira',
    'Idade': 30,
    'Profissão': 'Programador',
    
}

nova_chave = input('Diite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo')
pessoa [nova_chave] = novo_valor

#Exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
    