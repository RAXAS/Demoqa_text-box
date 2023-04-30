from generator.generator import generated_person
from pages.locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def fill_fields_and_submit(self):
        person = generated_person()
        self.element_is_visible(TextBoxLocators.full_name_field).send_keys(person.full_name)
        self.element_is_visible(TextBoxLocators.email_field).send_keys(person.email)
        self.element_is_visible(TextBoxLocators.current_address_field).send_keys(person.current_address)
        self.element_is_visible(TextBoxLocators.permanent_address_field).send_keys(person.permanent_address)
        self.element_is_visible(TextBoxLocators.submit_button).click()
        return person

    def text_box_result(self):
        result_list = self.elements_are_visible(TextBoxLocators.results)
        text_box_result = [i.text for i in result_list]
        return text_box_result