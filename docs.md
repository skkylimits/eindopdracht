# Docs

## Python

Student heeft een programma gemaakt waarin alle 
verplichte onderdelen van Python zijn gebruikt: 

- Assignment 
- Input 
- Type casting 
- IF...ELIF...ELSE 
- WHILE loop 
- FOR loop 
- Lists of Tuples 
- Functies 
  
De student kan uitleggen hoe de verplichte onderdelen van 
Python zijn toegepast in de code.

```python
# Assignment: Toewijzen van waarden aan variabelen
x = 5
y = "Hello"
z = True

# Input: Gebruiker invoer ontvangen
name = input("Enter your name: ")

# Type casting: Omzetten van het ene gegevenstype naar het andere
num_str = input("Enter a number: ")
num_int = int(num_str)

# IF...ELIF...ELSE: Beslissingsstructuur
if num_int > 0:
    print("Positive number")
elif num_int < 0:
    print("Negative number")
else:
    print("Zero")

# WHILE loop: Herhaalde uitvoering van een blok code zolang een bepaalde voorwaarde waar is
count = 0
while count < 5:
    print(count)
    count += 1

# FOR loop: Itereren over een reeks items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Lists of Tuples: Een lijst van tuples waarbij elk tuple meerdere elementen kan bevatten
students = [("John", 20), ("Alice", 22), ("Bob", 21)]
for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}")

# Functies: Een stukje herbruikbare code dat een specifieke taak uitvoert
def add(a, b):
    return a + b

result = add(3, 5)
print("Result of addition:", result)

```


## BDA

- Entiteiten (min. 5 stuks) 
- (non-) identifying relationships 
- Relaties en hun kardinaliteiten 
- Constraints (PK, FK, NN, UQ) 
- Gegevenstypen 

Natuurlijk, laten we de verschillende concepten bekijken met betrekking tot entiteiten in databases:

### Entiteiten:

Dit zijn de objecten of concepten waarmee de database werkt, zoals klanten, producten, bestellingen, enz.

### Identificerende (Identifying) relaties:

Dit zijn relaties waarbij het kindentiteitstype afhankelijk is van het ouderentiteitstype voor zijn identiteit. Met andere woorden, het kind kan niet bestaan zonder het ouderentiteitstype. Bijvoorbeeld, een factuuritem kan alleen bestaan binnen de context van een factuur.
### Niet-identificerende (Non-identifying) relaties:

Dit zijn relaties waarbij het kindentiteitstype onafhankelijk bestaat van het ouderentiteitstype. Het kan bestaan zonder het ouderentiteitstype. Bijvoorbeeld, een klant kan verschillende bestellingen hebben, maar een bestelling kan bestaan zonder een specifieke klant.

### Relaties en hun kardinaliteiten:

### 1-op-1 relatie: 

Een record in de ene entiteit komt overeen met precies één record in de andere entiteit.    

### 1-op-veel relatie: 

Een record in de ene entiteit komt overeen met nul of meer records in de andere entiteit.

### Veel-op-veel relatie: 

Een record in de ene entiteit komt overeen met nul of meer records in de andere entiteit, en vice versa.
Constraints:

### Primary Key (PK): 

Uniek identificatiemechanisme voor een entiteit om duplicaten te voorkomen.

### Foreign Key (FK): 

Verwijst naar de primaire sleutel in een andere tabel en zorgt voor referentiële integriteit.

### Not Null (NN): 

Specificeert dat een kolom geen NULL-waarden mag bevatten.

### nique (UQ): 

Zorgt ervoor dat alle waarden in een kolom uniek zijn.

### Gegevenstypen:

Dit zijn de typen gegevens die een kolom kan bevatten, zoals integers, floats, strings, datums, enz.
Dit zijn de basiselementen waarmee je rekening moet houden bij het ontwerpen van databases en het definiëren van de structuur en relaties tussen entiteiten.

## SQL
Laten we elk van deze verplichte onderdelen toepassen in een voorbeeld van een databaseproject:

```sql

- **SELECT**: Gebruikt om gegevens uit een database te halen. Bijvoorbeeld: `SELECT * FROM Klant;` haalt alle klantgegevens op.

- **INSERT**: Gebruikt om nieuwe gegevens in een database in te voegen. Bijvoorbeeld: `INSERT INTO Klant (voornaam, achternaam) VALUES ('John', Johnsen);` voegt een nieuwe klant toe aan de tabel Klanten.

- **UPDATE**: Gebruikt om bestaande gegevens in een database bij te werken. Bijvoorbeeld: `UPDATE Klant SET voornaam = Johnny WHERE name = 'John';` wijzigt de leeftijd van de student met de naam 'John'.

- **DELETE**: Gebruikt om gegevens uit een database te verwijderen. Bijvoorbeeld: `DELETE FROM Klant WHERE klantID = '{klantnummer}';` verwijdert de klant met de klantnummer '{klantnummer}' uit de tabel Klant.

- **JOIN**: Gebruikt om gegevens uit meerdere tabellen te combineren. Bijvoorbeeld: `
SELECT *
FROM klant
RIGHT JOIN Adres
ON klant.klantID = Adres.adresID
` 

haalt de namen van klanten en hun adressen op, waarbij de gegevens worden gecombineerd uit de tabellen klant en Adres.

- **Group By**: Gebruikt om gegevens te groeperen op basis van een bepaalde kolom. Bijvoorbeeld: `
SELECT MIN(voornaam) AS voornaam -- of MAX(voornaam) of een andere aggregatiefunctie
FROM Klant
GROUP BY achternaam;
`
Haal alle unieke voornamen per achternaam.

- **View**: Een opgeslagen query die wordt behandeld als een virtuele tabel. Bijvoorbeeld: `
CREATE VIEW Fietsjes AS SELECT * FROM Fiets WHERE dagprijs > 1.0;
SHOW CREATE VIEW Fietsjes;
SELECT * FROM Fietsjes;
`

maakt een weergave van fietsen met de naam Fietsjes met een dagprijs van meer dan 1.

- **Subquery**: Een query die is genest in een andere query. Bijvoorbeeld: `SELECT name FROM Students WHERE age IN (SELECT MAX(age) FROM Students);` ha alt de namen op van studenten met de hoogste leeftijd.

- **Pattern search m.b.v. LIKE**: Gebruikt om gegevens te zoeken op basis van een patroon. Bijvoorbeeld: `SELECT * FROM klant WHERE achternaam LIKE '%{deel_achternaam}%` haalt alle namen op waarvan de naam '{deel_achternaam}' bevat.
```

In een databaseproject kunnen deze SQL-opdrachten worden gebruikt om gegevens te manipuleren, te analyseren en op te halen op een gestructureerde manier. Elke opdracht heeft een specifieke functie en biedt flexibiliteit bij het werken met databases.
