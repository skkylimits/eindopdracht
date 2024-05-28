import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os

#####################################
#           DB Connection           #
#####################################
# Laad het .env-bestand
load_dotenv()  

# Haal het wachtwoord op uit een omgevingsvariabele
db_pass = os.getenv("DB_PASS")

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=db_pass,
    database="mydb"
)
mycursor = mydb.cursor()

# Controleer of de verbinding succesvol tot stand is gebracht
if mydb.is_connected():
    print("Database connected successfully")
else:
    print("Failed to connect to database")


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

    # Sluit de cursor en de verbinding
    mycursor.close()

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

    ###########################
    # Wijzig klantgegevens db #
    ###########################

    # Stap 0: Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Stap 1: Haal het adres ID op dat bij de klant hoort
    fetch_query = "SELECT k_adresID FROM Klant WHERE klantID = %s"
    mycursor.execute(fetch_query, (klantnummer ,))
    result = mycursor.fetchone()
    adres_id = result[0]

    # Step 2: Update de klant
    update_klant_query = """
    UPDATE Klant 
    SET voornaam = CASE WHEN %s != '' THEN %s ELSE voornaam END, 
        tussenvoegsel = CASE WHEN %s != '' THEN %s ELSE tussenvoegsel END, 
        achternaam = CASE WHEN %s != '' THEN %s ELSE achternaam END,
        bankrekeningnummer = CASE WHEN %s != '' THEN %s ELSE bankrekeningnummer END 
    WHERE klantID = %s
    """

    klant_data = (nieuwe_voornaam, nieuwe_voornaam, nieuwe_tussenvoegsel, nieuwe_tussenvoegsel, nieuwe_achternaam, nieuwe_achternaam, nieuw_bankrekeningnummer, nieuw_bankrekeningnummer, klantnummer)
    mycursor.execute(update_klant_query, klant_data)
        
    # Step 3: Update het Adres
    update_address_query = """
    UPDATE Adres 
    SET postcode = CASE WHEN %s != '' THEN %s ELSE postcode END, 
        huisnummer = CASE WHEN %s != '' THEN %s ELSE huisnummer END, 
        straat = CASE WHEN %s != '' THEN %s ELSE straat END,
        plaats = CASE WHEN %s != '' THEN %s ELSE plaats END,
        catagorie = CASE WHEN %s != '' THEN %s ELSE catagorie END 
    WHERE AdresID = %s
    """

    address_data = (nieuwe_postcode, nieuwe_postcode, nieuwe_huisnummer, nieuwe_huisnummer, nieuwe_straat, nieuwe_straat, nieuwe_plaats, nieuwe_plaats, nieuwe_catagorie, nieuwe_catagorie, adres_id)
    mycursor.execute(update_address_query, address_data)
        
    # Stap 4: Commit de transactie
    mydb.commit()

    # Stap 5: Sluit de cursor en de verbinding
    mycursor.close()

    # Meld dat een nieuwe klant succesvol is toegevoegd.
    print(f"\nKlantgegevens succesvol bijgewerkt!")


def verwijderen_klant(klantnummer):
    #############################
    # Verwijder klant uit de db #
    #############################
    
    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Stap 1: Haal het adres-ID op dat hoort bij de klant
    mycursor.execute("SELECT k_adresID FROM Klant WHERE klantID = %s", (klantnummer,))
    adres_id = mycursor.fetchone()

    if adres_id:
        adres_id = adres_id[0]
        print(f"Adres-ID voor klant {klantnummer}: {adres_id}")

        # Stap 2: Verwijder alle huurrecords gerelateerd aan de contracten van de klant
        delete_query_huur = """
            DELETE FROM Huur 
            WHERE Contracten_ContractNummer IN (
                SELECT contractNummer FROM contract WHERE c_klantID = %s
            )
        """
        mycursor.execute(delete_query_huur, (klantnummer,))
        mydb.commit()

        # Stap 3: Verwijder alle contracten van de klant
        delete_query_contract = "DELETE FROM contract WHERE c_klantID = %s"
        mycursor.execute(delete_query_contract, (klantnummer,))
        mydb.commit()

        # Stap 4: Verwijder de klant
        delete_query_klant = "DELETE FROM Klant WHERE klantID = %s"
        mycursor.execute(delete_query_klant, (klantnummer,))
        mydb.commit()

        # Stap 5: Verwijder het adres
        delete_query_adres = "DELETE FROM Adres WHERE adresID = %s"
        mycursor.execute(delete_query_adres, (adres_id,))

        # Bevestig de transactie na alle verwijderingen
        mydb.commit()

        # Sluit de cursor en de verbinding
        mycursor.close()

        print(f"Klant {klantnummer} en adres {adres_id} verwijderd")

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
                print("\n")
        else:
            # Als er geen klanten gevonden zijn, druk dan een passend bericht af
            print(f"Geen klant gevonden met de naam {deel_achternaam}")
    
    except mysql.connector.Error as error:
        # Druk een foutmelding af als er een fout optreedt bij het verbinden met MySQL
        print("Fout bij het verbinden met MySQL:", error)
    
    # Sluit de cursor en de verbinding
    mycursor.close()
            
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

        # Bevestig de transactie om de wijzigingen in de database permanent te maken
        mydb.commit()

        # Meld dat een nieuwe klant succesvol is verwijderd
        print(f"\n Nieuwe fiets succesvol toegevoegd aan de database!")
    except Exception as e:
        # Als er een fout optreedt, maak dan geen wijzigingen in de database en toon een foutmelding
        print("Er is een fout opgetreden bij het toevoegen van de fiets:", e)
        mydb.rollback()

    # Sluit de cursor en de verbinding
    mycursor.close()

