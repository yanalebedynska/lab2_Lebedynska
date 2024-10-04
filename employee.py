from person import Person

class Employee(Person):
    all_employees = []
    isGoodSpecialist = False

    def __init__(self, name, surname, date_of_birth, email, password, address, salary: int, experience: int):
        super().__init__(name, surname, date_of_birth)
        self.email = email
        self._password = password
        self._address = address
        self.salary = salary
        self.experience = experience

        Employee.all_employees.append(self)


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print('Salary cannot be negative!')
            print('Please enter a valid salary: ')
            value = int(input())
            self._salary = value
        else:
            self._salary = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            print('Experience cannot be negative!')
            print('Please enter a valid experience: ')
            value = int(input())
            self._experience = value
        else:
            self._experience = value


    def get_person_descriptions(self):
        print('\n ~ Information about employee ~')
        print(f'--- Name: {self.name}')
        print(f'--- Surname: {self.surname}')
        print(f'--- Date of birth: {self.date_of_birth}')
        print(f'--- Email: {self.email}')
        print(f'--- Password: {self._password}')
        print(f'--- Address: {self._address}')
        print(f'--- Salary: {self.salary}')
        print(f'--- Experience: {self.experience}')
        print("\n--- Total amount of employees' descriptions: " + str(len(Employee.all_employees)))


    goodSpecialistExperience = 1
    masterExperience = 10

    def info_about_professionalism(self):
        if self.experience > Employee.masterExperience:
            self.isGoodSpecialist = True
            print('\n --- This employee is master!')

        elif self.experience > Employee.goodSpecialistExperience:
            self.isGoodSpecialist = True
            print('\n--- This employee is good specialist!')

        else:
            self.isGoodSpecialist = False
            print('\n--- This employee is green in this field!')


    salary_for_little_bonus = 15000
    salary_for_big_bonus = 25000
    hours_for_small_premium = 6
    hours_for_big_premium = 15

    def info_about_premium(self, additional_hours):
        if self.salary > Employee.salary_for_little_bonus:
            print('\n--- You did great! Get your bonus - one day off when you want')

        elif self.salary > Employee.salary_for_big_bonus:
            print('\n--- You did great! Get your bonus - three days off when you want')

        else:
            print('\n--- Sorry, we have not any bonuses for you :(')

        if additional_hours > Employee.hours_for_small_premium:
            print('--- Congratulations! You get additional premium - 200$')
        elif additional_hours > Employee.hours_for_big_premium:
            print('--- Congratulations! You get additional premium - 350$')
        else:
            print('--- Sorry, you have no bonuses :(')
            print('Good luck next time!')
