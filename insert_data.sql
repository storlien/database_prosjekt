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
(2, 'Parkett', 2),
(3, 'Balkong', 2),
(4, 'Galleri', 2);