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
('Gazelle', 'Ultimate', 'Herenfiets', 'False', '15.0', '2023-05-14', 1),
('Batavus', 'Finez', 'Stadsfiets', 'True', '12.5', '2022-11-03', 2),
('Sparta', 'Ion', 'Elektrische fiets', 'True', '20.0', '2021-07-22', 3),
('Koga', 'F3', 'Hybride fiets', 'False', '18.0', '2023-09-11', 1),
('Trek', 'Domane', 'Racefiets', 'False', '22.0', '2024-01-05', 2),
('Giant', 'Explore', 'Mountainbike', 'True', '17.0', '2022-02-17', 3),
('Cannondale', 'Quick', 'Gravelbike', 'False', '19.0', '2023-04-29', 1),
('Cube', 'Kathmandu', 'Reisfiets', 'True', '21.0', '2024-03-08', 2),
('Merida', 'Scultura', 'Racefiets', 'False', '23.0', '2022-06-20', 3),
('Scott', 'Addict', 'Racefiets', 'True', '24.0', '2021-12-10', 1),
('Specialized', 'Diverge', 'Gravelbike', 'False', '25.0', '2023-10-15', 2),
('Santa Cruz', 'Hightower', 'Mountainbike', 'True', '26.0', '2024-02-22', 3),
('BMC', 'Roadmachine', 'Racefiets', 'False', '27.0', '2021-09-18', 1),
('Focus', 'Mares', 'Cyclocross', 'True', '28.0', '2023-11-07', 2),
('Orbea', 'Gain', 'Elektrische fiets', 'True', '29.0', '2022-03-12', 3),
('Riese & Muller', 'Superdelite', 'Elektrische fiets', 'True', '30.0', '2023-08-25', 1),
('VanMoof', 'S3', 'Stadsfiets', 'True', '31.0', '2021-05-30', 2),
('Liv', 'Langma', 'Racefiets', 'False', '32.0', '2024-04-10', 3),
('Bianchi', 'Oltre', 'Racefiets', 'True', '33.0', '2022-01-19', 1),
('Pinarello', 'Dogma', 'Racefiets', 'False', '34.0', '2023-06-14', 2);

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
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '5', '2024-05-08', '2024-05-28');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-08', 3);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '4', '2024-05-08', '2024-06-13');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-03', 4);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '5', '2024-05-03', '2024-05-05');

INSERT INTO contract(datum, c_klantID) VALUES('2024-05-02', 5);
SET @contract_id = LAST_INSERT_ID();
INSERT INTO Huur(Contracten_ContractNummer, Fiets_Fietsnummer, startdatum, inleverdatum) VALUES(@contract_id, '6', '2024-05-02', '2024-05-19');

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

