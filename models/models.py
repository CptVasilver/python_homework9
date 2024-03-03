from selene import browser, be, have, command
import os
class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def assert_user_data(self, full_name, email, gender,
                         phone_number, birthday, subjects, hobbies,
                         picture, address, state_city):
        browser.all('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                birthday,
                subjects,
                hobbies,
                picture,
                address,
                state_city))

    def fill_second_name(self, second_name):
        browser.element('#lastName').should(be.blank).type(second_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def choose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value_containing(gender)).with_(click_by_js=True).click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').should(be.blank).type(phone_number)

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def fill_hobbies(self, hobbies):
        for hobbie in hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobbie)).click()

    def upload_picture(self, pic):
        browser.element('#uploadPicture').send_keys(os.path.abspath(pic))

    def fill_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    def fill_state(self, state):
        browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()

    def submit(self, value):
        browser.element(f'#{value}').click()

    def assert_filled_table(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
