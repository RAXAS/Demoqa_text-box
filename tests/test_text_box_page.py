from pages.text_box_page import TextBoxPage


class TestTextBoxPage:

    def test_text_box_page(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        person = text_box_page.fill_fields_and_submit()
        result = text_box_page.text_box_result()
        assert result[0][5:] == person.full_name, 'The "name" field was not filled'
        assert result[1][6:] == person.email, 'The "email" field was not filled'
        assert result[2][17:] == person.current_address.replace("\n", " "), 'The "current address" field was not filled'
        assert result[3][20:] == person.permanent_address.replace("\n", " "), 'The "permanent address" field was not ' \
                                                                              'filled '

