PRAGMA foreign_keys = ON;

INSERT INTO TeaterSesong (SesongID, Aar, Aarstid)
VALUES
(1, 2024, 'Vinter/vår');

INSERT INTO Teatersal (SalNr, SalNavn)
VALUES
(1, 'Hovedscenen'),
(2, 'Gamle scene'),
(3, 'Studioscenen'),
(4, 'Teaterkjelleren'),
(5, 'Teaterkafeen');

INSERT INTO Teaterstykke (StykkeID, Tittel, SkrevetAv, SesongID, SalNr)
VALUES
(1, 'Kongsemnene', 'Henrik Ibsen', 1, 1),
(2, 'Størst av alt er kjærligheten', 'Jonas Corell Petersen', 1, 2);

INSERT INTO Omraade (OmraadeID, Navn, SalNr)
VALUES
(1, 'Hovedscenen', 1),
(2, 'Galleri', 1),
(3, 'Parkett', 2),
(4, 'Balkong', 2),
(5, 'Galleri', 2);

INSERT INTO Akt (StykkeID, AktNr, Navn)
VALUES
(1, 1, '1'),
(1, 2, '2'),
(1, 3, '3'),
(1, 4, '4'),
(1, 5, '5'),
(2, 1, '1');

INSERT INTO Rolle (RolleID, Navn)
VALUES
-- Roller til Kongsemnene (Medvirkende)
(1, 'Haakon Haakonssønn'),
(2, 'Dagfinn Bonde'),
(3, 'Jatgeir Skald'),
(4, 'Sigrid'),
(5, 'Ingebjørg'),
(6, 'Skule jarl'),
(7, 'Inga fra Vartejg'),
(8, 'Paal Flida'),
(9, 'Fru Ragnhild'),
(10, 'Gregorius Jonssønn'),
(11, 'Margrete'),
(12, 'Biskop Nikolas'),
(13, 'Peter'),
(14, 'Trønder'),
(15, 'Baard Bratte'),

-- Roller til Størst av alt er kjærligheten (Medvirkende)
(16, 'Sunniva Du Mond Nordal'),
(17, 'Jo Saberniak'),
(18, 'Marte M. Steinholt'),
(19, 'Tor Ivar Hagen'),
(20, 'Trond-Ove Skrødal'),
(21, 'Natalie Grøndahl Tangen'),
(22, 'Åsmund Flaten');

INSERT INTO PaaAkt (StykkeID, AktNr, RolleID)
VALUES
-- Håkon Håkonson
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(1, 4, 1),
(1, 5, 1),

-- Dagfinn Bonde
(1, 1, 2),
(1, 2, 2),
(1, 3, 2),
(1, 4, 2),
(1, 5, 2),

-- Jatgeir Skald
(1, 4, 3),

-- Sigrid
(1, 1, 4),
(1, 2, 4),
(1, 5, 4),

-- Ingebjørg
(1, 4, 5),

-- Skule Jarl
(1, 1, 6),
(1, 2, 6),
(1, 3, 6),
(1, 4, 6),
(1, 5, 6),

-- Inga frå Vartejg
(1, 1, 7),
(1, 3, 7),

-- Paal Flida
(1, 1, 8),
(1, 2, 8),
(1, 3, 8),
(1, 4, 8),
(1, 5, 8),

-- Fru Ragnhild
(1, 1, 9),
(1, 5, 9),

-- Gregorius Jonsson
(1, 1, 10),
(1, 2, 10),
(1, 3, 10),
(1, 4, 10),
(1, 5, 10),

-- Margrete
(1, 1, 11),
(1, 2, 11),
(1, 3, 11),
(1, 4, 11),
(1, 5, 11),

-- Biskop Nikolas
(1, 1, 12),
(1, 2, 12),
(1, 3, 12),

-- Peter
(1, 3, 13),
(1, 4, 13),
(1, 5, 13),

-- Trønder
(1, 1, 14),

-- Baard Bratte
(1, 2, 15),
(1, 3, 15),
(1, 4, 15),
(1, 5, 15),

-- Sunniva Du Mond Nordal
(2, 1, 16),

-- Jo Saberniak
(2, 1, 17),

-- Marte M. Steinholt
(2, 1, 18),

-- Tor Ivar Hagen
(2, 1, 19),

-- Trond-Ove Skrødal
(2, 1, 20),

-- Natalie Grøndahl Tangen
(2, 1, 21),

-- Åsmund Flaten
(2, 1, 22);

INSERT INTO Ansatt (AnsattID, Navn, Status)
VALUES
-- Roller i Kongsemnene
(1, 'Arturo Scotti', 'Fast'),
(2, 'Ingunn Beate Strige Øyen', 'Fast'),
(3, 'Hans Petter Nilsen', 'Fast'),
(4, 'Madeleine Brandtzæg Nilsen', 'Fast'),
(5, 'Synnøve Fossum Eriksen', 'Fast'),
(6, 'Emma Caroline Deichmann', 'Fast'),
(7, 'Thomas Jensen Takyi', 'Fast'),
(8, 'Per Bogstad Gulliksen', 'Fast'),
(9, 'Isak Holmen Sørensen', 'Fast'),
(10, 'Fabian Heidelberg Lunde', 'Fast'),
(11, 'Emil Olafsson', 'Fast'),
(12, 'Snorre Ryen Tøndel', 'Fast'),

