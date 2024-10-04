from person import Person
from employee import Employee

class Volunteer(Employee):
    all_volunteers = []

    def __init__(self, name: str, surname: str, date_of_birth: str, email: str, password: str, address: str, salary: int, experience: int, working_hours: list):
        Person.__init__(self, name, surname, date_of_birth)
        Employee.__init__(self, name, surname, date_of_birth, email, password, address, salary, experience)
        self._working_hours = working_hours
        Volunteer.all_volunteers.append(self)

    def __str__(self):
        return 'Volunteer class object'

    @property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, value):
        if not isinstance(value, list):
            print('Working hours must be a list')
        else:
            self._working_hours = value


    def volunteer_work_shift(self):
        start, end = self.working_hours[0], self._working_hours[1]
        print(f"Volunteer's work shift starts at {start} and ends at {end} ")


