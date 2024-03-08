-- KundeProfil-tabellen
CREATE TABLE KundeProfil (
    Mobilnummer VARCHAR(15) PRIMARY KEY,
    Navn VARCHAR(100),
    Adresse VARCHAR(255)
);

-- BillettKjop-tabellen
CREATE TABLE BillettKjop (
    KjopID INT PRIMARY KEY,
    Tid TIME,
    Dato DATE,
    Mobilnummer VARCHAR(15),
    FOREIGN KEY (Mobilnummer) REFERENCES KundeProfil(Mobilnummer)
);

-- Billett-tabellen
CREATE TABLE Billett (
    BillettID INT PRIMARY KEY,
    KjopID INT,
    StykkeID INT,
    ForestillingNr INT,
    BillettType VARCHAR(50),
    OmraadeID INT,
    SeteNr INT,
    RadNr INT,
    FOREIGN KEY (KjopID) REFERENCES BillettKjop(KjopID),
    FOREIGN KEY (StykkeID, ForestillingNr) REFERENCES Forestilling(StykkeID, ForestillingNr),
    FOREIGN KEY (BillettType) REFERENCES KundeGruppe(GruppeNavn),
    FOREIGN KEY (OmraadeID, SeteNr, RadNr) REFERENCES Sete(OmraadeID, SeteNr, RadNr)
);

-- Sete-tabellen
CREATE TABLE Sete (
    SeteNr INT,
    RadNr INT,
    OmraadeID INT,
    PRIMARY KEY (SeteNr, RadNr, OmraadeID)
);

-- Omraade-tabellen
CREATE TABLE Omraade (
    OmraadeID INT PRIMARY KEY,
    Navn VARCHAR(100),
    SalNr INT,
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
);

-- KundeGruppe-tabellen
CREATE TABLE KundeGruppe (
    GruppeNavn VARCHAR(50) PRIMARY KEY
);

-- Teatersal-tabellen
CREATE TABLE Teatersal (
    SalNr INT PRIMARY KEY,
    SalNavn VARCHAR(100)
);

-- Teaterstykke-tabellen
CREATE TABLE Teaterstykke (
    StykkeID INT PRIMARY KEY,
    Tittel VARCHAR(100),
    SesongID INT,
    SalNr INT,
    FOREIGN KEY (SesongID) REFERENCES TeaterSesong(SesongID),
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
);

-- TeaterSesong-tabellen
CREATE TABLE TeaterSesong (
    SesongID INT PRIMARY KEY,
    Aar INT,
    Aarstid VARCHAR(50)
);

-- Forestilling-tabellen
CREATE TABLE Forestilling (
    StykkeID INT,
    ForestillingNr INT,
    Dato DATE,
    Tid TIME,
    PRIMARY KEY (StykkeID, ForestillingNr),
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
);

-- ... (og så videre for andre tabeller)

