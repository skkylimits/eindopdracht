from tabulate import tabulate

art = '''
              ____
             /  __\\
            (  @ @ )
             \\  O /
              \\__/
'''

# Print the stored art
print(art)

width_langste_woord = 30
text1 = "-"
print(text1 * 100)
print("{:<25} {:<35} {:<15} {:<25}".format("Contractnr: NUMMER", "Datum: 14-05-2024", "Vestiging", "WTC"))
print("{:<25} {:<35} {:<15} {:<25}".format("", "", "", "Strawinskylaan"))
print("{:<7} {:<69} {:<25}".format("Klant:", "Achternaam, Voornaam", "POSTCODE PLAATS"))
print("{:<7} {:<10} {:<51}".format("Adres:", "ADRES", ""))
print("{:<7} {:<10} {:<51}".format("", "POSTCODE PLAATS", ""))
print()
print()
print("{:<15} {:<10}".format("Startdatum:", "DATUM"))
print("{:<15} {:<10} {:<30}".format("Inleverdatum:", "DATUM", "-> aantal dagen: DAG"))
print(text1 * 100)
print()
print("FIETSEN:\n")
print("{:<15} {:<35} {:<15} {:<13} {:<20}".format("Fietsnr", "Type", "Model", "Elektrisch", "Prijs per dag"))
print("{:<15} {:<35} {:<15} {:^13} {:>20}".format("1 (Batavus)", "1. (Randstad Racer D)", "Dames", "Ja", "45.00"))
print()
print()
print()
print("TOTAAL\n")

data = [
    ["DAGEN", "DAGPRIJS", "TOTAAL"]
]
headers = ["Aantal dagen", "Prijs per dag", "Totaalbedrag"]
kolombreedte = 25
for row in data:
    formatted_row = [f"{cell:<{kolombreedte}}" for cell in row]
# print(tabulate([headers], colalign=["left"]))
print(tabulate(data, headers=headers, colalign=["right", "right", "right"]))
print("\n" * 3)
print("NB: Je hoeft alleen de gegevens op de juiste plek in het contract te tonen. Het logo, de belijning, de tabellen en de kleuren dienen hier alleen ter illustratie.")