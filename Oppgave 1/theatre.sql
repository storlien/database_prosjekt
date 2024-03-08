DROP TABLE IF EXISTS Forestilling;
DROP TABLE IF EXISTS TeaterSesong;
DROP TABLE IF EXISTS KundeProfil;
DROP TABLE IF EXISTS BillettKjop;
DROP TABLE IF EXISTS Billett;
DROP TABLE IF EXISTS Sete;
DROP TABLE IF EXISTS Omraade;
DROP TABLE IF EXISTS KundeGruppe;
DROP TABLE IF EXISTS Teatersal;
DROP TABLE IF EXISTS Teaterstykke;
DROP TABLE IF EXISTS ForGruppe;
DROP TABLE IF EXISTS Ansatt;
DROP TABLE IF EXISTS Skuespiller;
DROP TABLE IF EXISTS Rolle;
DROP TABLE IF EXISTS SpillerRolle;
DROP TABLE IF EXISTS Akt;
DROP TABLE IF EXISTS PaaAkt;
DROP TABLE IF EXISTS Oppgave;
DROP TABLE IF EXISTS Utforer;



CREATE TABLE KundeProfil (
    Mobilnummer INT(8) PRIMARY KEY,
    Navn VARCHAR(100),
    Adresse VARCHAR(255)
);

CREATE TABLE BillettKjop (
    KjopID INT PRIMARY KEY,
    Tid TIME,
    Dato DATE,
    Mobilnummer INT(8), -- Norske mobilnummer er 8 siffer
    FOREIGN KEY (Mobilnummer) REFERENCES KundeProfil(Mobilnummer)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Billett (
    BillettID INT PRIMARY KEY,
    KjopID INT,
    StykkeID INT,
    ForestillingNr INT,
    BillettType VARCHAR(50),
    OmraadeID INT,
    SeteNr INT,
    RadNr INT,
    FOREIGN KEY (KjopID) REFERENCES BillettKjop(KjopID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (StykkeID, ForestillingNr) REFERENCES Forestilling(StykkeID, ForestillingNr)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (BillettType) REFERENCES KundeGruppe(GruppeNavn)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (OmraadeID, SeteNr, RadNr) REFERENCES Sete(OmraadeID, SeteNr, RadNr)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Sete (
    SeteNr INT,
    RadNr INT,
    OmraadeID INT,
    PRIMARY KEY (SeteNr, RadNr, OmraadeID),
    FOREIGN KEY (OmraadeID) REFERENCES Omraade(OmraadeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Omraade (
    OmraadeID INT PRIMARY KEY,
    Navn VARCHAR(100),
    SalNr INT,
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE KundeGruppe (
    GruppeNavn VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Teatersal (
    SalNr INT PRIMARY KEY,
    SalNavn VARCHAR(100)
);

CREATE TABLE Teaterstykke (
    StykkeID INT PRIMARY KEY,
    Tittel VARCHAR(100),
    SesongID INT,
    SalNr INT,
    FOREIGN KEY (SesongID) REFERENCES TeaterSesong(SesongID)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE TeaterSesong (
    SesongID INT PRIMARY KEY,
    Aar INT,
    Aarstid VARCHAR(50)
);

CREATE TABLE Forestilling (
    StykkeID INT,
    ForestillingNr INT,
    Dato DATE,
    Tid TIME,
    PRIMARY KEY (StykkeID, ForestillingNr),
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ForGruppe (
    GruppeNavn VARCHAR(50),
    StykkeID INT,
    Pris DECIMAL(10,2),
    PRIMARY KEY (GruppeNavn, StykkeID),
    FOREIGN KEY (GruppeNavn) REFERENCES KundeGruppe(GruppeNavn)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    Navn VARCHAR(100),
    Email VARCHAR(100),
    Status VARCHAR(50)
);

CREATE TABLE Skuespiller (
    AnsattID INT,
    PRIMARY KEY (AnsattID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    Navn VARCHAR(100)
);

CREATE TABLE SpillerRolle (
    AnsattID INT,
    RolleID INT,
    PRIMARY KEY (AnsattID, RolleID),
    FOREIGN KEY (AnsattID) REFERENCES Skuespiller(AnsattID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Akt (
    StykkeID INT,
    AktNr INT,
    Navn VARCHAR(100),
    PRIMARY KEY (StykkeID, AktNr),
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PaaAkt (
    StykkeID INT,
    AktNr INT,
    RolleID INT,
    PRIMARY KEY (StykkeID, AktNr, RolleID),
    FOREIGN KEY (StykkeID, AktNr) REFERENCES Akt(StykkeID, AktNr)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID)
        ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE Oppgave (
    OID INT PRIMARY KEY,
    Navn VARCHAR(100),
    StykkeID INT,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Utforer (
    OID INT,
    AnsattID INT,
    PRIMARY KEY (OID, AnsattID),
    FOREIGN KEY (OID) REFERENCES Oppgave(OID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
        ON DELETE NO ACTION ON UPDATE CASCADE
);

-- test data 

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

