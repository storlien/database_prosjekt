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
    Mobilnummer INT(8),
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