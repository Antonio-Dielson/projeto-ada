from utilitarios.calcular_tempo import tempo
from utilitarios.entrada_data import validar_data
from utilitarios.validar_generic import ValidarDadosGeneric


def criar_registro(): #separar dia, mes e ano
    """Cria um novo registro financeiro com interação do usuário."""

    data = input('data')
    while True:
        tipo = input("Digite o tipo de movimentação (Receita, Despesa ou Investimento): ").capitalize()
        if tipo in ['Receita','Despesa','Investimento']:
            break
        else:
            print('Erro, tipo invalido')
    while True:
        valor = input("Digite o valor: ")
        try:
            valor = float(valor)
            break
        except ValueError:
            print('Digite apenas valores numericos')

    montante = None
    rendimento = None

    if tipo == 'Investimento':
        while True:
            juros = input('Digite o percentual mensal de juros do investimento:')
            try:
                juros = float(juros)
                break
            except ValueError:
                print('Erro, digite apenas números')

        montante_inicial = valor * (1+((juros)/100))**(tempo(data))
        montante = round(montante_inicial, 2)
        rendimento_inicial = montante - valor
        rendimento = round(rendimento_inicial, 2)

    registro = {
        'id': 0,
        'data': data,
        'tipo': tipo,
        'valor': valor if tipo != 'Despesa' else -valor, 
        'montante': montante,
        'rendimento': rendimento}

    return registro
