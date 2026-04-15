from models import db, cursor

#retornar mês atual
def actual_month():
    from datetime import date
    mes = date.today().month
    if mes == 1: return '01'
    elif mes == 2: return '02'
    elif mes == 3: return '03'
    elif mes == 4: return '04'
    elif mes == 5: return '05'
    elif mes == 6: return '06'
    elif mes == 7: return '07'
    elif mes == 8: return '08'
    elif mes == 9: return '09'
    elif mes == 10: return '10'
    elif mes == 11: return '11'
    elif mes == 12: return '12'

def past_month():
    from datetime import date
    mes = date.today().month
    if mes == 1: return '12'
    elif mes == 2: return '01'
    elif mes == 3: return '02'
    elif mes == 4: return '03'
    elif mes == 5: return '04'
    elif mes == 6: return '05'
    elif mes == 7: return '06'
    elif mes == 8: return '07'
    elif mes == 9: return '08'
    elif mes == 10: return '09'
    elif mes == 11: return '10'
    elif mes == 12: return '11'


def past_month_name(mes):
    if mes == '01': return 'Dezembro'
    elif mes == '02': return 'Janeiro'
    elif mes == '03': return 'Fevereiro'
    elif mes == '04': return 'Março'
    elif mes == '05': return 'Abril'
    elif mes == '06': return 'Maio'
    elif mes == '07': return 'Junho'
    elif mes == '08': return 'Julho'
    elif mes == '09': return 'Agosto'
    elif mes == '10': return 'Setembro'
    elif mes == '11': return 'Outubro'
    elif mes == '12': return 'Novembro'

def choice_month(mes):
    if mes == 'Janeiro': return '01'
    elif mes == 'Fevereiro': return '02'
    elif mes == 'Março': return '03'
    elif mes == 'Abril': return '04'
    elif mes == 'Maio': return '05'
    elif mes == 'Junho': return '06'
    elif mes == 'Julho': return '07'
    elif mes == 'Agosto': return '08'
    elif mes == 'Setembro': return '09'
    elif mes == 'Outubro': return '10'
    elif mes == 'Novembro': return '11'
    elif mes == 'Dezembro': return '12'


#Gastos totais, média, categoria com maior gasto, categoria com menor gasto, comparação com mês anterior
def gastos_total(month):
    
    cursor.execute(f"""SELECT SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%'
""")
    total = cursor.fetchall()
    if total[0][0] == None:
        return 0.0
    else:
        return total[0][0]


def gastos_media(month):
    cursor.execute(f"""SELECT AVG(valor) FROM gastos WHERE data LIKE '%/{month}/%'""")
    media = cursor.fetchall()
    if media[0][0] == None:
        return 0.0
    else:
        return media[0][0]


def categoria_maior(month):
    cursor.execute(f"""SELECT categoria, SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' 
               GROUP BY categoria """)
    dados = cursor.fetchall()
    select = ''
    maior = 0
    for valor in dados:
        categ, sumvalor = valor
        if sumvalor>maior:
            maior = sumvalor
            select = categ
    return select
    


def categoria_menor(month):
    cursor.execute(f"""SELECT categoria, SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' 
               GROUP BY categoria """)
    dados = cursor.fetchall()
    select = ''
    if(len(dados) == 0):
        select = 'Nenhuma categoria'
    else:
        menor = dados[0][1]
        for valor in dados:
            categ, sumvalor = valor
            if sumvalor<float(menor):
                menor = sumvalor
                select = categ

    return select

def comparacao():
    mes_atual = float(gastos_total(actual_month()))
    mes_passado = float(gastos_total(past_month()))
    if mes_atual > mes_passado:
        return f'R${mes_atual - mes_passado:,.2f} superior ao mês passado'
    elif mes_atual < mes_passado:
        return f'R${mes_passado - mes_atual:,.2f} inferior ao mês passado'
    else:
        return f'Mesma quantia acumulada refetente ao mês passado'

def gastos_por_categoria(month, categoria):
   cursor.execute(f"SELECT SUM(valor) FROM gastos WHERE data LIKE '%/{month}/%' AND categoria = '{categoria}'")
   dados = cursor.fetchall()
   return 0 if dados[0][0] == None else dados[0][0]

def months_():
    cursor.execute("""SELECT data FROM gastos GROUP BY data""")
    dados = cursor.fetchall()
    mes = []
    for data in dados:
        if past_month_name(data[0][3:5:]) not in mes:
            mes.append(past_month_name(data[0][3:5:]))
    return mes