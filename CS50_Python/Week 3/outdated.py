list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def checkFormat(input):

    if '/' in input:
        return 0
    else:
        return 1



def output(input, format):

    if format == 0:
        char = '-'
        month, day, year = input.split('/')
        month = int(month)
        day = int(day)
        year = int(year)

    else:
        month_str, day, year = input.split(' ')
        if not day.endswith(","):
            raise ValueError
        day = day.replace(",","")
        day = int(day)

        year = int(year)

        month = list.index(month_str) + 1

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError

    print(f"{year:04}-{month:02}-{day:02}")


def main():

    while True:
        try:
            str = input("Date: ").strip()
            format = checkFormat(str)
            output(str, format)
        except ValueError:
            pass
        else:
            break

main()
