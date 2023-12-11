"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """
    for i in range(number):
        yield "ABCD"[i % 4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    num = 1
    count = 0
    seat_letters = generate_seat_letters(number)
    for i in range(number):
        yield f"{num}{next(seat_letters)}"
        count += 1
        if count % 4 == 0:
            num += 1
            if num == 13:
                num += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passengers_dict = {}
    seat_numbers = generate_seats(len(passengers))
    for passenger in passengers:
        passengers_dict[passenger] = next(seat_numbers)

    return passengers_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    required_len = 12
    for num in seat_numbers:
        # ljust adds chars to end, rjust adds chars to the start
        yield f'{num}{flight_id}'.ljust(required_len, '0')
