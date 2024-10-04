class Person:
    all_people = []

    def __init__(self, name, surname, date_of_birth):
        self.name = str(name)
        self.surname = str(surname)
        self.date_of_birth = str(date_of_birth)
        print('\n\nSome person was added successfully')

        Person.all_people.append(self)


    def __str__(self):
        return 'Person class object'

    @staticmethod
    def about_person():
        print('\n\n--> Here you can find some basic information about person')
        print('--> Good luck in searching!')


    def get_person_descriptions(self):
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Date of birth: {self.date_of_birth}')
        return len(Person.all_people)


    @staticmethod
    def amount_of_all_people_descriptions():
        print("\nTotal amount of people added: " + str(len(Person.all_people)))

