from api.ticketmaster import TicketMaster
from api.validator import Validator
import sys, config

sliced_lines = []
seats_to_reserve = []

hall = ""
play = ""
play_id = 0
act_no = 0
date = ""


def main():
    global sliced_lines
    global hall
    global play
    global play_id
    global date
    global act_no

    arguments = sys.argv[1:]

    if len(arguments) < 2:
        print("Missing argument")
        print("Usage: python3 scan_seats.py <file.txt> <hall name> <optional database.db>")
        return

    elif len(arguments) == 2:
        print(f"Missing argument, using default '{config.DEFAULT_DB}'")
    
    elif len(arguments) > 3:
        print("Too many arguments")
        print("Usage: python3 scan_seats.py <file.txt> <hall name> <optional database.db>")
        return
    
    filename = arguments[0]

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line[:len(line)-1]
                sliced_lines.append(line)

    except FileNotFoundError:
        print("File doesn't exist, check file name!")
        return
    except Exception:
        print("Error, something went wrong:", Exception)
        return
    
    date = get_date(sliced_lines)
    
    if date == None:
        return
    
    db = config.DEFAULT_DB if len(arguments) == 2 else arguments[2]

    vd = Validator(db)
    tm = TicketMaster(db)

    hall = arguments[1]

    if not vd.validate_hall(hall):
        print("No such hall found in the database!")
        return

    plays = tm.which_play(hall, date, config.DEFAULT_SEASON_ID)

    if plays is not None:
        play = plays[0]
    else:
        print("No play found with that name and date in season", config.DEFAULT_SEASON_ID)
        return
    
    play_id, act_no = tm.get_play_id_and_act_no(play, date)
    kjop_id = tm.admin_create_billett_kjop()

    sliced_lines = sliced_lines[1:]
    
    while (len(sliced_lines) > 0 and sliced_lines[0] != ""):
        seats_to_reserve.extend(find_section_and_seats(tm))

    tm.reserve_seat_list(kjop_id, seats_to_reserve)

    print("Successfully reserved seats for", play, "on", date, "in", hall)


def get_date(lines):
    if "Dato" in lines[0]:
        words = lines[0].split()

        if len(words) != 2:
            print("Wrong format on date. Correct format is YYYY-MM-DD")
            return None, None, None

        date = words[1].split("-")

        if len(date) != 3:
            print("Wrong format on date. Correct format is YYYY-MM-DD")
            return None, None, None

        year = date[0]
        month = date[1].lstrip("0")
        day = date[2].lstrip("0")

        if len(year) != 4 or len(month) > 2 or len(day) > 2:
            print("Wrong format on date. Correct format is YYYY-MM-DD")
            return None, None, None

        if len(str(month)) == 1:
            month = "0" + str(month)
        
        if len(str(day)) == 1:
            day = "0" + str(day)

        return year + "-" + month + "-" + day
    
    else:
        print("Date not found")
        return None, None, None


def find_section_and_seats(tm: TicketMaster):
    global sliced_lines

    section_line = sliced_lines[0]
    sliced_lines = sliced_lines[1:]

    if hall == config.HALL_GAMLE_SCENE:

        if config.SECTION_GAMLE_SCENE_GALLERI in section_line:

            tuple_list = get_seats_to_reserve(sliced_lines, config.NO_ROWS_GALLERI_GAMLE_SCENE, config.GAMLE_SCENE_GALLERI_SECTION_ID)
            sliced_lines = sliced_lines[config.NO_ROWS_GALLERI_GAMLE_SCENE:]
            return tuple_list

        elif config.SECTION_GAMLE_SCENE_BALKONG in section_line:

            tuple_list = get_seats_to_reserve(sliced_lines, config.NO_ROWS_BALKONG_GAMLE_SCENE, config.GAMLE_SCENE_BALKONG_SECTION_ID)
            sliced_lines = sliced_lines[config.NO_ROWS_BALKONG_GAMLE_SCENE:]
            return tuple_list

        elif config.SECTION_GAMLE_SCENE_PARKETT in section_line:

            tuple_list = get_seats_to_reserve(sliced_lines, config.NO_ROWS_PARKETT_GAMLE_SCENE, config.GAMLE_SCENE_PARKETT_SECTION_ID)
            sliced_lines = sliced_lines[config.NO_ROWS_PARKETT_GAMLE_SCENE:]
            return tuple_list

    elif hall == config.HALL_HOVEDSCENEN:
        # TODO
        return (0,0,0,0)


def get_seats_to_reserve(sliced_lines, no_rows, section_id):

    tuple_list = []

    for index_row in range(no_rows):
        seats = list(sliced_lines[index_row])
        
        for index_seat in range(len(seats)):

            if seats[index_seat].lower() == "x":
                continue

            if int(seats[index_seat]) == 1:
                seat_tuple = (play_id, act_no, config.DEFAULT_CUSTOMER_GROUP, section_id, no_rows - index_row, index_seat + 1)
                tuple_list.append(seat_tuple)
    
    return tuple_list


if __name__ == "__main__":
    main()