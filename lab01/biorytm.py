from datetime import datetime
import math

def calculate_days(year, month, day):
    birth_date = datetime(year, month, day)
    today = datetime.now()
    difference = today - birth_date
    return difference.days

def calculate_physical_biorhythm(days):
    return math.sin((2 * math.pi / 23) * days)

def calculate_emotional_biorhythm(days):
    return math.sin((2 * math.pi / 28) * days)

def calculate_intelectual_biorhythm(days):
    return math.sin((2 * math.pi / 33) * days)

def get_user_info():
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia: "))
    day = int(input("Podaj dzień urodzenia: "))
    return name, year, month, day

def greet_user(name, days):
    print(f"Witaj, {name}! Dzisiaj jest {days} dzień Twojego życia.")

def checkIfBetter(days):
    calculate_physical_biorhythm(days+1)
    calculate_emotional_biorhythm(days+1)
    calculate_intelectual_biorhythm(days+1)

    if calculate_physical_biorhythm(days+1) > calculate_physical_biorhythm(days) or calculate_emotional_biorhythm(days+1) > calculate_emotional_biorhythm(days) or calculate_intelectual_biorhythm(days+1) > calculate_intelectual_biorhythm(days):
        print("Nie martw się, jutro będzie lepiej!")


def main():
    # get_user_info()
    name, year, month, day = get_user_info()
    days = calculate_days(year, month, day)
    greet_user(name, days)
    physical = calculate_physical_biorhythm(days)
    emotional = calculate_emotional_biorhythm(days)
    intelectual = calculate_intelectual_biorhythm(days)
    print(f"Twoje biorytmy na dzisiaj to: ")
    print(f"fizyczny: {physical}")
    print(f"emocjonalny: {emotional}")
    print(f"intelektualny: {intelectual}")
    checkIfBetter(days)

    if physical or emotional or intelectual < -0.5:
        print("oooo szkoda")
    
    if physical or emotional or intelectual > 0.5:
        print("Tak trzymaj! Dzisiaj jest Twój dzień!")



if __name__ == "__main__":
    main()

# 23 min
    
# ChatGPT version
    
# from datetime import datetime
# import math

# def calculate_days(year, month, day):
#     birth_date = datetime(year, month, day)
#     today = datetime.now()
#     difference = today - birth_date
#     return difference.days

# def calculate_physical_biorhythm(days):
#     return math.sin((2 * math.pi / 23) * days)

# def calculate_emotional_biorhythm(days):
#     return math.sin((2 * math.pi / 28) * days)

# def calculate_intelectual_biorhythm(days):
#     return math.sin((2 * math.pi / 33) * days)

# def get_user_info():
#     name = input("Podaj swoje imię: ")
#     year = int(input("Podaj rok urodzenia: "))
#     month = int(input("Podaj miesiąc urodzenia: "))
#     day = int(input("Podaj dzień urodzenia: "))
#     return name, year, month, day

# def greet_user(name, days):
#     print(f"Witaj, {name}! Dzisiaj jest {days} dzień Twojego życia.")

# def main():
#     # get_user_info()
#     name, year, month, day = get_user_info()
#     days = calculate_days(year, month, day)
#     greet_user(name, days)
#     physical = calculate_physical_biorhythm(days)
#     emotional = calculate_emotional_biorhythm(days)
#     intelectual = calculate_intelectual_biorhythm(days)
#     print(f"Twoje biorytmy na dzisiaj to: ")
#     print(f"fizyczny: {physical}")
#     print(f"emocjonalny: {emotional}")
#     print(f"intelektualny: {intelectual}")

#     if physical < -0.5 or emotional < -0.5 or intelectual < -0.5:
#         print("Nie martw się, jutro będzie lepiej!")

#     if physical > 0.5 or emotional > 0.5 or intelectual > 0.5:
#         print("Tak trzymaj! Dzisiaj jest Twój dzień!")




# if __name__ == "__main__":
#     main()

# # ChatGPT on its own
    
# import datetime
# import math

# def oblicz_dni_zycia(data_urodzenia):
#     dzis = datetime.datetime.now()
#     roznica = dzis - data_urodzenia
#     return roznica.days

# def oblicz_biorytmy(dni_zycia):
#     # Stałe okresów dla biorytmów
#     fizyczny = 23
#     emocjonalny = 28
#     intelektualny = 33

#     # Obliczenia
#     fizyczny_wynik = math.sin(2 * math.pi * dni_zycia / fizyczny)
#     emocjonalny_wynik = math.sin(2 * math.pi * dni_zycia / emocjonalny)
#     intelektualny_wynik = math.sin(2 * math.pi * dni_zycia / intelektualny)

#     return fizyczny_wynik, emocjonalny_wynik, intelektualny_wynik

# def main():
#     imie = input("Podaj swoje imię: ")
#     rok_urodzenia = int(input("Podaj rok urodzenia (np. 1990): "))
#     miesiac_urodzenia = int(input("Podaj miesiąc urodzenia (1-12): "))
#     dzien_urodzenia = int(input("Podaj dzień urodzenia: "))
    
#     data_urodzenia = datetime.datetime(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
#     dni_zycia = oblicz_dni_zycia(data_urodzenia)
    
#     fizyczny, emocjonalny, intelektualny = oblicz_biorytmy(dni_zycia)
    
#     print(f"Cześć {imie}! Dzisiaj jest {dni_zycia} dzień Twojego życia.")
#     print("Twoje biorytmy na dzisiaj to:")
#     print(f"  Fizyczny: {fizyczny:.4f}")
#     print(f"  Emocjonalny: {emocjonalny:.4f}")
#     print(f"  Intelektualny: {intelektualny:.4f}")

# if __name__ == "__main__":
#     main()


