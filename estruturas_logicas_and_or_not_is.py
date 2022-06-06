"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Opradores unários:
    -not, is
Operadores binários:
    - and, or, is;

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', O valor do booeano é invertido, ou seja, se for True, vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo
"""
ativo = True
logado = False

if ativo:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. por favor, cheque seu e-mail')


# ativo é True?
print(ativo is True)
