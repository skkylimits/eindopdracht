import json
import mysql.connector

# Replace the values with your actual database connection details
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Inloggen01",
    database="mydb"
)

# Data
klanten = [
        ["Klantnummer", "Voornaam", "Achternaam", "Adres", "Postcode", "Woonplaats", "Bankrekeningnummer"],
        [1, "Mikey", "Rojas", "Dam", "1012JS", "Amsterdam", 'NLABNA001'],
        [2, "Jan", "Jantjes", "Leidseplein", "3010WW", "Rotterdam", 'NLING0002'],
        [3, "Peter", "Petersen", "Rembrandtplein", "2012WW", "Den Haag", 'NLRABO003']
    ]

fietsen = [
    ["Fietsnummer", "Merk", "Model", "Fietstype", "Elektrisch", "Dagprijs", "Aankoopdatum"],
    [101, "Gazelle", "CityZen", "Stadsfiets", True, 15.0, "2022-01-01"],
    [102, "Trek", "FX 3 Disc", "Hybride", False, 12.0, "2022-02-15"],
    [103, "Cortina", "E-U4", "Elektrische fiets", True, 20.0, "2021-12-10"]
]

locaties = [
    ["locatienummer", "Vestigingsnaam", "Adres", "Postcode", "Plaats"],
    [201, "Amsterdam Centraal", "Stationsplein 9", "1012 AB", "Amsterdam"],
    [202, "Rotterdam Zuid", "Laan op Zuid 393", "3071 AA", "Rotterdam"],
    [203, "Den Haag Centrum", "Spui 68", "2511 BT", "Den Haag"]
]

contracten = [
    ["Contractnummer", "Vestigingsnaam", "Klantnummer", "Startdatum", "Inleverdatum"],
    [301, "Amsterdam Centraal", 1, "2022-03-01", "2022-03-10"],
    [302, "Rotterdam Zuid", 2, "2022-02-20", "2022-03-05"],
    [303, "Den Haag Centrum", 3, "2022-01-15", "2022-01-25"],
    [303, "Utrecht Centrum", 1, "2022-03-25", "2022-09-23"]
]

# Functies
def toon_menu():
    print("\n"*9)
    print("+------------------------------------+")
    print("|                                    |")
    print("|     1 Toevoegen Klant              |")
    print("|     2 Klant Wijzigen               |")
    print("|     3 Klant Verwijderen            |")
    print("|     4 Klant Zoeken                 |")
    print("|     5 Fiets Toevoegen              |")
    print("|     6 Contract Opstellen           |")
    print("|     7 Contract Printen             |")
    print("|     8 Overzicht Alle Gegegevens    |")
    print("|     9 Programma Beindigen          |")
    print("|                                    |")
    print("+------------------------------------+")

def toevoegen_klant():
    # Vraag om input van de gebruiker
    klantnummer = genereer_klantnummer()
    voornaam = input("Voer voornaam in: ")
    tussenvoegsel = input("Voer tussenvoegsel in: ")
    achternaam = input("Voer uw achternaam in: ")
    straat = input("Voer uw adres in: ")
    huisnummer = input("Voer uw huisnummer in: ")
    postcode = input("Voer uw postcode in: ")
    woonplaats = input("Voer uw woonplaats in: ")
    categorie = input("Voer uw categorie in: ")
    bankrekeningnummer = input("Voer bankrekeningnummer in: ")
    nieuwe_klant = [int(klantnummer), voornaam, achternaam, straat, postcode, woonplaats, bankrekeningnummer]

    ###############################
    # Voeg klant toe aan de lijst #
    ###############################
    klanten.append(nieuwe_klant)
    print(f"Nieuwe klant met {klantnummer} succesvol toegevoegd aan lijst!")

    ############################
    # Voeg klant toe aan de db #
    ############################

    # Definieer de SQL-query's met behulp van f-strings
    insert_klant_query = f"INSERT INTO Klanten (idKlanten, Voornaam, Tussenvoegsel, Achternaam) VALUES ('{klantnummer}', '{voornaam}', '{tussenvoegsel}', '{achternaam}')"
    insert_adres_query = f"INSERT INTO Adres (idAdres, Postcode, Huisnummer, Straat, Plaats, Categorie) VALUES ('{klantnummer}', '{postcode}', '{huisnummer}', '{straat}', '{woonplaats}', '{categorie}')"

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    try:
        # Voer de eerste query uit om de klantgegevens in te voegen
        mycursor.execute(insert_klant_query)

        # Voer de tweede query uit om de adresgegevens in te voegen
        mycursor.execute(insert_adres_query)

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        print("Nieuwe klant succesvol toegevoegd aan de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het toevoegen van de klant:", e)
        mydb.rollback()

    # Als je wilt controleren of de klant correct is toegevoegd, kun je bijvoorbeeld de ID van de laatst toegevoegde rij afdrukken
    print("Klant toegevoegd aan de database met ID van de laatst toegevoegde klant:", mycursor.lastrowid)

