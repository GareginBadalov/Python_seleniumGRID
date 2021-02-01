import allure
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType


class Locators:
    locator_email = (By.CLASS_NAME, 'Textinput-Control')
    locator_passw = (By.ID, 'passp-field-passwd')
    locator_search_field = (By.CLASS_NAME, 'textinput__control')
    locator_count_m = (By.XPATH, "//span[@class='mail-MessagesSearchInfo-Title_misc nb-with-xs-left-gap']")
    locator_message = (By.CLASS_NAME, "mail-MessageSnippet-Item")
    locator_answer = (By.CLASS_NAME, 'mail-Toolbar-Item_reply')
    locator_topic_area = (By.XPATH, "//input[@class='composeTextField ComposeSubject-TextField']")
    locator_text_field = (By.XPATH, "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr']/div[1]")
    locator_send_button = (By.XPATH, "//button[@class='control button2 button2_view_default button2_tone_default button2_size_l button2_theme_action button2_pin_circle-circle ComposeControlPanelButton-Button ComposeControlPanelButton-Button_action']")


class MailChecker(BasePage):

    @allure.feature('Authorization')
    @allure.story('Enter email and password')
    def auth(self, login, password):
        email = self.find_element(Locators.locator_email)
        email.send_keys(login)
        email.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        passw = self.find_element(Locators.locator_passw)
        self.driver.implicitly_wait(10)
        passw.send_keys(password)
        return passw.send_keys(Keys.ENTER)

    @allure.feature('Find count of messages')
    @allure.story('Enter search request and find count of messages ')
    @allure.severity('normal')
    def find_messages(self, from_who):
        search_field = self.find_element(Locators.locator_search_field)
        search_field.send_keys(from_who)
        search_field.send_keys(Keys.ENTER)
        with allure.step('screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='SearchResult', attachment_type=AttachmentType.PNG)
        self.driver.implicitly_wait(10)
        count_m = self.find_element(Locators.locator_count_m)
        count_m = count_m.text
        return count_m

    @allure.feature('Reply to')
    @allure.story('Enter text, topic and answer')
    @allure.severity('critical')
    def answer(self, topic_text, message_text):
        message = self.find_element(Locators.locator_message)
        message.click()
        self.driver.implicitly_wait(10)
        answer = self.find_element(Locators.locator_answer)
        answer.click()
        self.driver.implicitly_wait(10)
        topic_area = self.find_element(Locators.locator_topic_area)
        topic_area.click()
        topic_area.clear()
        topic_area.send_keys(topic_text)
        text_field = self.find_element(Locators.locator_text_field)
        text_field.click()
        text_field.send_keys(message_text)
        with allure.step('screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='message_text_topic',
                          attachment_type=AttachmentType.PNG)
        return self.find_element(Locators.locator_send_button).click()
