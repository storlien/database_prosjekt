CREATE TABLE KundeProfil (
    Mobilnummer VARCHAR(15) PRIMARY KEY,
    Navn VARCHAR(100),
    Adresse VARCHAR(255)
);
CREATE TABLE BillettKjop (
    KjopID INT PRIMARY KEY,
    Tid TIME,
    Dato DATE,
    Mobilnummer VARCHAR(8),
    FOREIGN KEY (Mobilnummer) REFERENCES KundeProfil(Mobilnummer)
        ON DELETE CASCADE ON UPDATE CASCADE
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