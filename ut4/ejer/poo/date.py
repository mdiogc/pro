from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        if 1900 <= year <= 2050:
            self.year = year
        else:
            self.year = 1900
        if 1 <= month <= 12:
            self.month = month
        else:
            self.month = 1
        if 1 <= day <= self.days_in_month(self.month, self.year):
            self.day = day
        else:
            self.day = 1

    @staticmethod
    def is_leap_year(year: int) -> bool:
        if year % 400 == 0:
                return True
        if year % 100 != 0 and year % 4 == 0:
                return True
        return False

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == 2:
            if Date.is_leap_year(year):
                return 29
            else:
                return 28
        if month in {4, 6, 9, 11}:
            return 30
        return 31
            

    def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        total_days = sum(Date.days_in_month(m, self.year) for m in range(1, self.month))
        total_days += self.day

        total_days += sum(366 if Date.is_leap_year(y) else 365 for y in range(1900, self.year))

        if self.month > 2 and Date.is_leap_year(self.year):
            total_days += 1
        return total_days

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        days_since_monday = (self.get_delta_days() + 1) % 7
        return days_since_monday

    @property
    def is_weekend(self) -> bool:
        return self.weekday in {0, 6}


    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        return f"{self.day:02}/{self.month:02}/{self.year}"


    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        WEEKDAY_NAME = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO']
        MONTH_NAME = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
        weekday_name = WEEKDAY_NAME[self.weekday]
        month_name = MONTH_NAME[self.month - 1]
        return f"{weekday_name} {self.day} DE {month_name} DE {self.year}"
   
    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        total_days = self.get_delta_days() + days
        return Date.get_delta_days(total_days)

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        if isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()
        if isinstance(other, int):
            new_delta_days = self.get_delta_days() - other
            return Date.get_delta_days_delta_days(new_delta_days)


    def __lt__(self, other: Date) -> bool:
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day


    def __gt__(self, other) -> bool:
        if not isinstance(other, Date):
            return False
        return self.get_delta_days() > other.get_delta_days()

    def __eq__(self, other) -> bool:
          if not isinstance(other, Date):
            return False
          else:
            return self.day == other.day and self.month == other.month and self.year == other.year
