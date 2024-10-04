from person import Person
from employee import Employee
from user import User
from volunteer import Volunteer

Person.about_person()

person1 = Employee('Yana', 'Bobby', '19-07-2006', 'lebedinska3@gmail.com', '453628', 'Lviv', 2500, 9)
person1.get_person_descriptions()
person1.info_about_premium(16)
person1.info_about_professionalism()


person2 = User('Olena', 'Marty', '23-10-2000', 'olenchik@gmail.com', 'olenka_lenka', 238, 'rt456g', 17)
person2.get_person_descriptions()
person2.info_about_discount()
person2.check_vip_status()

person3 = User('Max', 'Bottom', '01-01-2001', 'bottom32@gmail.com', 'bott_boot', 147, 'koferdo', 26)
person3.get_person_descriptions()
person3.info_about_discount()
person3.check_vip_status()

Person.amount_of_all_people_descriptions()


person4 = Volunteer('Oksana', 'Pally', '1976-03-23', 'lebedinska2@gmail.com', '213087', 'Lviv', 30000, 9, ['09:00', '17:00'])
person4.volunteer_work_shift()
print(person4)

