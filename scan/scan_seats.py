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

        return year, month, day
    
    else:
        print("Date not found")
        return None, None, None

def get_bought_seats(sliced_lines, no_rows):

    list_of_bought_seats = []

    for index_row in range(no_rows):
        seats = list(sliced_lines[index_row])
        
        for index_seat in range(len(seats)):

            if seats[index_seat].lower() == "x":
                continue

            if int(seats[index_seat]) == 1:
                seat_tuple = (no_rows - index_row, index_seat + 1)
                list_of_bought_seats.append(seat_tuple)
    
    return list_of_bought_seats