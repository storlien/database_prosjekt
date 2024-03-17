import sys
import scan_seats
import api.hovedscenen as api

sliced_lines = []
no_rows_parkett = 18
no_rows_galleri = 4

def main():
    global sliced_lines
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Missing argument")
        print("Usage: python3 scan_seats_hovedscenen.py <file.txt>")
        return
    
    elif len(arguments) > 1:
        print("Too many arguments")
        print("Usage: python3 scan_seats_hovedscenen.py <file.txt>")
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
    
    year, month, day = scan_seats.get_date(sliced_lines)
    
    if (year, month, day) == (None, None, None):
        return
    
    sliced_lines = sliced_lines[1:]
    
    while (len(sliced_lines) > 0 and sliced_lines[0] != ""):
        find_section_and_reserve_seats()
    
def find_section_and_reserve_seats():
    global sliced_lines

    section_line = sliced_lines[0]
    sliced_lines = sliced_lines[1:]

    if "Galleri" in section_line:
        bought_seats = scan_seats.get_bought_seats(sliced_lines, no_rows_galleri)
        bought_seats_correct_seat_number = []

        for seat_tuple in bought_seats:
            new_seat_no = 504 + (seat_tuple[0] - 1) * 5 + seat_tuple[1]
            bought_seats_correct_seat_number.append((seat_tuple[0], new_seat_no))

        api.reserve_seats("teater.db", "Galleri", bought_seats_correct_seat_number)
        sliced_lines = sliced_lines[no_rows_galleri:]

    elif "Parkett" in section_line:
        bought_seats = scan_seats.get_bought_seats(sliced_lines, no_rows_parkett)
        bought_seats_correct_seat_number = []

        for seat_tuple in bought_seats:
            new_seat_no = seat_tuple[1] + (seat_tuple[0] - 1) * 28
            bought_seats_correct_seat_number.append((seat_tuple[0], new_seat_no))

        api.reserve_seats("teater.db", "Balkong", bought_seats_correct_seat_number)
        sliced_lines = sliced_lines[no_rows_parkett:]

    else:
        print("Unknown section", sliced_lines[0])
        return

if __name__ == "__main__":
    main()