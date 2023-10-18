from selene import browser, be, have, by
from Lesson_10 import resourses


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def register(self, user):
        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').should(be.visible).type(user.last_name)
        browser.element('#userEmail').should(be.visible).type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').should(be.visible).type(user.phone_number)
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(str(user.birthdate.year))).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(user.birthdate.strftime('%B'))).click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(str(user.birthdate.day))).click()
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        if 'Sports' in user.hobby:
            browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
        if 'Music' in user.hobby:
            browser.element('label[for=hobbies-checkbox-3]').should(be.visible).click()
        browser.element('#uploadPicture').should(be.visible).type(resourses.path(user.picture))
        browser.element('#currentAddress').should(be.visible).type(user.current_address)
        browser.element("#react-select-3-input").should(be.visible).type(user.state).press_enter()
        browser.element("#react-select-4-input").should(be.visible).type(user.city).press_enter()
        browser.element("#submit").should(be.visible).click()



    def student_should_by_registred(self, user):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            user.birthdate.strftime("%d %B,%Y"),
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.state} {user.city}'
        ))
