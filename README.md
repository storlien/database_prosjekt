# Prosjekt i TDT4145 - Databasesystem for Trøndelag Teater
Prosjekt i faget TDT4145: Datamodellering og databasesystemer

## Hvordan raskt sette opp alle tabeller med innsetting av data

Kjør kommando: python3 complete_setup_theatre.py teater.db

## Hvordan sette opp databasen med tabeller
//TODO
1. Kommando sqlite3 teater.db
2. Kommando .read setup_tables.sql

##  Hvordan sette inn testdata
//TODO

## Forutsetninger eller andre merknader

Roller i Kongsemnene:
Guttorm Ingesson fantes ikke på nettsiden, så vi har ikke lagt inn denne i databasen.
Trønder stod ikke oppført i prosjektbeskrivelsen, men den fantes på nettsiden. Den er derfor satt til å spille i akt 1 siden vi antar det egentlig er rollen Guttorm Ingesson.

Baard Bratte var ikke satt opp på noen akter i tabellen i prosjektbeskrivelsen, så vi antar rollen spilles på akter 2, 3, 4 og 5.