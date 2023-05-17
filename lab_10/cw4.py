from datetime import datetime, timedelta

def wiek(urodziny):
    dzis = datetime.today().date()
    urodziny = datetime.strptime(urodziny, "%Y-%m-%d").date()

    wiekk = dzis.year - urodziny.year
    if dzis.month < urodziny.month or (dzis.month == urodziny.month and dzis.day <urodziny.day):
        wiekk -= 1

    nextu = urodziny.replace(year=dzis.year)
    if dzis > nextu:
        nextu = nextu.replace(year=dzis.year + 1)

    days = (nextu - dzis).days
    
    miesiace = dzis.month-urodziny.month
    if miesiace < 0:
        miesiace = miesiace*(-1)

    print("Dziś masz ",wiekk," lat, ",miesiace," miesięcy i ",dzis.day-urodziny.day," dni")
    print("Do kolejnych urodziny zostało ", days," dni")

urodziny = input("Podaj swoją datę urodzenia w formacie RRRR-MM-DD: ")
wiek(urodziny)
