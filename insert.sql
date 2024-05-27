use mydb;

-- Insert Fietsen
INSERT INTO Fietsen (Fietsnummer, Merk, Model, Fietstype, Electrisch, Dagprijs, Aankoopdatum) values ('101', 'Gazelle', 'CityZen', 'Stadsfiets', True, 15,0, '22-01-01');
INSERT INTO Fietsen (Fietsnummer, Merk, Model, Fietstype, Electrisch, Dagprijs, Aankoopdatum) values ('102', 'Trek', 'FX 3 Disc', 'Hybride', False, 12,0, '22-02-15');
INSERT INTO Fietsen (Fietsnummer, Merk, Model, Fietstype, Electrisch, Dagprijs, Aankoopdatum) values ('103', 'Cortina', 'E-U4', 'Elektrische fiets', True, 20,0, '22-12-10');

-- Insert Klanten
INSERT INTO Klanten (idKlanten, voornaam, tussenvoegsel, achternaam) values ('001', 'Jan', '', 'Jantjes');
INSERT INTO Klanten (idKlanten, voornaam, tussenvoegsel, achternaam) values ('002', 'Peter', '', 'Peterson');
INSERT INTO Klanten (idKlanten, voornaam, tussenvoegsel, achternaam) values ('003', 'Mark', '', 'Rutte');
 
-- Insert Vestigingen
INSERT INTO Vestigingen (idVestiging, Vestigingnaam) values ('201', 'Amsterdam Centraal');
INSERT INTO Vestigingen (idVestiging, Vestigingnaam) values ('202', 'Rotterdam Zuid');
INSERT INTO Vestigingen (idVestiging, Vestigingnaam) values ('203', 'Den Haag Centrum');

-- Insert Contracten
INSERT INTO Contracten (contractnummer, vestigingnaam, klantnummer, startdatum, inleverdatum) values ('301', 'Amsterdam Centraal', 1, '2022-03-01', '2022-03-10');
INSERT INTO Contracten (contractnummer, vestigingnaam, klantnummer, startdatum, inleverdatum) values ('302', 'Rotterdam Zuid', 1, '2022-02-20', '2022-03-05');
INSERT INTO Contracten (contractnummer, vestigingnaam, klantnummer, startdatum, inleverdatum) values ('303', 'Den Haag', 1, '2022-01-15', '2022-01-25');
INSERT INTO Contracten (contractnummer, vestigingnaam, klantnummer, startdatum, inleverdatum) values ('304', 'Amsterdam Centraal', 1, '2022-03-25', '2022-09-23');

-- Insert Bedrijf
INSERT INTO Bedrijf (KVKnummer) VALUES ('12345678', 'NL01');

-- Insert Adres
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (1, '1012 AB', 9, 'Stationsplein', 'Amsterdam', 'Vestiging');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (2, '3071 AA', 393, 'Laan op Zuid', 'Rotterdam', 'Vestiging');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (3, '2511 BT', 68, 'Spui', 'Den Haag', 'Vestiging');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (4, '1012JS', 3, 'Dam', 'Amsterdam', 'particulier');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (5, '3010WW', 9, 'Leidseplein', 'Rotterdam', 'particulier');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (6, '2121AP', 9, 'Rembrandt', 'Den Haag', 'particulier');
INSERT INTO Adres (idAdres, postcode, Huisnummer, straat, plaats, categorie) VALUES (6, '2121AP', 9, 'Rembrandt', 'Den Haag', 'zakelijk');


-- Insert Gehuurde fietsen
-- INSERT INTO Gehuurde fietsen (idKlanten, voornaam, tussenvoegsel, achternaam) values ('001', 'Jan', '', 'Jantjes');

