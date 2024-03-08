INSERT INTO KundeProfil (Mobilnummer, Navn, Adresse)
VALUES 
('12345678', 'Ola Nordmann', 'Gateadresse 123, 0123 Oslo'),
('23456789', 'Kari Nordmann', 'Annen gate 456, 0234 Oslo'),
('34567890', 'Per Hansen', 'Tredje vei 789, 0345 Bergen');

INSERT INTO BillettKjop (KjopID, Tid, Dato, Mobilnummer)
VALUES 
(1, '12:00:00', '2024-03-10', '12345678'),
(2, '14:30:00', '2024-03-11', '23456789'),
(3, '16:45:00', '2024-03-12', '34567890');

INSERT INTO Billett (BillettID, KjopID, StykkeID, ForestillingNr, BillettType, OmraadeID, SeteNr, RadNr)
VALUES 
(101, 1, 5, 3, 'Voksen', 2, 15, 3),
(102, 2, 6, 2, 'Student', 1, 10, 2),
(103, 3, 7, 1, 'Barn', 3, 5, 4);

INSERT INTO Sete (SeteNr, RadNr, OmraadeID)
VALUES 
(10, 2, 1),
(5, 4, 3);


INSERT INTO Omraade (OmraadeID, Navn, SalNr)
VALUES 
(4, 'Balkong', 2),
(5, 'Galleri', 3);


INSERT INTO KundeGruppe (GruppeNavn)
VALUES 
('Student'),
('Barn');


INSERT INTO Teatersal (SalNr, SalNavn)
VALUES 
(2, 'Hovedsalen'),
(3, 'Lillesalen');


INSERT INTO Teaterstykke (StykkeID, Tittel, SesongID, SalNr)
VALUES 
(6, 'Romeo og Julie', 1, 2),
(7, 'Hamlet', 2, 3);


INSERT INTO TeaterSesong (SesongID, Aar, Aarstid)
VALUES 
(1, 2024, 'Vår'),
(2, 2024, 'Sommer');


INSERT INTO Forestilling (StykkeID, ForestillingNr, Dato, Tid)
VALUES 
(6, 2, '2024-04-15', '19:00:00'),
(7, 1, '2024-05-20', '20:00:00');


INSERT INTO Ansatt (AnsattID, Navn, Email, Status)
VALUES
(1, 'Anna Solberg', 'anna@teater.no', 'Aktiv'),
(2, 'Lars Monsen', 'lars@teater.no', 'Aktiv');

INSERT INTO Skuespiller (AnsattID)
VALUES
(1),
(2);


INSERT INTO Rolle (RolleID, Navn)
VALUES
(1, 'Hovedrolle'),
(2, 'Biroolle');


INSERT INTO SpillerRolle (AnsattID, RolleID)
VALUES
(1, 1),
(2, 2);


INSERT INTO Akt (StykkeID, AktNr, Navn)
VALUES
(6, 1, 'Akt 1'),
(6, 2, 'Akt 2'),
(7, 1, 'Akt 1');

INSERT INTO PaaAkt (StykkeID, AktNr, RolleID)
VALUES
(6, 1, 1),
(6, 2, 2),
(7, 1, 1);

INSERT INTO Oppgave (OID, Navn, StykkeID)
VALUES
(1, 'Lysdesign', 6),
(2, 'Lydeffekter', 7);

INSERT INTO Utforer (OID, AnsattID)
VALUES
(1, 1),
(2, 2);

INSERT INTO ForGruppe (GruppeNavn, StykkeID, Pris)
VALUES
('Student', 6, 150),
('Barn', 7, 100);