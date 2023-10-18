from Lesson_10.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form():
    # GIVEN
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Anton')
    registration_page.fill_last_name('Levochkin')
    registration_page.fill_email('www.Garu33@mail.ru')
    registration_page.choose_a_gender()
    registration_page.fill_phone_number('9998347268')
    registration_page.choose_date_of_birth(month='7', year='96', day='010')
    registration_page.choose_a_subject('Computer Science')
    registration_page.choose_a_hobby()
    registration_page.upload_a_picture('1669713891808.jpg')
    registration_page.type_current_address('adress')
    registration_page.choose_state('Uttar Pradesh')
    registration_page.choose_city('Agra')
    registration_page.submit_form()

    # THEN
    registration_page.student_should_by_registred(
        'Anton Levochkin',
        'www.Garu33@mail.ru',
        'Male',
        '9998347268',
        '10 July,1995',
        'Computer Science',
        'Sports, Music',
        '1669713891808.jpg',
        'adress',
        'Uttar Pradesh Agra'
    )
