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