somaidade=0
médiaidade=0
maioridadehomem=0
nomevelho=0
totmulher20=0
for c in range(1,5):
    print('----- {}° pessoa -----'.format(c))
    nome=str(input('nome:')).strip()
    idade=int(input('idade:'))
    sexo=input('sexo:')
    somaidade += idade
    if c == 1 and sexo in 'mM':
        maioridadehomem=idade
        nomevelho= nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho = nome
    if sexo in 'fF'and idade < 20:
        totmulher20 += 1
médiaidade=somaidade/4
print('a media de idade do grupo é {:.1f}'.format(médiaidade))
print('o homem mais velho do grupo é o {} ele tem {}'.format(nomevelho,maioridadehomem))
print('ao todo são {} mulheres no grupo com menos de 20 anos'.format(totmulher20))



