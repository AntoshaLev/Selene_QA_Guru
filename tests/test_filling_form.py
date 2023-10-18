from datetime import date
from Lesson_10.pages.registration_page import RegistrationPage
from Lesson_10.data.users import User

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    student = User(first_name='Anton', last_name='Levochkin', email='www.Garu33@mail.ru', gender='Male',
                   phone_number='9998347268', birthdate=date(1995, 7, 10),
                   subject='Computer Science', hobby='Sports, Music', picture='1669713891808.jpg',
                   current_address='adress', state='Uttar Pradesh', city='Agra')
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.student_should_by_registred(student)
