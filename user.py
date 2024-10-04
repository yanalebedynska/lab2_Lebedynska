from person import Person

class User(Person):
    all_users = []
    vip_users = []

    def __init__(self, name, surname, date_of_birth, email, username, days_on_store: int, password, amount_of_orders: int):
        super().__init__(name, surname, date_of_birth)
        self.email = email
        self.username = username
        self.days_on_store = days_on_store
        self._password = password
        self.amount_of_orders = amount_of_orders

        User.all_users.append(self)


    @property
    def days_on_store(self):
        return self._days_on_store

    @days_on_store.setter
    def days_on_store(self, value):
        if value < 0:
            print('Days cannot be negative!')
            print('Please enter a valid days: ')
            value = int(input())
            self._days_on_store = value
        else:
            self._days_on_store = value


    @property
    def amount_of_orders(self):
        return self._amount_of_orders

    @amount_of_orders.setter
    def amount_of_orders(self, value):
        if value < 0:
            print('Orders cannot be negative!')
            print('Please enter a valid orders: ')
            value = int(input())
            self._amount_of_orders = value

        else:
            self._amount_of_orders = value

    def get_person_descriptions(self):
        user_info = {
            'Name': self.name,
            'Surname': self.surname,
            'Username': self.username,
            'Date of Birth': self.date_of_birth,
            'Email': self.email,
            'Days On Store': self.days_on_store,
        }
        print('\n ~ Information about user ~')
        for key, value in user_info.items():
            print(f'>>> {key}: {value}')
        print("\n>>> Total amount of users' descriptions: " + str(len(User.all_users)))
        return user_info


    days_for_small_discount = 100
    days_for_medium_discount = 300
    days_for_big_discount = 600

    def info_about_discount(self):
        if self.days_on_store > User.days_for_small_discount:
            print('\n>>> Congratulations! You get a discount: -10%')

        elif self.days_on_store > User.days_for_medium_discount:
            print('\n>>> Congratulations! You get a discount: -30%')

        elif self.days_on_store > User.days_for_big_discount:
            print('\n>>> Congratulations! You get a discount: -50%')

        else:
            print('\n>>> Sorry, you have no discounts!')


    orders_to_be_VIP = 20

    def check_vip_status(self):
        if self.amount_of_orders > User.orders_to_be_VIP:
            User.vip_users.append(self)
            print(f'{self.username}, you are a VIP customer with {self.amount_of_orders} purchases!')
        else:
            orders_left = 20 - int(self.amount_of_orders)
            print(f'sorry {self.username}, you are not a VIP customer')
            print(f'You need to make {orders_left} more orders to become a VIP customer')
