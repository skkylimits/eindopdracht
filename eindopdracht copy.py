import json
import mysql.connector
from datetime import datetime

#####################################
#           DB Connection           #
#####################################
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Inloggen01",
    database="mydb"
)
mycursor = mydb.cursor()
#############################
#           Data            #
#############################
klanten = [
        ["Klantnummer", "Voornaam", "Achternaam", "Adres", "Postcode", "plaats", "Bankrekeningnummer"],
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
    [202, "WTC", "Laan op Zuid 393", "1071 AA", "Amsterdam"],
    [203, "NDSM", "Spui 68", "1012 BT", "Amsterdam"]
]

contracten = [
    ["Contractnummer", "Klantnummer", "Vestigingsnaam", "Startdatum", "Inleverdatum"],
    [301, 1, "Amsterdam Centraal", "2022-03-01", "2022-03-10"],
    [302, 2, "WTC", "2022-02-20", "2022-03-05"],
    [303, 3, "NDSM", "2022-01-15", "2022-01-25"],
    [303, 4, "WTC", "2022-03-25", "2022-09-23"]
]

#################################
#           Functies            #
#################################
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
    plaats = input("Voer uw plaats in: ")
    categorie = input("Voer uw categorie in: ")
    bankrekeningnummer = input("Voer bankrekeningnummer in: ")
    nieuwe_klant = [int(klantnummer), voornaam, achternaam, straat, postcode, plaats, bankrekeningnummer]

    ###############################
    # Voeg klant toe aan de lijst #
    ###############################
    klanten.append(nieuwe_klant)
    print(f"Nieuwe klant met {klantnummer} succesvol toegevoegd aan lijst!")

    ############################
    # Voeg klant toe aan de db #
    ############################
    
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voeg eerst het adres toe aan de adresstabel        
    adres_query = '''INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
                     VALUES (%s, %s, %s, %s, %s)
                  '''       
    adres_values = (postcode, huisnummer, straat, plaats, categorie)         
    mycursor.execute(adres_query, adres_values)         

    mydb.commit()         
    # Haal het gegenereerde adres-ID op        
    mycursor.execute("SELECT LAST_INSERT_ID()")         
    adres_id = mycursor.fetchone()[0]         
    # Voeg vervolgens de klant toe met het juiste adres-ID        
    klant_query = "INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) VALUES (%s, %s, %s, %s, %s)"       
    klant_values = (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, adres_id)         
    mycursor.execute(klant_query, klant_values)         
    mydb.commit() 

