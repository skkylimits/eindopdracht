
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

    # Vraag de nieuwe adresinformatie aan de gebruiker
    nieuwe_straat = input("Voer het nieuwe adres in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_huisnummer = input("Voer het nieuwe huisnummer in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_postcode = input("Voer de nieuwe postcode in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_plaats = input("Voer de nieuwe plaats in (druk op Enter om de huidige waarde te behouden): ")
    nieuwe_catagorie = input("Voer de nieuwe catagorie in (druk op Enter om de huidige waarde te behouden): ")

    # Controleer of de nieuwe invoer leeg is en behoud indien nodig de oude waarden
    if not nieuwe_straat:
        nieuwe_straat = oude_straat

    if not nieuwe_huisnummer:
        nieuwe_huisnummer = oude_huisnummer

    if not nieuwe_postcode:
        nieuwe_postcode = oude_postcode

    if not nieuwe_plaats:
        nieuwe_plaats = oude_plaats

    if not nieuwe_catagorie:
        nieuwe_catagorie = oude_catagorie

    # Definieer de waarden voor de adres update-query
    adres_values = (nieuwe_postcode, nieuwe_huisnummer, nieuwe_straat, nieuwe_plaats, nieuwe_catagorie, klantnummer)

    # Voer de query uit 
    mycursor.execute(query_adres, adres_values)
    mydb.commit()
