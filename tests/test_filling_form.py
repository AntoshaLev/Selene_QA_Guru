import os
from selene import browser, have


def test_filling_form():
    browser.open('/')
    browser.element('#firstName').type('Anton')
    browser.element('#lastName').type('Levochkin')
    browser.element('#userEmail').type('www.Garu33@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9998347268')
    browser.element('#dateOfBirth').click()
    browser.element(".react-datepicker__month-select").click().element('option[value="6"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1995"]').click()
    browser.element(".react-datepicker__day--010").click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('file/1669713891808.jpg'))
    browser.element('#currentAddress').type('adress')
    browser.element("#state").click().element("#react-select-3-option-1").click()
    browser.element("#city").click().element("#react-select-4-option-0").click()
    browser.element("#submit").click()
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
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
    ))
