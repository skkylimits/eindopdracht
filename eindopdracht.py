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
    voornaam = input("Voer voornaam in: ")
    tussenvoegsel = input("Voer tussenvoegsel in: ")
    achternaam = input("Voer uw achternaam in: ")
    straat = input("Voer uw adres in: ")
    huisnummer = input("Voer uw huisnummer in: ")
    postcode = input("Voer uw postcode in: ")
    plaats = input("Voer uw plaats in: ")
    categorie = input("Voer uw categorie in: ")
    bankrekeningnummer = input("Voer bankrekeningnummer in: ")

    ############################
    # Voeg klant toe aan de db #
    ############################
    
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voeg eerst het adres toe aan de adrestabel        
    adres_query = '''
        INSERT INTO Adres (
            postcode, 
            huisnummer, 
            straat, 
            plaats, 
            catagorie
        ) VALUES (%s, %s, %s, %s, %s)
    '''

    # Paramatiseer values om SQL injecties te voorkomen 
    adres_values = (postcode, huisnummer, straat, plaats, categorie)

    # Voer de adresquery uit met de adreswaarden en bevestig de wijzigingen in de database.
    mycursor.execute(adres_query, adres_values)         
    mydb.commit()       

    # Haal het gegenereerde adres-ID op        
    mycursor.execute("SELECT LAST_INSERT_ID()")         
    adres_id = mycursor.fetchone()[0] 

    # Definieer de geparameteriseerde query
    klant_query = '''
        INSERT INTO Klant (
            voornaam, 
            tussenvoegsel, 
            achternaam, 
            bankrekeningnummer, 
            k_adresID
        ) VALUES (%s, %s, %s, %s, %s)
    '''

    # Defineer de waarden
    klant_values = (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, adres_id)

    # Voer de adresquery uit met de adreswaarden en bevestig de wijzigingen in de database.
    mycursor.execute(klant_query, klant_values)
    mydb.commit()

    # Meld dat een nieuwe klant succesvol is toegevoegd.
    print(f"\nNieuwe klant succesvol toegevoegd aan de database!")

