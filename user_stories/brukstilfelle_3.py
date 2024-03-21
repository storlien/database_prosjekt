from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config
from api.validator import Validator
from api.ticketmaster import TicketMaster
from api.kjopcalculator import PriceCalculator

TEATERSTYKKE_CHOICES = [config.TEATERSTYKKE_STORST_AV_ALT, config.TEATERSTYKKE_KONGSENMNENE]
KUNDEGRUPPE_CHOICES = [
    config.ORDNIAER,
    config.BARN,
    config.STUDENT,
    config.GRUPPE_10,
    config.GRUPPE_HONNOR,
    config.HONNOR,
]
SECTION_CHOICES = [
    config.SECTION_GAMLE_SCENE_PARKETT,
    config.SECTION_GAMLE_SCENE_BALKONG,
    config.SECTION_GAMLE_SCENE_GALLERI,
]


def main():
    tm = TicketMaster()
    v = Validator()
    pc = PriceCalculator()

    default_play_name = TEATERSTYKKE_CHOICES[0]
    play_name = input(f"Skriv inn stykkets navn (standard: {default_play_name}): ") or default_play_name
    if v.validate_play_name(play_name):
        pass
    else:
        print("Ugyldig stykkenavn. Vennligst skriv inn et gyldig stykkenavn.")
        return

    default_date = "2024-02-03"
    date = input(f"Skriv inn datoen (ÅÅÅÅ-MM-DD, standard: {default_date}): ") or default_date
    try:
        _ = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Ugyldig datoformat. Vennligst bruk ÅÅÅÅ-MM-DD.")
        return

    default_section = SECTION_CHOICES[0]
    section = input(f"Skriv inn seksjonsnavnet (standard: {default_section}): ") or default_section

    hall = tm.get_hall_by_play(play_name)

    if v.validate_section(hall, section):
        pass
    else:
        print("Ugyldig seksjonsnavn. Vennligst skriv inn et gyldig seksjonsnavn.")
        return

    default_number_of_tickets = 1
    number_of_tickets = (
        input(f"Skriv inn antall billetter (standard: {default_number_of_tickets}): ") or default_number_of_tickets
    )
    try:
        number_of_tickets = int(number_of_tickets)
    except ValueError:
        print("Ugyldig antall billetter. Vennligst skriv inn et gyldig antall billetter.")
        return

    phone_number = input(f"Skriv inn ditt telefonnummer (8 siffer): ")
    if len(phone_number) != 8 or not phone_number.isdigit():
        print("Ugyldig telefonnummer. Vennligst skriv inn et gyldig telefonnummer.")
        return

    name, address = tm.check_customer_exists(phone_number)
    if not name or not address:
        print("Brukeren eksisterer ikke. Vennligst registrer navn og addresse.")
        customer_name = input("Skriv inn kundens navn: ")
        customer_address = input("Skriv inn kundens adresse: ")
    else:
        customer_name = name
        customer_address = address
        print(f"Fant bruker på med navn '{name}', på adresse: '{address}' med telefonnummer '{phone_number}'")

    customer_groups = []
    for i in range(number_of_tickets):
        default_customer_group = KUNDEGRUPPE_CHOICES[0]
        customer_group = (
            input(f"Skriv inn kundegruppen for billett {i+1} (standard: {default_customer_group}): ")
            or default_customer_group
        )
        if customer_group in KUNDEGRUPPE_CHOICES:
            customer_groups.append(customer_group)
        else:
            print("Ugyldig kundegruppe. Vennligst skriv inn en gyldig kundegruppe.")
            return

    result, kjop_id = tm.purchase_tickets(
        play_name, date, section, number_of_tickets, phone_number, customer_name, customer_address, customer_groups
    )
    print(result + "\n")
    if kjop_id is None:
        print("Kjøpet ble ikke fullført. Ugyldig kjøpId")
        return
    price = pc.calculate_total_price(kjop_id)
    print("Den totalen prisen for kjøpet er: " + str(price) + " kr.")


if __name__ == "__main__":
    main()