-- Kunstnerisk lag i Kongsemnene
(13, 'Yury Butusov', 'Fast'),
(14, 'Aleksandr Shishkin-Hokusai', 'Fast'),
(15, 'Eivind Myren', 'Fast'),
(16, 'Mina Rype Stokke', 'Fast'),

-- Roller i Størst av alt er kjærligheten
(17, 'Sunniva Du Mond Nordal', 'Fast'),
(18, 'Jo Saberniak', 'Fast'),
(19, 'Marte M. Steinholt', 'Fast'),
(20, 'Tor Ivar Hagen', 'Fast'),
(21, 'Trond-Ove Skrødal', 'Fast'),
(22, 'Natalie Grøndahl Tangen', 'Fast'),
(23, 'Åsmund Flaten', 'Fast'),

-- Kustnerisk lag i Størst av alt er kjærligheten
(24, 'Jonas Corell Petersen', 'Fast'),
(25, 'David Gehrt', 'Fast'),
(26, 'Gaute Tønder', 'Fast'),
(27, 'Magnus Mikaelsen', 'Fast'),
(28, 'Kristoffer Spender', 'Fast');

INSERT INTO Skuespiller (AnsattID)
VALUES
-- Kongsemnene
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),

-- Størst av alt er kjærligheten
(17),
(18),
(19),
(20),
(21),
(22),
(23);

INSERT INTO SpillerRolle (AnsattID, RolleID)
VALUES
-- Roller i Kongsemnene
(1, 1),
(2, 7),
(3, 6),
(4, 9),
(5, 11),
(6, 4),
(6, 5),
(7, 12),
(8, 10),
(9, 8),
(9, 14),
(10, 15),
(10, 14),
(11, 3),
(11, 2),
(12, 13),

-- Roller i Størst av alt er kjærligheten
(17, 16),
(18, 17),
(19, 18),
(20, 19),
(21, 20),
(22, 21),
(23, 22);

INSERT INTO Oppgave(OID, Navn, StykkeID)
VALUES
-- Oppgaver til Kongsemnene (Kunsterisk lag)
(1, 'Regi og musikkutvelgelse', 1),
(2, 'Scenografi og kostymer', 1),
(3, 'Lysdesign', 1),
(4, 'Dramaturg', 1),

-- Oppgaver til Størst av alt er kjærligheten (Kunsterisk lag)
(5, 'Regi', 2),
(6, 'Scenografi og kostymer', 2),
(7, 'Musikalsk ansvarlig', 2),
(8, 'Lysdesign', 2),
(9, 'Dramaturg', 2);

INSERT INTO Utforer (OID, AnsattID)
VALUES
-- Oppgaver til Kongsemnene (Kunsterisk lag)
(1, 13),
(2, 14),
(3, 15),
(4, 16),

-- Oppgaver til Størst av alt er kjærligheten (Kunsterisk lag)
(5, 24),
(6, 25),
(7, 26),
(8, 27),
(9, 28);

INSERT INTO KundeGruppe (GruppeNavn)
VALUES
('Ordinær'),
('Barn'),
('Student'),
('Gruppe 10'),
('Gruppe honnør'),
('Honnør');

INSERT INTO BillettPriser (GruppeNavn, StykkeID, Pris)
VALUES
( 'Ordinær', 1, 450),
( 'Honnør', 1, 380),
( 'Student', 1, 280),
( 'Gruppe 10', 1, 420),
( 'Gruppe honnør', 1, 360),

( 'Ordinær', 2, 350),
( 'Barn', 2, 220),
( 'Student', 2, 220),
( 'Gruppe 10', 2, 320),
( 'Gruppe honnør', 2, 270),
( 'Honnør', 2, 300);

INSERT INTO Forestilling (StykkeID, ForestillingNr, Dato, Tid)
VALUES
-- Kongsemnene
(1, 1, '2024-02-01', '19:00'),
(1, 2, '2024-02-02', '19:00'),
(1, 3, '2024-02-03', '19:00'),
(1, 4, '2024-02-05', '19:00'),
(1, 5, '2024-02-06', '19:00'),

-- Størst av alt er kjærligheten
(2, 1, '2024-02-03', '18:30'),
(2, 2, '2024-02-06', '18:30'),
(2, 3, '2024-02-07', '18:30'),
(2, 4, '2024-02-12', '18:30'),
(2, 5, '2024-02-13', '18:30'),
(2, 6, '2024-02-14', '18:30');

INSERT INTO KundeProfil (Mobilnummer, Navn, Adresse)
VALUES
('55555555', 'Admin', 'Adminveien 1')