def toon_alle_gegevens_uit_lijst():
    alle_gegevens = {
        "klanten": {},  # Maak een lege dictionary voor klanten
        "fietsen": {},  # Maak een lege dictionary voor fietsen
        "locaties": {}  # Maak een lege dictionary voor locaties
    }

    # Loop door elke klant in de lijst van klanten en sla eerste headerrij over
    for klant in klanten[1:]:
        klantnummer = klant[0]
        klant_naam = f"{klant[1]} {klant[2]}"

        # Maak een dictionary voor de huidige klant
        klant_dict = {
            "Klantnummer": klantnummer,
            "Voornaam": klant[1],
            "Achternaam": klant[2],
            "Adres": klant[3],
            "Postcode": klant[4],
            "Woonplaats": klant[5],
            "Bankrekeningnummer": klant[6],
            "Contracten": []  # Maak een lege lijst voor contracten van deze klant
        }

        # Voor elke contract in de lijst van contracten
        for contract in contracten[1:]:
            if contract[2] == klantnummer:
                klant_dict["Contracten"].append({
                    "Contractnummer": contract[0],
                    "Startdatum": contract[3],
                    "Inleverdatum": contract[4]
                })

        # Voeg de klant toe aan de klanten dictionary
        alle_gegevens["klanten"][klant_naam] = klant_dict

    for fiets in fietsen[1:]:
        fiets_naam = f"{fiets[1]} {fiets[2]}"
        fiets_dict = {
            "Fietsnummer": fiets[0],
            "Merk": fiets[1],
            "Model": fiets[2],
            "Fietstype": fiets[3],
            "Elektrisch": fiets[4],
            "Dagprijs": fiets[5],
            "Aankoopdatum": fiets[6],
        }

        # Voeg de klant toe aan de klanten dictionary
        alle_gegevens["fietsen"][fiets_naam] = fiets_dict

    for locatie in locaties[1:]:
        locatie_naam = f"{locatie[1]}"
        locatie_dict = {
            "Locatienummer": locatie[0],
            "Vestigingnaam": locatie[1],
            "Adres": locatie[2],
            "Postcode": locatie[3],
            "Plaats": locatie[4],
        }

        # Voeg de klant toe aan de klanten dictionary
        alle_gegevens["locaties"][locatie_naam] = locatie_dict


    # Print de klantgegevens als een dictionary
    print(json.dumps(alle_gegevens, indent=4))

def toon_alle_gegevens_uit_db(): 
    # Define the SQL query to select all data from the "sporthal" table in the "Basketbal" database
    fetch_query = 'SELECT * FROM Klanten'

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Execute the SQL query
    mycursor.execute(fetch_query)

    # Fetch all the results from the executed query
    result = mycursor.fetchall()

    # Iterate over the results and print each row
    for db_klanten in result:
        print(db_klanten)

