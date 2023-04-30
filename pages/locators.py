from selenium.webdriver.common.by import By


class TextBoxLocators:
    full_name_field = (By.CSS_SELECTOR, 'input#userName')
    email_field = (By.CSS_SELECTOR, 'input#userEmail')
    current_address_field = (By.CSS_SELECTOR, 'textarea#currentAddress')
    permanent_address_field = (By.CSS_SELECTOR, 'textarea#permanentAddress')
    submit_button = (By.CSS_SELECTOR, 'button#submit')
    results = (By.XPATH, '//div[@class="border col-md-12 col-sm-12"]//p')