def wijzigen_klant():
    klantnummer = int(input("Voer het klantnummer in van de klant die u wilt bijwerken: "))
    nieuwe_voornaam = input("Voer de nieuwe voornaam in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_tussenvoegsel = input("Voer de nieuwe tussenvoegsel in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_achternaam = input("Voer de nieuwe achternaam in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_straat = input("Voer het nieuwe adres in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_huisnummer = input("Voer het nieuwe huisnummer in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_postcode = input("Voer de nieuwe postcode in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_plaats = input("Voer de nieuwe plaats in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_catagorie = input("Voer de nieuwe catagorie in (druk op Enter om de huidige waarde te behouden): ")
    nieuw_bankrekeningnummer = input("Voer het nieuwe bankrekeningnummer in (druk op Enter om de huidige waarde te behouden): ")

    #############################
    # Wijzig klant toe in de db #
    #############################

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Update de klantgegevens met de nieuwe waarden, waarbij het klantnummer overeenkomt.
    query_klant = """
        UPDATE Klant 
        SET voornaam = %s, 
            tussenvoegsel = %s, 
            achternaam = %s, 
            bankrekeningnummer = %s 
        WHERE klantID = %s
    """

    # Definieer de waarden voor de klantupdate-query
    klant_values = (nieuwe_voornaam, nieuwe_tussenvoegsel, nieuwe_achternaam, nieuw_bankrekeningnummer, klantnummer)

    # Voer de query uit
    mycursor.execute(query_klant, klant_values)
    mydb.commit()
    
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Update de adresgegevens met de nieuwe waarden, waarbij het adresnummer overeenkomt.
    query_adres = """
        UPDATE Adres 
        SET postcode = %s, 
            huisnummer = %s, 
            straat = %s, 
            plaats = %s, 
            catagorie = %s 
        WHERE AdresID = %s
    """

    # Definieer de waarden voor de adres update-query
    adres_values = (nieuwe_postcode, nieuwe_huisnummer, nieuwe_straat, nieuwe_plaats, nieuwe_catagorie, klantnummer)

    # Voer de query uit 
    mycursor.execute(query_adres, adres_values)
    mydb.commit()

    # Meld dat een nieuwe klant succesvol is toegevoegd.
    print(f"\nKlantgegevens succesvol bijgewerkt!")
  
def verwijderen_klant(klantnummer):
    #############################
    # Verwijder klant uit de db #
    #############################

    ## Definieer de delete-query voor het verwijderen van de klant met het opgegeven klantnummer
    mycursor = mydb.cursor()
    delete_query_klant = f"DELETE FROM Klant WHERE klantID = '{klantnummer}';"
    
    # Voer de query uit
    mycursor.execute(delete_query_klant)
    mydb.commit()

    # Definieer de delete-query voor het verwijderen van het adres van de klant met het opgegeven klantnummer
    mycursor = mydb.cursor()
    delete_query_klant_adres = f"DELETE FROM Adres WHERE adresID = '{klantnummer}';"
    
    # Voer de query uit
    mycursor.execute(delete_query_klant_adres)
    mydb.commit()

    # Meld dat een nieuwe klant succesvol is verwijderd.
    print(f"\nKlant succesvol verwijderd!")

def zoeken_klant():
    #############################
    # Zoek klant in de database #
    #############################

    # Vraag de gebruiker om een deel van de achternaam om te zoeken
    deel_achternaam = input("Voer een deel van de achternaam in om te zoeken: ")

    try:
        # Maak een cursor object om SQL-query's uit te voeren
        mycursor = mydb.cursor()
            
        # Definieer de SQL-query met behulp van een f-string
        query = f"SELECT * FROM klant WHERE achternaam LIKE '%{deel_achternaam}%'"
            
        # Voer de query uit
        mycursor.execute(query)
            
        # Haal alle overeenkomende records op
        klanten_db = mycursor.fetchall()

        # Controleer of klanten_db niet leeg is
        if klanten_db:
            # Itereer over elk element (klant) in klanten_db
            for klant_db in klanten_db:
                # Druk het klant ID af
                print("Klant ID:", klant_db[0])
                # Druk de gevonden naam af
                print("Voornaam:", klant_db[1])
                print("Tussenvoegsel:", klant_db[2])
                print("Achternaam:", klant_db[3])
        else:
            # Als er geen klanten gevonden zijn, druk dan een passend bericht af
            print(f"Geen klant gevonden met de naam {deel_achternaam}")
    
    except mysql.connector.Error as error:
        # Druk een foutmelding af als er een fout optreedt bij het verbinden met MySQL
        print("Fout bij het verbinden met MySQL:", error)
            
def toevoegen_fiets():
    merk = input("Voer merk in: ")
    model = input("Voer model in: ")
    fietstype = input("Voer de fietstype in: ")
    elektrisch = input("Is de fiets elektrisch? [True | False]: ")
    dagprijs = input("Voer de dagprijs in hele nummers [12.0]: ")
    aankoopdatum = input("Voer de aankoopdatum in [yyyy-mm-dd]: ")
    vestigingsid = input("Voer de vestigingsid in: ")

    ############################
    # Voeg fiets toe aan de db #
    ############################

    # Definieer de SQL-query's met behulp van f-strings
    insert_fiets_query = f"INSERT INTO Fiets (merk, model, fietstype, elektrisch, dagprijs, aankoopdatum, f_vestegingsID)  VALUES ('{merk}', '{model}', '{fietstype}', '{elektrisch}', '{dagprijs}', '{aankoopdatum}', '{vestigingsid}')"

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    try:
        # Voer de eerste query uit om de klantgegevens in te voegen
        mycursor.execute(insert_fiets_query)

        # Voer de tweede query uit om de adresgegevens in te voegen

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        print(f"Nieuwe fiets succesvol toegevoegd aan de database!")
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
    print("Contract Opstellen")
    klantnummer = klantnummer
    vestigingsnaam = vestigingsnaam
    startdatum = input("Voer de startdatum in.. ")
    inleverdatum = input("Voer de inleverdatum in.. ")

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

        print(f"Nieuwe contract succesvol toegevoegd aan de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het toevoegen van de contract:", e)
        mydb.rollback()

    # Als je wilt controleren of de klant correct is toegevoegd, kun je bijvoorbeeld de ID van de laatst toegevoegde rij afdrukken
    print("Contract toegevoegd aan de database met ID van de laatst toegevoegde contract:", mycursor.lastrowid)

def toon_contract(contractnummer):
    width_langste_woord = 10  # De breedte van de breedste term, rekening houdend met "Vestiging:"
    contractnummer = contractnummer
  
    #############################################
    # Stel contract op met informatie uit de DB #
    #############################################

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
            nummer = input("Voer uw klantnummer in.. ")
            vestigingsid = input("Voer het vestigingsid in.. ")
            toevoegen_contract(nummer, vestigingsid)
        elif choice == "7":
            contractnummer = int(input("Voer het contractnummer in dat moet worden getoond: "))
            toon_contract(contractnummer)
        elif choice == "8":
            toon_alle_gegevens()

        else:
            print("Ongeldige keuze. Probeer een nummer optie tussen 0 en 9.")
            continue  # Continue to the next iteration of the loop if the choice is invalid

if __name__ == "__main__":
    main()