def wijzigen_klant():
    ############################
    # Wijzig klant in de lijst #
    ############################

    klantnummer = int(input("Voer het klantnummer in van de klant die u wilt bijwerken: "))
    
    # Zoeken naar de index van de klant in de lijst
    klant_index = None
    for klant in klanten[1:]:
        if klant[0] == klantnummer:
            klant_index = klanten.index(klant)
            break
    
    if klant_index is not None:
        # Vraag om nieuwe gegevens voor de klant
        nieuwe_voornaam = input("Voer de nieuwe voornaam in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_tussenvoegsel = input("Voer de nieuwe tussenvoegsel in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_achternaam = input("Voer de nieuwe achternaam in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_straat = input("Voer het nieuwe adres in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_huisnummer = input("Voer het nieuwe huisnummer in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_postcode = input("Voer de nieuwe postcode in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_plaats = input("Voer de nieuwe plaats in (druk op Enter om de huidige waarde te behouden): ")
        nieuwe_catagorie = input("Voer de nieuwe catagorie in (druk op Enter om de huidige waarde te behouden): ")
        nieuw_bankrekeningnummer = input("Voer het nieuwe bankrekeningnummer in (druk op Enter om de huidige waarde te behouden): ")

        # Bijwerken van
        
        # Bijwerken van de klantgegevens
        if nieuwe_voornaam.strip():
            klanten[klant_index][1] = nieuwe_voornaam
        if nieuwe_achternaam.strip():
            klanten[klant_index][2] = nieuwe_achternaam
        if nieuwe_straat.strip():
            klanten[klant_index][3] = nieuwe_straat
        if nieuwe_postcode.strip():
            klanten[klant_index][4] = nieuwe_postcode
        if nieuwe_plaats.strip():
            klanten[klant_index][5] = nieuwe_plaats
        if nieuw_bankrekeningnummer.strip():
            klanten[klant_index][6] = nieuw_bankrekeningnummer
        
        print("Klantgegevens succesvol bijgewerkt.")
    else:
        print("Klantnummer niet gevonden.")

    #########################
    # Wijzig klant in de db #
    #########################
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()
    query_klant = f"UPDATE Klant SET voornaam = {nieuwe_voornaam}, tussenvoegsel = {nieuwe_tussenvoegsel}, achternaam  = {nieuwe_achternaam}, bankrekeningnummer = {nieuw_bankrekeningnummer} WHERE klantID = {klantnummer};"
    # Voer de query uit
    mycursor.execute(query_klant)
    mydb.commit()

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()
    query_adres = f"UPDATE Adres SET postcode = '{nieuwe_postcode}', huisnummer = '{nieuwe_huisnummer}', straat = '{nieuwe_straat}', plaats = '{nieuwe_plaats}', catagorie = '{nieuwe_catagorie}' WHERE AdresID = {klantnummer};"
    # Voer de query uit
    mycursor.execute(query_adres)
    mydb.commit()
  
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
    mycursor = mydb.cursor()
    delete_query_klant = f"DELETE FROM Klant WHERE klantID = '{klantnummer}';"
    # Voer de query uit
    mycursor.execute(delete_query_klant)
    mydb.commit()

    mycursor = mydb.cursor()
    delete_query_klant_adres = f"DELETE FROM Adres WHERE adresID = '{klantnummer}';"
    # Voer de query uit
    mycursor.execute(delete_query_klant_adres)
    mydb.commit()

def zoeken_klant2():
    klant_id = None
    wijze_zoeken = input('vult u een klantnummer of achternaam in? ')
    if wijze_zoeken == 'klantnummer':
        zoek_opdracht = int(input('vult u een klantnummer in: '))
        query = "SELECT * FROM klant AS k JOIN Adres AS a ON k.k_adresID = a.adresID WHERE klant.klantID = %s"
        mycursor.execute(query, (zoek_opdracht))
        klant = mycursor.fetchall()
        query = "SELECT klantID FROM Klant WHERE klant.klantID = %s"
        mycursor.execute(query,(zoek_opdracht))
        klant_id = mycursor.fetchone()
        print(klant)
    elif wijze_zoeken == 'achternaam':    
        zoek_opdracht = input('vult u een achternaam in: ')
        query = "SELECT * FROM klant AS k JOIN Adres AS a ON k.k_adresID = a.adresID WHERE klant.achternaam = %s"
        mycursor.execute(query, (zoek_opdracht))
        klant = mycursor.fetchall()
        query = "SELECT klantID FROM Klant WHERE klant.achternaam = %s"
        mycursor.execute(query,(zoek_opdracht))
        klant_id = mycursor.fetchone()
        print(klant)
    
    return klant_id

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
    try:
        # Maak een cursor object om SQL-query's uit te voeren
        mycursor = mydb.cursor()
            
        # Definieer de SQL-query met behulp van een f-string
        query = f"SELECT * FROM klant WHERE achternaam LIKE '%{deel_achternaam}%'"
            
        # Voer de query uit
        mycursor.execute(query)
            
        # Haal alle overeenkomende records op
        klanten_db = mycursor.fetchall()
            
        if klanten_db:
            for klant_db in klanten_db:
                print("Klant ID:", klant_db[0])
                print("Naam:", klant_db[1])
                print("Achternaam:", klant_db[3])
                # Je kunt andere klantgegevens afdrukken zoals nodig
        else:
            print(f"Geen klant gevonden met de naam {deel_achternaam}")
    
    except mysql.connector.Error as error:
        print("Fout bij het verbinden met MySQL:", error)
            
def toevoegen_fiets():
    ###############################
    # Voeg fiets toe aan de lijst #
    ###############################
    fietsnummer = genereer_fietsnummer()
    merk = input("Voer merk in: ")
    model = input("Voer model in: ")
    fietstype = input("Voer de fietstype in: ")
    elektrisch = input("Is de fiets elektrisch? True/False: ")
    dagprijs = input("Voer de dagprijs in: ")
    aankoopdatum = input("Voer de aankoopdatum in yyyy-mm-dd: ")
    vestigingsid = input("Voer de vestigingsid in: ")
    nieuwe_fiets = [int(fietsnummer), merk, model, fietstype, elektrisch, dagprijs, aankoopdatum]
    fietsen.append(nieuwe_fiets)
    toon_alle(fietsen)

    ############################
    # Voeg fiets toe aan de db #
    ############################

    # Definieer de SQL-query's met behulp van f-strings
    # insert_fiets_query = f"INSERT INTO Fietsen (fietsnummer, merk, model, fietstype, elektrisch, dagprijs, aankoopdatum, f_vestigingsID) VALUES ('{fietsnummer}', '{merk}', '{model}', '{fietstype}', '{elektrisch}', '{dagprijs}', '{aankoopdatum}', '{fietsnummer}')"
    insert_fiets_query = f"INSERT INTO Fiets (merk, model, fietstype, elektrisch, dagprijs, aankoopdatum, f_vestegingsID)  VALUES ('{merk}', '{model}', '{fietstype}', '{elektrisch}', '{dagprijs}', '{aankoopdatum}', '{vestigingsid}')"

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    try:
        # Voer de eerste query uit om de klantgegevens in te voegen
        mycursor.execute(insert_fiets_query)

        # Voer de tweede query uit om de adresgegevens in te voegen

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        print(f"Nieuwe fiets met fietsnummer: {fietsnummer} succesvol toegevoegd aan de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het toevoegen van de fiets:", e)
        mydb.rollback()


def selecteer_fietsen(startdatum, inleverdatum):
    fietskeuze = input("Welke fiets wilt u huren? (bijv. 2 heren elektrisch, 2 dames niet-elektrisch): ")
    fietskeuze = fietskeuze.split(", ")
    gekozen_fietsen = []    
    for keuze in fietskeuze:
        if " " not in keuze:
            print("Dit is geen geldige keuze, probeer het opnieuw")
            continue
        aantal, type, elektrisch = keuze.split(" ")
        elektrisch = elektrisch.lower() == "elektrisch"
        # geeft lijst met types en elektrisch of niet elektrisch
        gekozen_fietsen.append((type, aantal, elektrisch))
    return gekozen_fietsen

def voeg_fietsen_toe_aan_contract(vestegingsid, gekozen_fietsen, datum_string, inleverdatum_string):
    beschikbare_fietsen = []
    vestegingsid = input("In welke vesteging wilt u het contract opstellen? Centraal station/ WTC / NDSM-werf: ")
    if gekozen_fietsen[0][2] == True:
        elektrisch = 'Ja'
        print('elektrisch ja')
    else:
        elektrisch = 'Nee'
        print('elektrisch ja')

    # convert tuple to list
    type_fietsen = gekozen_fietsen[0]
    type_fietsen_list = list(type_fietsen)

    print(type_fietsen_list[0])
    print(elektrisch)
    print(datum_string)
    print(inleverdatum_string)
    print(vestegingsid)

    query = f"SELECT * FROM Fiets JOIN Huur ON Fiets.fietsnummer = Huur.Fiets_Fietsnummer WHERE fietstype = '{type_fietsen_list[0]}' AND elektrisch = '{elektrisch}' AND Fiets_Fietsnummer NOT IN (SELECT Fiets_Fietsnummer FROM Huur WHERE '{datum_string}' BETWEEN startdatum AND inleverdatum OR '{inleverdatum_string}' BETWEEN startdatum AND inleverdatum) AND f_vestigingsID = {vestegingsid};"
    
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
def toevoegen_contract(klantnummer, vestigingsnaam):
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voeg eerst het adres toe aan de adresstabel        
    huur_query = f"INSERT INTO Contract (datum, c_klantID) VALUES ('2024-05-17', '2')"       
    mycursor.execute(huur_query)         

    mydb.commit()         

    # Haal het gegenereerde adres-ID op        
    mycursor.execute("SELECT LAST_INSERT_ID()")         
    contract_id = mycursor.fetchone()[0]  

    # Voeg vervolgens de klant toe met het juiste adres-ID        
    klant_query = f"INSERT INTO Huur (Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES ({contract_id}, '5', '2000-01-02', '2000-02-03')"       
    mycursor.execute(klant_query)         
    mydb.commit()

    
def toevoegen_contract2(klantnummer, vestigingsnaam):
    ##################################
    # Voeg contract toe aan de lijst #
    ##################################

    print("Contract Opstellen")
    contractnummer = genereer_contractnummer()
    klantnummer = klantnummer
    vestigingsnaam = vestigingsnaam
    startdatum = input("Voer de startdatum in.. ")
    inleverdatum = input("Voer de inleverdatum in.. ")
    nieuw_contract = [int(contractnummer), klantnummer, vestigingsnaam, startdatum, inleverdatum]

    print("nieuwe contract succesvol toegevoegd!")
    contracten.append(nieuw_contract)
    toon_alle(contracten)

    ###############################
    # Voeg contract toe aan de db #
    ###############################

    # Definieer de SQL-query's met behulp van f-strings
    insert_contract_query = f"INSERT INTO Contracten (idKlanten, Vestiginsnaam, Startdatum, Inleverdatum) VALUES ('{klantnummer}', '{vestigingsnaam}', '{startdatum}', '{inleverdatum}')"

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    try:
        # Voer de eerste query uit om de klantgegevens in te voegen
        mycursor.execute(insert_contract_query)

        # Voer de tweede query uit om de adresgegevens in te voegen

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        print(f"Nieuwe contract met contractummer: {contractnummer} succesvol toegevoegd aan de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het toevoegen van de contract:", e)
        mydb.rollback()

    # Als je wilt controleren of de klant correct is toegevoegd, kun je bijvoorbeeld de ID van de laatst toegevoegde rij afdrukken
    print("Contract toegevoegd aan de database met ID van de laatst toegevoegde contract:", mycursor.lastrowid)

def toon_contract(contractnummer):
    ##################################
    # Voeg contract toe aan de lijst #
    ##################################

    width_langste_woord = 10  # De breedte van de breedste term, rekening houdend met "Vestiging:"
    contractnummer = contractnummer

    # Search for the sublist with contract number 303
    contract_info = None
    for contract in contracten[1:]:
        if contract[0] == contractnummer:
            contract_info = contract
            break

    if contract_info:
        # Haal klantnummer en locatienaam op uit de contractinformatie
        klantnummer = contract_info[1]
        locatie_naam = contract_info[2]

    # Zoek klantinformatie
    klant_informatie = None
    for klant in klanten[1:]:
        if klant[0] == klantnummer:
            klant_informatie = klant
            break

    # Zoek locatieinformatie
    locatie_informatie = None
    for locatie in locaties[1:]:
        print(locatie)
        if locatie[1] == locatie_naam:
            locatie_informatie = locatie
            break
    
    if klant_informatie and len(klant_informatie) >= 3:  # Controleer of klant_informatie bestaat en voldoende elementen heeft
        klant_naam = klant_informatie[2]
    else:
        klant_naam = "Onbekend"  # Als de informatie ontbreekt, gebruik een standaardwaarde

  
    #############################
    #           LOGO            #
    #############################
    print("                  ____  ")
    print("                 /  __\\")
    print("                (  @ @ )")
    print("                 \\  O /")
    print("                  \\__/ ")
    print("                        ")

    #################################
    #           CONTRACT            #
    #################################
    
    # Get date today
    date_today =  datetime.today()
    date_today_str = date_today.strftime('%d-%m-%Y')

    print(f"Contractnr: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Datum: {str(date_today_str):<{width_langste_woord}}", end="\n")
    
    #################################
    #           VESTIGING           #
    #################################
    print(f"{'':<{width_langste_woord}}")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Vestiging: {locatie_informatie[1]:<{width_langste_woord}}", end="\t")
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"

    # Lengte van de kolommen
    kolom_breedte = 11

    # Adresgegevens
    print(f"{'':<{kolom_breedte}}{locatie_informatie[2]}")
    print(f"{'':<{kolom_breedte}}{locatie_informatie[3]}")

    #############################
    #           KLANT           #
    #############################
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Klant: {str(klant_informatie[1]):<{3}}, {str(klant_informatie[2])} (klantnr {klant_informatie[0]})")
    # Adresgegevens

    # Lengte van de kolommen
    kolom_breedte = 7

    # Header
    print(f"{'Adres:':<{kolom_breedte}}{klant_informatie[3]}")
    print(f"{'':<{kolom_breedte}}{klant_informatie[4]} {klant_informatie[5]}")

    #############################
    #           DATUM           #
    #############################

    # Converteer de gebruikersinvoer naar datetime objecten
    startdatum = datetime.strptime(contract_info[3], "%Y-%m-%d")
    inleverdatum = datetime.strptime(contract_info[4], "%Y-%m-%d")

    # Verschil berekenen
    verschil = inleverdatum - startdatum
 
    '''
    verschil.days is een attribuut van het verschil tussen twee datetime-objecten. 
    In dit geval wordt verschil berekend door inleverdatum - startdatum. Dit geeft een timedelta-object terug.
    Wat het verschil aangeeft tussen de twee datums in dagen. verschil.minutes doet dit voor minuten enz.
    '''
    aantal_dagen = verschil.days
 

    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Stardatum: {str(contract_info[3]):<{width_langste_woord}}")
    print(f"Inleverdatum: {str(contract_info[4]):<{width_langste_woord}} --> aantal dagen: {aantal_dagen}", end="\n")
    print("")

    print(f'-----------------------------------------------------------------------------------', end="\n")

    #############################
    #           FIETSEN         #
    #############################  
    print("")
    print("FIETSEN:")
    print("")

    # Gegevens
    gehuurde_fietsen = 3
    prijs_per_dag = 25

    # Header
    print(f"{'Fietsnr':<15} {'Type':<15} {'Model':<15} {'Elektrisch':<15} {'Prijs Per Dag':<15}")

    # Gegevens voor elke dag
    for dag in range(1, 4):
        totaalbedrag = dag * prijs_per_dag
        print(f"{dag:<15} {prijs_per_dag:<15} {totaalbedrag:<15} {totaalbedrag:^15} {totaalbedrag:>15}")
    
    print("")
    print(f'-----------------------------------------------------------------------------------', end="\n")
    
    #############################
    #           Totaal          #
    #############################
    print("")
    print("TOTAAL:")
    print("")

   # Gegevens
    prijs_per_dag = 25

    # Header
    print(f"{'Aantal dagen':>15} {'Prijs per dag':>15} {'Totaalbedrag':>15}")

    # Gegevens voor elke dag
    for dag in range(1, 2):
        totaalbedrag = dag * prijs_per_dag
        print(f"{aantal_dagen:>15} {prijs_per_dag:>15} {totaalbedrag:>15}")

def toon_alle_gegevens():
    ########################################
    # Voeg klant gegevens toe aan de lijst #
    ########################################
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
            "plaats": klant[5],
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

    #####################################
    # Voeg klant gegevens toe aan de db #
    #####################################

    # Define the SQL query to select all data from the "sporthal" table in the "Basketbal" database
    fetch_query = 'SELECT * FROM Klant'

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Execute the SQL query
    mycursor.execute(fetch_query)

    # Fetch all the results from the executed query
    result = mycursor.fetchall()

    # Iterate over the results and print each row
    for db_klanten in result:
        print(db_klanten)

#################################
#           Utility             #
#################################
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

#############################
#           Program         #
#############################
def main():
    while True:
        toon_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            if mydb.is_connected():
                mydb.close()
            print("Programma beëindigen. Tot de volgende keer!")
            break
        elif choice == "1":
            toevoegen_klant()
        elif choice == "2":
            wijzigen_klant()
        elif choice == "3":
            klantnummer = int(input("Voer het klantnummer in dat moet worden verwijderd: "))
            verwijderen_klant(klantnummer)
        elif choice == "4":
            zoeken_klant()
        elif choice == "5":
            toevoegen_fiets()
            
        elif choice == "6":
            
            # toevoegen_contract(klantnummer, vestigingsnaam)
            # datum_string = input("Voer ingangsdatum in..")
            # inleverdatum_string = input ("voer inleverdatum in..")
            # test = selecteer_fietsen(datum_string, inleverdatum_string)
            nummer = input("Voer uw klantnummer in.. ")
            vestigingsid = input("Voer het vestigingsid in.. ")


            # voeg_fietsen_toe_aan_contract(vestigingsid, test, datum_string, inleverdatum_string)

            toevoegen_contract(nummer, vestigingsid)
        elif choice == "7":
            contractnummer = int(input("Voer het contractnummer in dat moet worden getoond: "))
            toon_contract(contractnummer)
        elif choice == "8":
            toon_alle_gegevens()
            toon_alle(klanten)

        else:
            print("Ongeldige keuze. Probeer een nummer optie tussen 0 en 9.")
            continue  # Continue to the next iteration of the loop if the choice is invalid

if __name__ == "__main__":
    main()