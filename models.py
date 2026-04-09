from funcoes import past_month_name
import sqlite3

db = sqlite3.connect('gastos.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS gastos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT(100) NOT NULL,
               valor REAL NOT NULL,
               categoria TEXT(50) NOT NULL,
               data DATE NOT NULL
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS fixos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT(100) NOT NULL,
               valor REAL NOT NULL,
               categoria TEXT(50) NOT NULL
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS categoria (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT(100) NOT NULL UNIQUE)
""")


# cursor.execute("""SELECT nome, valor, categoria, data FROM gastos""")
# query = cursor.fetchall()
# for dados in query:
#     valorA, valorB, valorC,valorD = dados
#     print(f'{valorA}: R${valorB:.2f} ({valorC}) {valorD}')



# for linha in range(2, main_page.max_row+1):
#     valorA = main_page[f'A{linha}'].value
#     valorB = float(main_page[f'B{linha}'].value)
#     valorC = main_page[f'C{linha}'].value
#     valorD = main_page[f'D{linha}'].value

#     cursor.execute("""INSERT INTO GASTOS (nome, valor, categoria, data)
#                    VALUES (?, ?, ?, ?)""", (valorA, valorB, valorC, valorD))
# for i in table.sheetnames:
#     page = table[i]
#     for linha in range(2, page.max_row+1):
#         valorA = page[f'A{linha}'].value
#         valorB = float(page[f'B{linha}'].value)
#         valorC = page[f'C{linha}'].value
#         valorD = page[f'D{linha}'].value

#         cursor.execute("""INSERT INTO GASTOS (nome, valor, categoria, data)
#                        VALUES (?, ?, ?, ?)""", (valorA, valorB, valorC, valorD))
        

#cursor.execute("""DELETE FROM gastos""") #Limpa a tabela para evitar duplicação de dados

# cursor.execute(f"""SELECT categoria, SUM(valor) FROM gastos GROUP BY categoria""")
# dados = cursor.fetchall()
def months_():
    cursor.execute("""SELECT data FROM gastos GROUP BY data""")
    dados = cursor.fetchall()
    mes = []
    for data in dados:
        if past_month_name(data[0][3:5:]) not in mes:
            mes.append(past_month_name(data[0][3:5:]))
    return mes


db.commit()
