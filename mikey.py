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
    ["Contractnummer", "Klantnummer", "Vestigingsnaam", "Startdatum", "Inleverdatum"],
    [301, 1, "Amsterdam Centraal", "2022-03-01", "2022-03-10"],
    [302, 2, "Rotterdam Zuid", "2022-02-20", "2022-03-05"],
    [303, 3, "Den Haag Centrum", "2022-01-15", "2022-01-25"],
    [303, 4, "Utrecht Centrum", "2022-03-25", "2022-09-23"]
]

def toon_contract(contractnummer):
    contractnummer = 309
    width_langste_woord = 10  # De breedte van de breedste term, rekening houdend met "Vestiging:"
    datum = '12-09-2024'
    vestiging = 'Amsterdam'
    adres = 'Keizersgracht 123'
    huisnummer = '1015 CJ'
    voornaam = 'Jan'
    achternaam = 'Jantjes'
    klantnummer = '1'
    startdatum = '21-06-2024'
    inleverdatum = '27-0-2024'
    aantal_dagen = 4

    # Logo
    print("              ____  ")
    print("             /  __\\")
    print("            (  @ @ )")
    print("             \\  O /")
    print("              \\__/ ")
    print("                    ")

    # Print contractinformatie
    print(f"Contractnr: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Datum: {str(datum):<{width_langste_woord}}", end="\n")
    
    # Print vestinging adresinformatie
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Vestiging: {str(vestiging):<{width_langste_woord}}")
    print(f"Adres: {str(adres):<{width_langste_woord}}", end="\n")
    print(f"Huisnummer: {str(huisnummer):<{width_langste_woord}}")

    # Print klant adresinformatie
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Klant: {str(voornaam):<{3}}, {str(achternaam)} (klantnr {klantnummer})")
    print(f"Adres: {str(adres):<{width_langste_woord}}", end="\n")
    print(f"Huisnummer: {str(huisnummer):<{width_langste_woord}}")

    # Print start & inleverdatum
    print(f"{'':<{width_langste_woord}}", end="\n")  # Ruimte voor de kolom "Contractnr:" en "Datum:"
    print(f"Stardatum: {str(startdatum):<{width_langste_woord}}")
    print(f"Inleverdatum: {str(inleverdatum):<{width_langste_woord}} --> aantal dagen: {aantal_dagen}", end="\n")
    print("")

    print(f'-----------------------------------------------', end="\n")

    # Fietsen
    print("")
    print("FIETSEN")

    width_langste_woord = 5
    print(f"Fietsnr: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Type: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Model: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Elektrisch: {str(contractnummer):<{width_langste_woord}}", end="\t")
    print(f"Prijs per dag: {str(datum):<{width_langste_woord}}", end="\n")

    # Totaal
    print("")
    print("TOTAAL")

   # Print the empty space and then the address information
   # Print the headers
    # Assuming width_langste_woord is defined and has the same value in both blocks

    # Print the headers
    print(f"{'':<{width_langste_woord}}Aantal dagen", end="\t")
    print(f"{'':<{width_langste_woord}}Prijs per dag", end="\t")
    print(f"{'':<{width_langste_woord}}Totaalbedrag", end="\n")

    # Print the data
    print(f"{'':<{width_langste_woord}}{aantal_dagen}", end="\t")
    print(f"{'':<{width_langste_woord}}{aantal_dagen}", end="\t")
    print(f"{'':<{width_langste_woord}}{aantal_dagen}", end="\n")



toon_contract(2)