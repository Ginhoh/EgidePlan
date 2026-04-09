
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

