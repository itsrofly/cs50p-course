import re
import sys
import inflect
from datetime import date

class Seasons:
    def __init__(self, date_):
        try:
            self.date_ = date.fromisoformat(date_)
        except:
            self.date_ = date_

    def __str__(self):
        p = inflect.engine()
        time = self.date_.days *  1440
        return p.number_to_words(time, andword="").capitalize()

    def __sub__(self, other):
        date_ = self.date_ - other.date_
        return Seasons(date_)


def main():
    birth = input("Date of Birth: ")
    time = get_time(birth)
    print(time, end=" minutes\n")


def get_time(birth):
    if re.search("^([0-9][0-9][0-9][0-9])-([0-0][1-9]|1[0-2])-([0-9][0-9])$", birth):
        birth = Seasons(birth)
        today = Seasons(date.today())
        return today - birth

    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()