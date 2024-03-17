CREATE TABLE KundeProfil (
    Mobilnummer INTEGER PRIMARY KEY,
    Navn VARCHAR(100),
    Adresse VARCHAR(255)
);

CREATE TABLE BillettKjop (
    KjopID INTEGER PRIMARY KEY,
    Tid TIME,
    Dato DATE,
    Mobilnummer INTEGER,
    FOREIGN KEY (Mobilnummer) REFERENCES KundeProfil(Mobilnummer)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Billett (
    BillettID INTEGER PRIMARY KEY,
    KjopID INTEGER,
    StykkeID INTEGER,
    ForestillingNr INTEGER,
    BillettType VARCHAR(50),
    OmraadeID INTEGER,
    SeteNr INTEGER,
    RadNr INTEGER,
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
    SeteNr INTEGER,
    RadNr INTEGER,
    OmraadeID INTEGER,
    PRIMARY KEY (SeteNr, RadNr, OmraadeID),
    FOREIGN KEY (OmraadeID) REFERENCES Omraade(OmraadeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Omraade (
    OmraadeID INTEGER PRIMARY KEY,
    Navn VARCHAR(100),
    SalNr INTEGER,
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE KundeGruppe (
    GruppeNavn VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Teatersal (
    SalNr INTEGER PRIMARY KEY,
    SalNavn VARCHAR(100)
);

CREATE TABLE Teaterstykke (
    StykkeID INTEGER PRIMARY KEY,
    Tittel VARCHAR(100),
    SkrevetAv VARCHAR(100),
    SesongID INTEGER,
    SalNr INTEGER,
    FOREIGN KEY (SesongID) REFERENCES TeaterSesong(SesongID)
        ON DELETE SET NULL ON UPDATE CASCADE,
    FOREIGN KEY (SalNr) REFERENCES Teatersal(SalNr)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE TeaterSesong (
    SesongID INTEGER PRIMARY KEY,
    Aar INTEGER,
    Aarstid VARCHAR(50),
    UNIQUE (Aar, Aarstid)
);

CREATE TABLE Forestilling (
    StykkeID INTEGER,
    ForestillingNr INTEGER,
    Dato DATE,
    Tid TIME,
    PRIMARY KEY (StykkeID, ForestillingNr),
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ForGruppe (
    GruppeNavn VARCHAR(50),
    StykkeID INTEGER,
    Pris DECIMAL(10,2),
    PRIMARY KEY (GruppeNavn, StykkeID),
    FOREIGN KEY (GruppeNavn) REFERENCES KundeGruppe(GruppeNavn)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ansatt (
    AnsattID INTEGER PRIMARY KEY,
    Navn VARCHAR(100),
    Email VARCHAR(100),
    Status VARCHAR(50)
);

CREATE TABLE Skuespiller (
    AnsattID INTEGER,
    PRIMARY KEY (AnsattID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Rolle (
    RolleID INTEGER PRIMARY KEY,
    Navn VARCHAR(100)
);

CREATE TABLE SpillerRolle (
    AnsattID INTEGER,
    RolleID INTEGER,
    PRIMARY KEY (AnsattID, RolleID),
    FOREIGN KEY (AnsattID) REFERENCES Skuespiller(AnsattID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Akt (
    StykkeID INTEGER,
    AktNr INTEGER,
    Navn VARCHAR(100),
    PRIMARY KEY (StykkeID, AktNr),
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PaaAkt (
    StykkeID INTEGER,
    AktNr INTEGER,
    RolleID INTEGER,
    PRIMARY KEY (StykkeID, AktNr, RolleID),
    FOREIGN KEY (StykkeID, AktNr) REFERENCES Akt(StykkeID, AktNr)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID)
        ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE Oppgave (
    OID INTEGER PRIMARY KEY,
    Navn VARCHAR(100),
    StykkeID INTEGER,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Utforer (
    OID INTEGER,
    AnsattID INTEGER,
    PRIMARY KEY (OID, AnsattID),
    FOREIGN KEY (OID) REFERENCES Oppgave(OID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID)
        ON DELETE NO ACTION ON UPDATE CASCADE
);