def toevoegen_contract(klantnummer, vestigingsid):
    # Vraag gebruiker input
    fietsnummer = input('Voer fietsnummer in? ')
    startdatum = input('Wat is de gewenste ingangsdatum? [yyyy-mm-dd] ')
    inleverdatum = input('Wat is de gewenste inleverdatum? [yyyy-mm-dd] ')

    # Get date today
    date_today = datetime.today()
    date_today_str = date_today.strftime('%Y-%m-%d')

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voeg eerst de huur data toe aan de huurtabel        
    huur_query = f"INSERT INTO Contract (datum, c_klantID) VALUES ('{date_today_str}', {klantnummer})"  

    # Voer de query uit
    mycursor.execute(huur_query)         
    mydb.commit()         

    # Haal het gegenereerde huur-ID op        
    mycursor.execute("SELECT LAST_INSERT_ID()")         
    contract_id = mycursor.fetchone()[0]  

    # Voeg vervolgens het contract toe met het juiste huur-ID        
    klant_query = f"INSERT INTO Huur (Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES ({contract_id}, {fietsnummer}, '{startdatum}', '{inleverdatum}')"
    
    # Voer query uit
    mycursor.execute(klant_query)         
    mydb.commit()

    # Sluit de cursor en de verbinding
    mycursor.close()

    #  Meld dat een nieuwe klant succesvol is verwijderd
    print(f"\nNieuw contract succesvol toegevoegd aan de database!")
    