def verwijderen_klant(klantnummer):
    ################################
    # Verwijder klant uit de lijst #
    ################################
    for klant in klanten:
        for item in klant:
            if klantnummer == item:
                print(klant)
                index = klanten.index(klant)
                klanten.pop(index)
                print(f'klant succesvol verwijderd met klantnummer {klantnummer}')

    #############################
    # Verwijder klant uit de db #
    #############################

    # Maak een SQL-query om de klant te verwijderen
    delete_query = f"DELETE FROM Klanten WHERE idKlanten = '{klantnummer}'"

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    try:
        # Voer de DELETE-query uit om de klant te verwijderen
        mycursor.execute(delete_query)

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        print(f"Klant met klantnummer {klantnummer} succesvol verwijderd uit de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het verwijderen van de klant:", e)
        mydb.rollback()

def zoeken_klant():
    ##########################
    # Zoek klant in de lijst #
    ##########################
    
    # Vraag de gebruiker om een deel van de achternaam om te zoeken
    deel_achternaam = input("Voer een deel van de achternaam in om te zoeken: ")

    # Loop through each klant in klanten
    for klant in klanten:
        # Check if the input substring is in the lowercase version of the last name
        if deel_achternaam.lower() in klant[2].lower():
            # Print the klant sublist
            print(klant)
            # Exit the loop after finding the first match
            break
    #############################
    # Zoek klant in de database #
    #############################

    # Definieer de SQL-query's met behulp van f-strings
    # Maak een cursor object om SQL-query's uit te voeren
        mycursor = mydb.cursor()
        
        # Definieer de SQL-query met behulp van een f-string
        query = f"SELECT * FROM klanten WHERE achternaam LIKE '%{deel_achternaam}%'"

        # Voer de query uit
        mycursor.execute(query)
        
        # Haal alle overeenkomende records op
        klanten = mycursor.fetchall()
        
        if klanten:
            for klant in klanten:
                print("Klant ID:", klant[0])
                print("Naam:", klant[1])
                print("Email:", klant[2])
                # Je kunt andere klantgegevens afdrukken zoals nodig
        else:
            print(f"Geen klant gevonden met de naam", {deel_achternaam})
            
# Utility
def toon_alle(data):
    ## Find maximum width for each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print formatted data
    for row in data:
        for item, width in zip(row, column_widths):
            print(f"{str(item):<{width}}", end="\t")  # Left-align each item within its column
        print()  # Move to the next row

def vind_hoogste_nummer(data, koprij):
    # Initialiseer het hoogste nummer met een waarde van nul
    hoogste_nummer = 0

    # Itereer door elke rij in de gegevens
    for rij in data:
        # Controleer of de huidige rij de koprij is
        if rij[0] == koprij:
            continue  # Sla de koprij over
        
        nummer = rij[0]
        if nummer > hoogste_nummer:
                hoogste_nummer = nummer

    return hoogste_nummer

def genereer_klantnummer():
    hoogste_klantnummer = vind_hoogste_nummer(klanten, "Klantnummer")
    return hoogste_klantnummer + 1

def genereer_contractnummer():
    hoogste_contractnummer = vind_hoogste_nummer(contracten, "Contractnummer")
    return hoogste_contractnummer + 1

def genereer_fietsnummer():
    hoogste_fietsnummer = vind_hoogste_nummer(fietsen, "Fietsnummer")
    return hoogste_fietsnummer + 1

# Program
def main():
    while True:
        toon_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            print("Programma beëindigen. Tot de volgende keer!")
            break
        elif choice == "1":
            toevoegen_klant()
        elif choice == "2":
            toon_alle(klanten)
        elif choice == "3":
            klantnummer = int(input("Voer het klantnummer in dat moet worden verwijderd: "))
            verwijderen_klant(klantnummer)
        elif choice == "4":
            print('8')
        elif choice == "5":
            print('5')
            zoeken_klant()
        elif choice == "6":
            print('6')
        elif choice == "7":
            print('Contract tonen')
        elif choice == "8":
            toon_alle_gegevens_uit_lijst()
            toon_alle(klanten)
            toon_alle_gegevens_uit_db()

        else:
            print("Ongeldige keuze. Probeer een nummer optie tussen 0 en 9.")
            continue  # Continue to the next iteration of the loop if the choice is invalid

if __name__ == "__main__":
    main()