import calendar
import datetime
from unittest import TestCase

from src.ordinal_date_util import get_date_of, ordinal, month


class GetSundayDateOffset(TestCase):
    first_sundays_2019 = [6, 3, 3, 7, 5, 2, 7, 4, 1, 6, 3, 1]
    second_sundays_2019 = [13, 10, 10, 14, 12, 9, 14, 11, 8, 13, 10, 8]
    third_sundays_2019 = [20, 17, 17, 21, 19, 16, 21, 18, 15, 20, 17, 15]
    fourth_sundays_2019 = [27, 24, 24, 28, 26, 23, 28, 25, 22, 27, 24, 22]
    fifth_sundays_2019 = [None, None, 31, None, None, 30, None, None, 29, None, None, 29]

    first_sundays_2020 = [5, 2, 1, 5, 3, 7, 5, 2, 6, 4, 1, 6]
    second_sundays_2020 = [12, 9, 8, 12, 10, 14, 12, 9, 13, 11, 8, 13]
    third_sundays_2020 = [19, 16, 15, 19, 17, 21, 19, 16, 20, 18, 15, 20]
    fourth_sundays_2020 = [26, 23, 22, 26, 24, 28, 26, 23, 27, 25, 22, 27]
    fifth_sundays_2020 = [None, None, 29, None, 31, None, None, 30, None, None, 29, None]

    first_sundays_2021 = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    second_sundays_2021 = [10, 14, 14, 11, 9, 13, 11, 8, 12, 10, 14, 12]
    third_sundays_2021 = [17, 21, 21, 18, 16, 20, 18, 15, 19, 17, 21, 19]
    fourth_sundays_2021 = [24, 28, 28, 25, 23, 27, 25, 22, 26, 24, 28, 26]
    fifth_sundays_2021 = [31, None, None, None, 30, None, None, 29, None, 31, None, None]

    first_sundays_2022 = [2, 6, 6, 3, 1, 5, 3, 7, 4, 2, 6, 4]
    second_sundays_2022 = [9, 13, 13, 10, 8, 12, 10, 14, 11, 9, 13, 11]
    third_sundays_2022 = [16, 20, 20, 17, 15, 19, 17, 21, 18, 16, 20, 18]
    fourth_sundays_2022 = [23, 27, 27, 24, 22, 26, 24, 28, 25, 23, 27, 25]
    fifth_sundays_2022 = [30, None, None, None, 29, None, 31, None, None, 30, None, None]

    def test_first_sundays_2019(self):
        for m in month:
            seed_date = datetime.date(year=2019, month=m, day=1)
            date_of_first_sun = get_date_of(ordinal=ordinal.FIRST, day=calendar.SUNDAY, date=seed_date)
            d2 = self.first_sundays_2019[m - 1]
            d1 = date_of_first_sun.day
            self.assertEqual(d1, d2)

    def test_second_sundays_2019(self):
        for m in month:
            seed_date = datetime.date(year=2019, month=m, day=1)
            date_of_second_sun = get_date_of(ordinal=ordinal.SECOND, day=calendar.SUNDAY, date=seed_date)
            d2 = self.second_sundays_2019[m - 1]
            d1 = date_of_second_sun.day
            self.assertEqual(d1, d2)

    def test_third_sundays_2019(self):
        for m in month:
            seed_date = datetime.date(year=2019, month=m, day=1)
            date_of_third_sun = get_date_of(ordinal=ordinal.THIRD, day=calendar.SUNDAY, date=seed_date)
            d2 = self.third_sundays_2019[m - 1]
            d1 = date_of_third_sun.day
            self.assertEqual(d1, d2)

    def test_fourth_sundays_2019(self):
        for m in month:
            seed_date = datetime.date(year=2019, month=m, day=1)
            date_of_fourth_sun = get_date_of(ordinal=ordinal.FOURTH, day=calendar.SUNDAY, date=seed_date)
            d2 = self.fourth_sundays_2019[m - 1]
            d1 = date_of_fourth_sun.day
            self.assertEqual(d1, d2)

    def test_fifth_sundays_2019(self):
        for m in month:
            seed_date = datetime.date(year=2019, month=m, day=1)
            d2 = get_date_of(ordinal=ordinal.FIFTH, day=calendar.SUNDAY, date=seed_date)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_sundays_2019[m - 1], d2)

    def test_first_sundays_2020(self):
        for m in month:
            seed_date = datetime.date(year=2020, month=m, day=1)
            date_of_first_sun = get_date_of(ordinal=ordinal.FIRST, day=calendar.SUNDAY, date=seed_date)
            d2 = self.first_sundays_2020[m - 1]
            d1 = date_of_first_sun.day
            self.assertEqual(d1, d2)

    def test_second_sundays_2020(self):
        for m in month:
            seed_date = datetime.date(year=2020, month=m, day=1)
            date_of_second_sun = get_date_of(ordinal=ordinal.SECOND, day=calendar.SUNDAY, date=seed_date)
            d2 = self.second_sundays_2020[m - 1]
            d1 = date_of_second_sun.day
            self.assertEqual(d1, d2)

    def test_third_sundays_2020(self):
        for m in month:
            seed_date = datetime.date(year=2020, month=m, day=1)
            date_of_third_sun = get_date_of(ordinal=ordinal.THIRD, day=calendar.SUNDAY, date=seed_date)
            d2 = self.third_sundays_2020[m - 1]
            d1 = date_of_third_sun.day
            self.assertEqual(d1, d2)

    def test_fourth_sundays_2020(self):
        for m in month:
            seed_date = datetime.date(year=2020, month=m, day=1)
            date_of_fourth_sun = get_date_of(ordinal=ordinal.FOURTH, day=calendar.SUNDAY, date=seed_date)
            d2 = self.fourth_sundays_2020[m - 1]
            d1 = date_of_fourth_sun.day
            self.assertEqual(d1, d2)

    def test_fifth_sundays_2020(self):
        for m in month:
            seed_date = datetime.date(year=2020, month=m, day=1)
            d2 = get_date_of(ordinal=ordinal.FIFTH, day=calendar.SUNDAY, date=seed_date)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_sundays_2020[m - 1], d2)

    def test_first_sundays_2021(self):
        for m in month:
            seed_date = datetime.date(year=2021, month=m, day=1)
            date_of_first_sun = get_date_of(ordinal=ordinal.FIRST, day=calendar.SUNDAY, date=seed_date)
            d2 = self.first_sundays_2021[m - 1]
            d1 = date_of_first_sun.day
            self.assertEqual(d1, d2)

    def test_second_sundays_2021(self):
        for m in month:
            seed_date = datetime.date(year=2021, month=m, day=1)
            date_of_second_sun = get_date_of(ordinal=ordinal.SECOND, day=calendar.SUNDAY, date=seed_date)
            d2 = self.second_sundays_2021[m - 1]
            d1 = date_of_second_sun.day
            self.assertEqual(d1, d2)

    def test_third_sundays_2021(self):
        for m in month:
            seed_date = datetime.date(year=2021, month=m, day=1)
            date_of_third_sun = get_date_of(ordinal=ordinal.THIRD, day=calendar.SUNDAY, date=seed_date)
            d2 = self.third_sundays_2021[m - 1]
            d1 = date_of_third_sun.day
            self.assertEqual(d1, d2)

    def test_fourth_sundays_2021(self):
        for m in month:
            seed_date = datetime.date(year=2021, month=m, day=1)
            date_of_fourth_sun = get_date_of(ordinal=ordinal.FOURTH, day=calendar.SUNDAY, date=seed_date)
            d2 = self.fourth_sundays_2021[m - 1]
            d1 = date_of_fourth_sun.day
            self.assertEqual(d1, d2)

    def test_fifth_sundays_2021(self):
        for m in month:
            seed_date = datetime.date(year=2021, month=m, day=1)
            d2 = get_date_of(ordinal=ordinal.FIFTH, day=calendar.SUNDAY, date=seed_date)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_sundays_2021[m - 1], d2)

    def test_first_sundays_2022(self):
        for m in month:
            seed_date = datetime.date(year=2022, month=m, day=1)
            date_of_first_sun = get_date_of(ordinal=ordinal.FIRST, day=calendar.SUNDAY, date=seed_date)
            d2 = self.first_sundays_2022[m - 1]
            d1 = date_of_first_sun.day
            self.assertEqual(d1, d2)

    def test_second_sundays_2022(self):
        for m in month:
            seed_date = datetime.date(year=2022, month=m, day=1)
            date_of_second_sun = get_date_of(ordinal=ordinal.SECOND, day=calendar.SUNDAY, date=seed_date)
            d2 = self.second_sundays_2022[m - 1]
            d1 = date_of_second_sun.day
            self.assertEqual(d1, d2)

    def test_third_sundays_2022(self):
        for m in month:
            seed_date = datetime.date(year=2022, month=m, day=1)
            date_of_third_sun = get_date_of(ordinal=ordinal.THIRD, day=calendar.SUNDAY, date=seed_date)
            d2 = self.third_sundays_2022[m - 1]
            d1 = date_of_third_sun.day
            self.assertEqual(d1, d2)

    def test_fourth_sundays_2022(self):
        for m in month:
            seed_date = datetime.date(year=2022, month=m, day=1)
            date_of_fourth_sun = get_date_of(ordinal=ordinal.FOURTH, day=calendar.SUNDAY, date=seed_date)
            d2 = self.fourth_sundays_2022[m - 1]
            d1 = date_of_fourth_sun.day
            self.assertEqual(d1, d2)

    def test_fifth_sundays_2022(self):
        for m in month:
            seed_date = datetime.date(year=2022, month=m, day=1)
            d2 = self.fifth_sundays_2022[m - 1]
            d1 = get_date_of(ordinal=ordinal.FIFTH, day=calendar.SUNDAY, date=seed_date)
            if d1:
                d1 = d1.day
            self.assertEqual(d1, d2)
