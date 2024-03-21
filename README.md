# Prosjekt i TDT4145 - Databasesystem for Trøndelag Teater
Prosjekt i faget TDT4145: Datamodellering og databasesystemer

Det forutsettes at du har installert Python (versjon 3) og SQLite (versjon 3) for å kunne utføre stegene.

## Mappestruktur - kort forklaring

- `/api` inneholder klasser som håndterer spørringer relatert til brukerhistorie 1-3

- `/seats_bought` inneholder alle tekstfiler delt ut for prosjektet

- `/setup` inneholder spørringer for sette opp databasen, samt sette inn data til databasen

- `/user_stories` ligger alle skripts som besvarer hver enkelt brukerhistorie. Mer om hvordan vi interagerer med disse brukerhistoriene kommer under.

NB: `scan_seats` ligger i rotmappa da vi ser på denne som essensiell for de fleste *user_stories*

## Hvordan raskt sette opp alle tabeller med innsetting av data

1. Kjør kommando i terminalen: 

```zsh
python3 complete_setup_theatre.py
```

Dette skriptet lager en databasefil som heter **teater.db** i rotmappa, setter opp alle tabeller og setter inn data for to teaterstykker i henhold til prosjektbeskrivelsen og informasjon fra nettsiden til Trøndelag Teater.

**Det er nå klart for å interagere med databasen!**

## Hvordan manuelt sette opp databasen med tabeller og data

Dersom du ikke ønsker å raskt sette opp databasen med tabeller og data gjennom ett enkelt skript, kan hvert steg gjøres hver for seg.

Du må være i sqlite3-shellet for å kjøre kommandoen for [oppsetting av tabeller](#hvordan-sette-opp-databasen-med-tabeller) og [innsetting av data](#hvordan-sette-inn-data).

Kjør kommando:

```zsh
sqlite3 teater.db
```

Denne kommandoen åpner sqlite3-shellet tilknyttet databasefil kalt teater.db. Du vet du er i sqlite3-shellet når hver linje i terminalen starter med "sqlite>".

### Hvordan sette opp databasen med tabeller

1. Gitt at du er i sqlite3-shellet, kjør kommando:

```zsh
.read setup/setup_tables.sql
```

Etter dette vil det eksistere en databasefil kalt teater.db. Den inneholder alle tabeller, men ingen data.

###  Hvordan sette inn data

1. Gitt at du er i sqlite3-shellet, kjør kommando::

```zsh
.read setup/insert_data.sql
```

Nå vil all dataen for teaterstykkene være satt inn i databasefilen, med unntak av setene i teatersalene. Dette gjøres av to Python-skript for enkelthets skyld.

2. Gå ut av sqlite3-shellet ved å kjøre kommando:

```zsh
.q
```

3. Kjør kommando:

```zsh
python3 setup/insert_seats_gamle_scene.py teater.db
```

4. Kjør kommando:

```zsh
python3 setup/insert_seats_hovedscenen.py teater.db
```

Nå vil databasefilen være helt komplett med tabeller og data for teaterstykkene i henhold til prosjektbeskrivelsen og informasjon på nettsiden til Trøndelag Teater.

**Det er nå klart for å interagere med databasen!**

## Interaksjon med databasen

Her er hvordan de ulike brukstilfellene er løst

### Brukstilfelle 1: Komplett oppsett av databasen

Brukstilfelle 1 ble løst i de foregående stegene der databasefilen ble satt opp med tabeller og data.

### Brukstilfelle 2: Lesing av fil med kjøpte seter

Følgende skript leser en fil med hvilke seter som er kjøpt til en forestilling med en gitt dato. Det opprettes et kjøp på adminbrukeren med navn *Admin*, telefonnummer *55555555* og adresse *Admingata 1*.

Her antas det at skriptet blir kjørt når det er ledige billetter på de gitte seten. Det vil si, vi antar at dette skriptet blir kjørt initielt i en forestilling av en administrator for å reservere seter eller lignende.

1. Kjør kommando for Gamle scene:

```zsh
python3 scan_seats.py seats_bought/gamle-scene.txt "Gamle scene"
```

2. Kjør kommando for Hovedscenen:

```zsh
python3 scan_seats.py seats_bought/hovedscenen.txt "Hovedscenen"
```

### Brukergrensesnitt brukstilfelle 3-7

For kjøre brukstilfellene 3-7 med et grensesnitt i terminalen, kjør kommando:

```zsh
python3 user_stories/brukstilfelle.py
```

Videre er det kommandoer for å kjøre brukstilfellene 3-7 direkte:

### Brukstilfelle 3: Kjøp av stoler til forestilling

For å kjøpe 9 stoler til forestilling "Størst av alt er kjærligheten", den 9. februar for seter med alle stoler på samme rad, kjør kommando:

```zsh
python3 user_stories/brukstilfelle_3.py
```

### Brukstilfelle 4: Oversikt over forestillinger og solgte stoler en gitt dato

For å skrive ut alle forestillinger og solgte stoler en gitt dato, kjør kommando:

```zsh
python3 user_stories/brukstilfelle_4.py
```

For default input trykk enter.

### Brukstilfelle 5: Hvilke skuespillere spiller på hvilke forestillinger

For å skrive ut alle forestillinger og skuespillere, kjør kommando:

```zsh
python3 user_stories/brukstilfelle_5.py
```

### Brukstilfelle 6: Hvilke forestillinger har solgt best

For å skrive ut hvor mange billetter hver forestilling har solgt sortert synkende, kjør kommando:

```zsh
python3 user_stories/brukstilfelle_6.py
```

### Brukstilfelle 7: Hvilke skuespillere har spilt i samme akt som en gitt skuespiller

For å skrive ut hvilke skuespillere som har spilt i samme akt som en gitt skuespiller, kjør kommando:

```zsh
python3 user_stories/brukstilfelle_7.py
```

For default input trykk enter.

## Forutsetninger eller andre merknader

**Roller i Kongsemnene:**

Guttorm Ingesson fantes ikke på nettsiden, så vi har ikke lagt inn denne i databasen.
Trønder stod ikke oppført i prosjektbeskrivelsen, men den fantes på nettsiden. Den er derfor satt til å spille i akt 1 siden vi antar det egentlig er rollen Guttorm Ingesson.

Baard Bratte var ikke satt opp på noen akter i tabellen i prosjektbeskrivelsen, så vi antar rollen spilles på akter 2, 3, 4 og 5. Vi har antatt dette fordi skuespilleren som spiller Baard Bratte spiller også Trønder, som vi har satt til å spille i akt 1.

Da vi ikke fant mailaddressen på skuespillerne, har vi satt mailaddressen til å være `NULL`.


## Endringer i ER Diagram - oppgradert

- Endret kardinalitet (0,n) fra (1, n) under Teatersal i diagrammet. Må kunne sette opp sal uten stykke.
- Lagt til SkrevetAv på Teaterstykke
- Endret fra ForGruppe til BillettPriser