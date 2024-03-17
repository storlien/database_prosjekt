import sys
from api.gamle_scene import reserve_seats

sliced_lines = []
no_rows_galleri = 3
no_rows_balkong = 4
no_rows_parkett = 10


def main():
    global sliced_lines
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Usage: python scan-seats-gamle-scene.py <file.txt>")
        return

    elif len(arguments) > 1:
        print("Too many arguments")
        print("Usage: python scan-seats-gamle-scene.py <file.txt>")
        return

    filename = arguments[0]

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line[: len(line) - 1]
                sliced_lines.append(line)

    except FileNotFoundError:
        print("File doesn't exist, check file name!")
        return
    except Exception as e:
        print("Error, something went wrong:", e)
        return

    year, month, day = get_date(sliced_lines)

    if (year, month, day) == (None, None, None):
        return

    sliced_lines = sliced_lines[1:]

    while len(sliced_lines) > 0 and sliced_lines[0] != "":
        find_section_and_reserve_seats()


def get_date(lines: list[str]):
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

        return year, month, day

    else:
        print("Date not found")
        return None, None, None


def find_section_and_reserve_seats():
    global sliced_lines

    section_line = sliced_lines[0]
    sliced_lines = sliced_lines[1:]

    if "Galleri" in section_line:
        bought_seats = get_bought_seats(no_rows_galleri)
        reserve_seats("Galleri", bought_seats)
        sliced_lines = sliced_lines[no_rows_galleri:]
    elif "Balkong" in section_line:
        bought_seats = get_bought_seats(no_rows_balkong)
        reserve_seats("Balkong", bought_seats)
        sliced_lines = sliced_lines[no_rows_balkong:]
    elif "Parkett" in section_line:
        bought_seats = get_bought_seats(no_rows_parkett)
        reserve_seats("Balkong", bought_seats)
        sliced_lines = sliced_lines[no_rows_parkett:]
    else:
        print("Unknown section", sliced_lines[0])
        return


def get_bought_seats(no_rows: int):

    list_of_bought_seats = []

    for index_row in range(no_rows):
        seats = list(sliced_lines[index_row])

        for index_seat in range(len(seats)):
            if int(seats[index_seat]) == 1:
                seat_tuple = (index_row + 1, index_seat + 1)
                list_of_bought_seats.append(seat_tuple)

    return list_of_bought_seats


if __name__ == "__main__":
    main()