def toon_contract(klantnummer):
    width_langste_woord = 10  # De breedte van de breedste term, rekening houdend met "Vestiging:"
    klantnummer = klantnummer

    #############################################
    # Stel contract op met informatie uit de DB #
    #############################################

    ####################
    # Fetch contracten #
    ####################

    # Definieer de SQL-query om alle gegevens uit de klantentabel in de mydb-database te selecteren.
    fetch_query = f"""
        SELECT 
            Contract.contractNummer,
            Contract.datum,
            Klant.voornaam, 
            Klant.tussenvoegsel,
            Klant.achternaam,
            Adres.straat,
            Adres.huisnummer,
            Adres.postcode,
            Adres.plaats,
            Fiets.fietsnummer,
            Fiets.merk,
            Fiets.model,
            Fiets.fietstype,
            Fiets.elektrisch,
            Huur.startdatum, 
            Huur.inleverdatum,
            (DATEDIFF(Huur.inleverdatum, Huur.startdatum)) AS aantal_verhuurde_dagen,
            Fiets.dagprijs,
            (DATEDIFF(Huur.inleverdatum, Huur.startdatum) * Fiets.dagprijs) AS totale_huurprijs,
            (SELECT COUNT(*) FROM Contract) AS aantal_fietsen
        FROM 
            Contract
        LEFT JOIN 
            klant ON Contract.c_klantID = klant.klantID
        LEFT JOIN 
            Adres ON Adres.AdresID = Klant.k_adresID
        LEFT JOIN 
            Huur ON Contract.contractNummer = Huur.Contracten_ContractNummer
        LEFT JOIN 
            Fiets ON Huur.Fiets_Fietsnummer = Fiets.fietsnummer
        WHERE 
            Klant.klantID = '{klantnummer}'
    """

    # Maak een cursor object aan om SQL-query's uit te voeren.
    mycursor = mydb.cursor()

    # Voer de SQL-query uit.
    mycursor.execute(fetch_query)

    # Haal alle resultaten op van de uitgevoerde query.
    result = mycursor.fetchall()

    contractnummer = result[0][0]
    voornaam = result[0][2]
    tussenvoegsel = result[0][3]
    achternaam = result[0][4]

    straat = result[0][5]
    huisnummer = result[0][6]
    postcode = result[0][7]
    plaats = result[0][8]

    startdatum = result[0][14]
    inleverdatum = result[0][15]

    aantal_verhuurde_dagen = result[0][16]

    ###################
    # Fetch vestiging #
    ###################
    
    # Definieer de SQL-query om alle gegevens uit de vestigingstabel in de mydb-database te selecteren
    fetch_vestiging_query = """
        SELECT 
            vestiging.vestegingsID,
            vestiging.vestegingsnaam,
            Adres.straat,
            Adres.huisnummer,
            Adres.postcode,
            Adres.plaats
        FROM 
            Vestiging
        LEFT JOIN 
            Adres ON Adres.AdresID = vestiging.v_adresID
        WHERE 
            vestiging.v_adresID = '3'
    """

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voer de SQL-query uit
    mycursor.execute(fetch_vestiging_query)

    # Haal alle resultaten op uit de uitgevoerde query
    vestiging = mycursor.fetchall()

    vestigings_naam = vestiging[0][1]
    vestigings_adres = vestiging[0][2]
    vestigings_huisnummer = vestiging[0][3]
    vestigings_postcode = vestiging[0][4]
    vestigings_plaats = vestiging[0][5]

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
    #           VESTIGING           #
    #################################
    print(f"{'':<{width_langste_woord}}")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Vestiging: {vestigings_naam:<{width_langste_woord}}", end="\t")
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"

    # Lengte van de kolommen
    kolom_breedte = 11

    # Adresgegevens
    print(f"{'':<{kolom_breedte}}{vestigings_adres} {vestigings_huisnummer}")
    print(f"{'':<{kolom_breedte}}{vestigings_postcode} {vestigings_plaats}")

    #################################
    #           CONTRACT            #
    #################################
    
    # Krijg datum vandaag
    date_today =  datetime.today()
    date_today_str = date_today.strftime('%d-%m-%Y')

    print(f"Contractnr: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Datum: {str(date_today_str):<{width_langste_woord}}", end="\n")
    

    #############################
    #           KLANT           #
    #############################
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Klant: {str(voornaam):<{2}}, {str(tussenvoegsel)} {str(achternaam)} (klantnr {klantnummer})")

    # Lengte van de kolommen
    kolom_breedte = 7

    # Header
    print(f"{'Adres:':<{kolom_breedte}}{straat} {huisnummer}")
    print(f"{'':<{kolom_breedte}}{postcode} {plaats}")

    #############################
    #           DATUM           #
    #############################

    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Stardatum: {str(startdatum):<{width_langste_woord}}")
    print(f"Inleverdatum: {str(inleverdatum):<{width_langste_woord}} --> aantal dagen: {aantal_verhuurde_dagen}", end="\n")
    print("")

    print(f'-----------------------------------------------------------------------------------', end="\n")

    #############################
    #           FIETSEN         #
    #############################  
    print("")
    print("FIETSEN:")
    print("") 

    # Header
    print(f"{'Fietsnr':<15} {'Type':<15} {'Model':<15} {'Elektrisch':<15} {'Prijs Per Dag':<15}")

    for fiets in result:
        print(f"{fiets[9]:<15} {fiets[11]:<15} {fiets[12]:<15} {fiets[13]:^15} {fiets[17]:>15}")

    print("")
    print(f'-----------------------------------------------------------------------------------', end="\n")
    
    #############################
    #           Totaal          #
    #############################
    print("")
    print("TOTAAL:")
    print("")

    # Maak een lege lijst om de waarden van fiets[17] op te slaan
    dagprijs_per_fiets = []

    # Itereer over de resultaten en voeg de waarden van fiets[17] toe aan de lijst
    for fiets in result:
        dagprijs_per_fiets.append(fiets[17])

    # Header
    print(f"{'Aantal dagen':>15} {'Prijs per dag':>15} {'Totaalbedrag':>15}")

    # Gegevens voor elke dag
    for _ in range(1, 2):
        prijs_per_dag = sum(dagprijs_per_fiets)
        totaalbedrag = aantal_verhuurde_dagen * prijs_per_dag
        print(f"{aantal_verhuurde_dagen:>15} {prijs_per_dag:>15} {totaalbedrag:>15}")
    
    # Sluit de cursor en de verbinding
    mycursor.close()

