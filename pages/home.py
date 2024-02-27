from selenium.webdriver.common.by import By

from pages.base import Base


class Home:
    def __init__(self, driver):
        self.driver = driver

    # --- Locators ---
    _chat_agent_btn_css = "[alt='Chat agent button']"
    _chat_agent_details_msg = "[class*='registered-no-details']"
    _first_name_id = "first_name"
    _email_id = "email"
    _next_btn = "[type='submit']"
    _welcome_msg_text = "[class='welcome-message']"
    _get_started_btn_css = "[class='get-started-link']"
    _agent_iframe_name = "avaamoIframe"

    @Base.take_screenshot
    def open_chat_agent(self):
        self.driver.find_element(By.CSS_SELECTOR, self._chat_agent_btn_css).click()

    @Base.take_screenshot
    def validate_welcome_msg(self, message):
        retrieved_msg = self.driver.find_element(By.CSS_SELECTOR, self._welcome_msg_text).text
        print(retrieved_msg)
        return retrieved_msg == message

    @Base.take_screenshot
    def switch_to_agent_frame(self):
        self.driver.switch_to.frame(self._agent_iframe_name)

    @Base.take_screenshot
    def click_get_started_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self._get_started_btn_css).click()

    @Base.take_screenshot
    def validate_agent_screen_msg(self, message):
        retrieved_msg = self.driver.find_element(By.CSS_SELECTOR, self._chat_agent_details_msg).text
        return retrieved_msg == message

    @Base.take_screenshot
    def enter_first_name(self, firstname):
        self.driver.find_element(By.ID, self._first_name_id).send_keys(firstname)

    @Base.take_screenshot
    def enter_email(self, email):
        self.driver.find_element(By.ID, self._email_id).send_keys(email)

    @Base.take_screenshot
    def click_next_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self._next_btn).click()
