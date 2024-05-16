# Eindopdracht

- [ ] Add cursor close where needed
- [ ] fix functie 2
- [ ] fix functie met database 7
- [ ] cannot add or update a child row  a foreign key contraint --> INSERT query --> kan geen klanten, fietsen, contracten toevoegen
- [ ] contracten heeft niet alle benodige tabellen
- [ ] toon contract update gehuurde fietsen in lijst & maak het zodat er uit de database datagehaald wordt

## Inleiding

Deze eindopdracht voor de vakken Databases en Programming wordt uitgevoerd in tweetallen. 

Het is toegestaan (en aan te raden) de werkzaamheden te verdelen, maar let op: beiden worden op alle
onderdelen getoetst. 

Zorg er dus voor dat je kennis hebt van alles wat de ander oplevert.

## Casus

Fietsverhuurbedrijf GoDutch uit Amsterdam wil een nieuw systeem laten maken voor het vastleggen
van de verhuur van fietsen aan klanten.

GoDutch heeft 3 vestigingen, in het Centraal Station, op de NDSM werf en in het WTC bij station
Zuid. Om klanten goed te kunnen helpen, moeten medewerkers gegevens van de fietsen en de
vestigingen regelmatig opzoeken. GoDutch wil graag dat deze gegevens opgeslagen worden in de
database.

Klanten kunnen een of meerdere fietsen huren bij een van de drie vestigingen. Om een contract te
kunnen opstellen moet van de klant de voornaam, achternaam, adres en woonplaats vastgelegd zijn.
De klant kan dan een contract afsluiten voor de huur van een of meerdere fietsen bij een van de
vestigingen. 

Klanten kunnen met één contract meerdere fietsen huren.

Alle fietsen hebben een uniek fietsnummer dat te lezen is op het stuur. 

Van iedere fiets willen we het merk en de aankoopdatum vastleggen zodat we kunnen zien hoe oud iedere fiets is.

GoDutch biedt verschillende type fietsen aan, nl. de vier modellen dames, heren, tandem en bakfiets
die ieder een gewone en elektrische variant kennen. 

Elk type fiets heeft een eigen dagprijs. Voor
marketingredenen heeft elk fietstype een unieke wervende naam gekregen, bijv. ‘Randstad Racer D’
voor de elektrische damesfiets en ‘Grachten Caddy’ voor de niet-elektrische bakfiets.

Wanneer de klant de fiets huurt, wordt ook de inleverdatum ingevuld. 

Op basis van de bovenstaande informatie wordt een contract gemaakt waarop het totaalbedrag wordt getoond, gebaseerd op een
berekening met de gegevens in de database.

## Op te leveren producten

- [ ] Een Python script
- [x] Een ERD
- [ ] Een Relationeel Model
- [x] Een SQL script om de database te creëren

## Checklist

- [x] Maak een ERD in Lucidchart.
- [ ] Maak van het ERD een Relationeel Model in MySQL Workbench.
- [x] Maak van het Relationeel Model een fysieke database met de optie Forward Engineering.
- [ ] Vul de database met de gegevens uit het voorbeeldcontract.
- [ ] Schrijf een Python programma met daarin het gevraagde menu en functies.
- [x] Met de functie zoeken_klant() kan op een deel van de achternaam worden gezocht.
- [ ] De functie toon_alle_gegevens( ) toont de gegevens van alle klanten, fietsen en contracten
      gesorteerd en overzichtelijk met behulp van string formatting. Voor ieder contract dient de
      totaalprijs te worden getoond. De klanten dienen gesorteerd te worden getoond op
      achternaam, de fietsen op aankoopdatum en de contracten op startdatum.

## Test programma

Voer de volgende acties uit om je programma te testen:

1. Maak een nieuwe (bak)fiets aan van het merk Gazelle die gekocht is op de eerste dag
   van de huidige maand. Deze is van het type elektrische bakfiets met de naam ‘Grachten
   Cab’ die 85 euro per dag kost.

2. Maak twee nieuwe fietsen aan van het type ‘Randstad Rider H’.

3. Maak een nieuw contract aan voor een nieuwe klant in de vestiging NDSM en verhuur
   één elektrische herenfiets.

4. Wijzig het adres en de woonplaats van een bestaande klant.
   
5. Toon het contract dat je hebt aangemaakt bij stap 3. Let op: alle contractgegevens
   moeten uit de database worden opgehaald.

6. Toon alle klant-, fiets en contractgegevens gesorteerd en overzichtelijk op het scherm.

## Maak een applicatie voor fietsverhuurbedrijf GoDutch.

• Maak een applicatie waarmee contracten met klant- en fietsgegevens worden vastgelegd en
geprint kunnen worden. De gegevens op het geprinte contract moeten zoveel mogelijk op
dezelfde plek staan en uitgelijnd zijn als in het voorbeeldcontract.

### De applicatie moet een menu tonen waarin de gebruiker uit de volgende functionaliteiten kan kiezen:

1. Klant toevoegen
2. Klant wijzigen
3. Klant verwijderen
4. Klant zoeken
5. Fiets toevoegen
6. Contract opstellen
7. Contract printen
8. Overzicht alle gegevens
9. Programma beëindigen


### Maak hiervoor de volgende functies:

10. toevoegen_klant()
11. wijzigen_klant(klantnummer)
12. verwijderen_klant(klantnummer)
13. zoeken_klant()
14. toevoegen_fiets()
15. toevoegen_contract(klantnummer, vestigingsnaam)
16. toon_contract(contractnummer)
    NB: Je hoeft alleen de gegevens op de juiste plek in het contract te tonen. Het logo, de belijning, de
    tabellen en de kleuren dienen hier alleen ter illustratie.
17. toon_alle_gegevens()

 - De gegevens van de applicatie dienen te worden opgeslagen in een database:
    - Van een klant worden de volgende gegevens vastgelegd:
        - Klantnummer
        - Voornaam
        - Achternaam
        - Adres
        - Postcode
        - Woonplaats
        - Bankrekeningnummer
    - Van een fiets worden de volgende gegevens vastgelegd:
        - Fietsnummer
        - Merk
        - Model
        - Fietstype
        - Elektrisch
        - Dagprijs
        - Aankoopdatum
    - Van een vestiging worden de volgende gegevens vastgelegd:
        - Vestigingsnaam
        - Adres
        - Postcode
        - Plaats
    - Een contract bestaat uit de volgende gegevens:
        - Contractnummer
        - Vestigingsnaam
        - Klantnummer
        - Startdatum
        - Inleverdatum
        - Een overzicht van gehuurde fietsen


## Cyber Security

Specifieke opdracht voor Cyber Security

1. Zorg ervoor dat het bankrekeningnummer van de klant gecodeerd wordt opgeslagen in de
   database, maar ongecodeerd wordt getoond op het scherm.

2. Maak een nieuwe gebruiker aan in de database en geef deze gebruiker alleen SELECT
   rechten.

## BDA

Specifieke opdracht voor Cyber Security

1. Zorg ervoor dat het bankrekeningnummer van de klant gecodeerd wordt opgeslagen in de
   database, maar ongecodeerd wordt getoond op het scherm.

2. Maak een nieuwe gebruiker aan in de database en geef deze gebruiker alleen SELECT
   rechten.
