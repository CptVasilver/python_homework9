from models.models import RegistrationPage


def test_filling_table():
    registration_page = RegistrationPage()
    registration_page.open()
    # filling form
    registration_page.fill_first_name('Yashaka')
    registration_page.fill_second_name('Selenium')
    registration_page.fill_email('Examplum@mulpmaxe.com')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('8005553535')
    registration_page.fill_date_of_birth('1900', 'Nov', '19')
    registration_page.fill_subjects('Math')
    registration_page.fill_hobbies(['Reading', 'Music'])
    registration_page.upload_picture('pic.png')
    registration_page.fill_address('Colorado-Springs')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Noida')
    registration_page.submit('submit')

    # check for successfully filled tab
    registration_page.assert_filled_table()

    # check for correct data
    registration_page.assert_user_data(
        'Yashaka Selenium',
        'Examplum@mulpmaxe.com',
        'Male',
        '8005553535',
        '19 November,1900',
        'Maths',
        'Reading, Music',
        'pic.png',
        'Colorado-Springs',
        'NCR Noida')
    registration_page.submit('closeLargeModal')
