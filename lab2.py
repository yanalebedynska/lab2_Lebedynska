#----------------------------DESCRIPTION----------------------------------------------------------------------------------------------
class Description:
    def __init__(self, name, surname, date_of_birth, email):
        self.name = str(name)
        self.surname = str(surname)
        self.date_of_birth = str(date_of_birth)
        self.email = str(email)
        print('\n\nSome descriptions was made successfully')

    def __str__(self):
        return 'Description class object'

    @staticmethod
    def about_description():
        print('\n\n--> In descriptions you can find some basic information about your object')
        print('--> Good luck in searching!')

    count_of_descriptions = 0

    def get_descriptions(self):
        print(f'Name: {self.name}')
        print(f'Surname: {self.surname}')
        print(f'Date of birth: {self.date_of_birth}')
        print(f'Email: {self.email}')
        Description.count_of_descriptions += 1
        return Description.count_of_descriptions

    @staticmethod
    def amount_of_all_people():
        print("\nTotal amount of people's descriptions: " + str(Description.count_of_descriptions))

# -----------------------------------------EMPLOYEE-------------------------------------------------------------------------------
class Employee(Description):
    count_of_employees = 0
    isGoodSpecialist = False

    def __init__(self, name, surname, date_of_birth, email, password, address, salary, experience):
        super().__init__(name, surname, date_of_birth, email)
        self._password = password
        self._address = address
        self.salary = salary
        self.experience = experience
        Employee.count_of_employees += 1
        Description.count_of_descriptions += 1


    def get_descriptions(self):
        print('\n ~ Information about employee ~')
        print(f'--- Name: {self.name}')
        print(f'--- Surname: {self.surname}')
        print(f'--- Date of birth: {self.date_of_birth}')
        print(f'--- Email: {self.email}')
        print(f'--- Password: {self._password}')
        print(f'--- Address: {self._address}')
        print(f'--- Salary: {self.salary}')
        print("\n--- Total amount of employees' descriptions: " + str(Employee.count_of_employees))



    def info_about_professionalism(self):
        if self.experience > 10:
            self.isGoodSpecialist = True
            print('\n --- This employee is master!')
        elif self.experience > 1:
            self.isGoodSpecialist = True
            print('\n--- This employee is good specialist!')
        else:
            self.isGoodSpecialist = False
            print('\n--- This employee is green in this field!')


    def info_about_premium(self, additional_hours):
        if self.salary > 15000:
            print('\n--- You did great! Get your bonus - one day off when you want')
        elif self.salary > 25000:
            print('\n--- You did great! Get your bonus - two days off when you want')
        else:
            print('\n--- Sorry, we have not any bonuses for you :(')

        if additional_hours > 6:
            print('--- Congratulations! You get additional premium - 200$')
        elif additional_hours > 15:
            print('--- Congratulations! You get additional premium - 350$')
        else:
            print('--- Sorry, you have no bonuses :(')
            print('Good luck next time!')

#---------------------------------USER----------------------------------------------------------------------------------------------
class User(Description):
    count_of_users = 0
    count_of_vip_users = 0

    def __init__(self, name, surname, date_of_birth, email, username, days_on_store, password, amount_of_orders):
        super().__init__(name, surname, date_of_birth, email)
        self.username = username
        self.days_on_store = days_on_store
        self._password = password
        self.amount_of_orders = amount_of_orders
        User.count_of_users += 1
        Description.count_of_descriptions += 1

    def get_descriptions(self):
        print('\n ~ Information about user ~')
        print(f'>>> Name: {self.name}')
        print(f'>>> Surname: {self.surname}')
        print(f'>>> Date of birth: {self.date_of_birth}')
        print(f'>>> Email: {self.email}')
        print(f'>>> Username: {self.username}')
        print(f'>>> Days On Store: {self.days_on_store}')
        print("\n>>> Total amount of users' descriptions: " + str(User.count_of_users))

    def info_about_discount(self):
        if self.days_on_store > 100:
            print('\n>>> Congratulations! You get a discount: -10%')
        elif self.days_on_store > 300:
            print('\n>>> Congratulations! You get a discount: -30%')
        elif self.days_on_store > 600:
            print('\n>>> Congratulations! You get a discount: -50%')
        else:
            print('\n>>> Sorry, you have no discounts!')

    def check_vip_status(self):
        if self.amount_of_orders > 20:
            User.count_of_vip_users += 1
            print(f'{self.username}, you are a VIP customer with {self.amount_of_orders} purchases!')
        else:
            orders_left = 20 - int(self.amount_of_orders)
            print(f'sorry {self.username}, you are not a VIP customer')
            print(f'You need to make {orders_left} more orders to become a VIP customer')


Description.about_description()

person1 = Employee('Yana', 'Bobby', '19-07-2006', 'lebedinska3@gmail.com', '453628', 'Lviv', 2500, 9)
person1.get_descriptions()
person1.info_about_premium(16)
person1.info_about_professionalism()


person2 = User('Olena', 'Marty', '23-10-2000', 'olenchik@gmail.com', 'olenka_lenka', 238, 'rt456g', 17)
person2.get_descriptions()
person2.info_about_discount()
person2.check_vip_status()

person3 = User('Max', 'Bottom', '01-01-2001', 'bottom32@gmail.com', 'bott_boot', 147, 'koferdon', 26)
person3.get_descriptions()
person3.info_about_discount()
person3.check_vip_status()

Description.amount_of_all_people()






