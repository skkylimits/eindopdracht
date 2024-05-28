USE mydb;

--
-- Vestigingen --
--

-- Voeg eerst het adres toe aan de adresstabel
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie)
VALUES ('1012AB', '1', 'Stationsplein', 'Amsterdam', '1');

-- Haal het gegenereerde adres-ID op
SET @adres_id = LAST_INSERT_ID();

-- Voeg vervolgens vestiging toe met het juiste adres-ID
INSERT INTO Vestiging (Vestegingsnaam, v_adresID)
VALUES ('Centraal Station', @adres_id);

-- NDSM
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie)
VALUES ('1033WB', '2', 'NDSM-Plein', 'Amsterdam', '1');

SET @adres_id = LAST_INSERT_ID();

INSERT INTO Vestiging (Vestegingsnaam, v_adresID)
VALUES ('NDSM', @adres_id);

-- WTC
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie)
VALUES ('1077XW', '3', 'Zuidplein', 'Amsterdam', '1');

SET @adres_id = LAST_INSERT_ID();

INSERT INTO Vestiging (Vestegingsnaam, v_adresID)
VALUES ('WTC', @adres_id);

--
-- Fiets --
--

-- Voeg fiets toe aan de fietstabel
INSERT INTO Fiets (merk, model, fietstype, elektrisch, dagprijs, aankoopdatum, f_vestegingsID) VALUES
-- Damesfietsen
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),
('Gazelle', 'Randstad Racer D’', 'Damesfiets', 'True', '18.0', '2023-04-14', 1),

-- Bakfietsen
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),
('Urban Arrow', 'Grachten Caddy', 'Bakfiets', 'False', '25.0', '2024-02-15', 3),

-- Herenfietsen
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),
('Batavus', 'Urban Cruiser H', 'Herenfiets', 'False', '14.0', '2022-10-03', 2),

-- Tandems
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1),
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1),
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1),
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1),
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1),
('Koga', 'Dynamic Duo', 'Tandem', 'False', '25.0', '2023-11-21', 1);
--
-- Klant --
--

-- Voeg eerst het adres toe aan de adresstabel voor de eerste klant
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('1012JS', '3', 'Dam', 'Amsterdam', '2');

-- Haal het gegenereerde adres-ID op voor de eerste klant
SET @adres_id = LAST_INSERT_ID();

-- Voeg vervolgens de klant toe met het juiste adres-ID
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('Johnny', '', 'Cash', 'NL12ABCD3456789012', @adres_id);

-- Tweede klant in Haarlem
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('2011LK', '5', 'Grote Markt', 'Haarlem', '2');
SET @adres_id = LAST_INSERT_ID();
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('Elvis', '', 'Presley', 'NL34EFGH5678901234', @adres_id);

-- Derde klant in Purmerend
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('1441BR', '12', 'Koemarkt', 'Purmerend', '2');
SET @adres_id = LAST_INSERT_ID();
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('Frank', '', 'Sinatra', 'NL56IJKL6789012345', @adres_id);

-- Vierde klant in Zaandam
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('1506MA', '7', 'Gedempte Gracht', 'Zaandam', '2');
SET @adres_id = LAST_INSERT_ID();
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('Ray', '', 'Charles', 'NL78MNOP7890123456', @adres_id);

-- Vijfde klant in Amstelveen
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('1181GC', '8', 'Stadstuinen', 'Amstelveen', '2');
SET @adres_id = LAST_INSERT_ID();
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('James', '', 'Brown', 'NL90QRST8901234567', @adres_id);

-- Zesde klant in Hoofddorp
INSERT INTO Adres (postcode, huisnummer, straat, plaats, catagorie) 
VALUES ('2132TZ', '10', 'Hoofdweg', 'Hoofddorp', '2');
SET @adres_id = LAST_INSERT_ID();
INSERT INTO Klant (voornaam, tussenvoegsel, achternaam, bankrekeningnummer, k_adresID) 
VALUES ('Marvin', '', 'Gaye', 'NL12UVWX9012345678', @adres_id);

--
-- Contract --
--

-- Voeg eerst het contract toe aan de huur
INSERT INTO contract(datum, c_klantID) VALUES('2024-05-08', 2);

-- Haal het gegenereerde contract-ID op
SET @contract_id = LAST_INSERT_ID();

-- Voeg vervolgens het contract toe met het juiste contract-ID
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '1', '2024-05-08', '2024-05-28');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-08', 3);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '2', '2024-05-08', '2024-06-13');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-03', 4);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '3', '2024-05-03', '2024-05-05');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-02', 5);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '4', '2024-05-02', '2024-05-19');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-13', 6);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '7', '2024-05-13', '2024-05-25');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-21', 1);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '8', '2024-05-21', '2024-07-11');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-16', 2);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '9', '2024-05-16', '2024-06-11');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-03', 3);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '10', '2024-05-03', '2024-05-23');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-04', 4);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '11', '2024-05-04', '2024-05-15');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-14', 5);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '12', '2024-05-14', '2024-05-21');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-01', 6);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '13', '2024-05-01', '2024-06-10');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-03', 1);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '14', '2024-05-02', '2024-05-29');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-11', 2);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '15', '2024-05-11', '2024-06-15');

