from datetime import date 
today = date.today()
print("Today's date:", today.strftime("%d/%m/%Y"))
dia = today.fromisocalendar(2024, 25, 3).day #
print("Day:", dia)