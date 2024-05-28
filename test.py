def toevoegen_contract(klantnummer, vestigingsid):
    # Vraag gebruiker input
    fietsnummer = input('Voer fietsnummer in? ')
    startdatum = input('Wat is de gewenste ingangsdatum? [yy-mm-dd]')
    inleverdatum = input('Wat is de gewenste inleverdatum? [yy-mm-dd]')

    # Get date today
    date_today =  datetime.today()
    date_today_str = date_today.strftime('%d-%m-%Y')

    # Maak een cursor object om SQL-query's uit te voeren
    mycursor = mydb.cursor()

   # Voeg eerst de huurdata toe aan de huurtabel        
    huur_query = f"""
        INSERT INTO Contract (datum, c_klantID) 
        VALUES ({date_today_str}, {klantnummer})
    """

    # Voer de query uit
    mycursor.execute(huur_query)         
    mydb.commit()         

    # Haal het gegenereerde huur-ID op        
    mycursor.execute("SELECT LAST_INSERT_ID()")         
    contract_id = mycursor.fetchone()[0]  

    # Voeg vervolgens het contract toe met het juiste huur-ID        
    klant_query = f"""
        INSERT INTO Huur (Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) 
        VALUES ({contract_id}, {fietsnummer}, {startdatum}, {inleverdatum})
    """

    # Voer de query uit
    mycursor.execute(klant_query)         
    mydb.commit()




   

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
    

    #############################
    #           KLANT           #
    #############################
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Klant: {str(voornaam):<{2}}, {str(tussenvoegsel)} {str(achternaam)} (klantnr {klantnummer})")
    # Adresgegevens

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
        print(f"{fiets[0]:<15} {fiets[0]:<15} {fiets[0]:<15} {fiets[0]:^15} {fiets[0]:>15}")

    print("")
    print(f'-----------------------------------------------------------------------------------', end="\n")
    
    #############################
    #           Totaal          #
    #############################
    print("")
    print("TOTAAL:")
    print("")

    # Header
    print(f"{'Aantal dagen':>15} {'Prijs per dag':>15} {'Totaalbedrag':>15}")

    # Gegevens voor elke dag
    for _ in range(1, 2):
        prijs_per_dag = aantal_fietsen * dagprijs
        totaalbedrag = aantal_fietsen * (aantal_verhuurde_dagen * dagprijs)
        print(f"{aantal_verhuurde_dagen:>15} {prijs_per_dag:>15} {totaalbedrag:>15}")



  