def toon_alle_gegevens():
    #####################################
    # Voeg klant gegevens toe aan de db #
    #####################################

    ###############
    # Vestigingen #
    ###############
    print('\n')
    print("+--------------------------------+")
    print("|                                |")
    print("|            Vestigingen         |")
    print("|                                |")
    print("+--------------------------------+")
    

    # Definieer de SQL-query om alle gegevens uit de "klant" tabel in de "Basketbal" database te selecteren
    fetch_query = 'SELECT * FROM Vestiging'

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voer de SQL-query uit
    mycursor.execute(fetch_query)

    # Haal alle resultaten op uit de uitgevoerde query
    result = mycursor.fetchall()

    # Itereer over de resultaten en print elke rij
    for db_klanten in result:
        print(db_klanten)
    
    print('\n')
    
    ###########
    # Fietsen #
    ###########

    print("+------------------------------+")
    print("|                              |")
    print("|            Fietsen           |")
    print("|                              |")
    print("+------------------------------+")
    
    # Definieer de SQL-query om alle gegevens uit de "klant" tabel in de "Basketbal" database te selecteren
    fetch_query = 'SELECT * FROM Fiets ORDER BY Aankoopdatum'

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voer de SQL-query uit
    mycursor.execute(fetch_query)

    # Haal alle resultaten op uit de uitgevoerde query
    result = mycursor.fetchall()

    # Itereer over de resultaten en print elke rij
    for db_klanten in result:
        print(db_klanten)
    
    print('\n')   

    #########
    # Klant #
    #########

    print("+------------------------------+")
    print("|                              |")
    print("|            Klanten           |")
    print("|                              |")
    print("+------------------------------+")

    # Definieer de SQL-query om alle gegevens uit de "klant" tabel in de "Basketbal" database te selecteren
    fetch_query = 'SELECT * FROM Klant ORDER BY achternaam;'

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voer de SQL-query uit
    mycursor.execute(fetch_query)

    # Haal alle resultaten op uit de uitgevoerde query
    result = mycursor.fetchall()

    # Itereer over de resultaten en print elke rij
    for db_klanten in result:
        print(db_klanten)
        
    print('\n')

    ############
    # Contract #
    ############

    print("+---------------------------------+")
    print("|                                 |")
    print("|            CONTRACTEN           |")
    print("|                                 |")
    print("+---------------------------------+")

    # Definieer de SQL-query om alle gegevens uit de "klant" tabel in de "Basketbal" database te selecteren
    fetch_query = """
        SELECT 
            Contract.contractNummer,
            Contract.datum,
            Huur.startdatum, 
            Huur.inleverdatum,
            (DATEDIFF(Huur.inleverdatum, Huur.startdatum) * Fiets.dagprijs) AS totale_huurprijs
        FROM 
            Contract
        LEFT JOIN 
            Klant ON Contract.c_klantID = Klant.klantID
        LEFT JOIN 
            Huur ON Contract.contractNummer = Huur.Contracten_ContractNummer
        LEFT JOIN 
            Fiets ON Huur.Fiets_Fietsnummer = Fiets.fietsnummer
        ORDER BY
            Huur.startdatum
        """

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

    # Voer de SQL-query uit
    mycursor.execute(fetch_query)

    # Haal alle resultaten op uit de uitgevoerde query
    result = mycursor.fetchall()

    # Itereer over de resultaten en print elke rij
    for db_klanten in result:
        print(db_klanten)
        
    print('\n')

    # Sluit de cursor en de verbinding
    mycursor.close()
   

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
            klantnummer = input("Voer uw klantnummer in.. ")
            vestigingsid = input("Voer het vestigingsid in.. ")
            toevoegen_contract(klantnummer, vestigingsid)
        elif choice == "7":
            klantnummer = int(input("Voer het klantnummer in dat moet worden getoond: "))
            toon_contract(klantnummer)
        elif choice == "8":
            toon_alle_gegevens()

        else:
            print("Ongeldige keuze. Probeer een nummer optie tussen 0 en 9.")
            continue  # Continue to the next iteration of the loop if the choice is invalid

if __name__ == "__main__":
    main()