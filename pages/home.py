from selenium.webdriver import Keys
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
    _login_success_msg_css = "[id='messages-list'] [class='media-body'] p"
    _login_welcome_img_css = "[id='messages-list'] [class='media-body'] img"
    _msg_query_id = "queryTextbox"
    _latest_agent_msg_xpath = "(//*[@class='media-body']//*[contains(@class, 'desc text-content')])[last()]"
    _bacon_topping_css = "[value='bacon_id']"
    _pepperoni_topping_css = "[value='pepperoni_id']"
    _submit_btn_xpath = "//button[text()='Submit' and @class='btn default_card_submit']"

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

    @Base.take_screenshot
    def validate_success_message_after_login(self, message):
        actual_msg = self.driver.find_element(By.CSS_SELECTOR, self._login_success_msg_css).text
        print(actual_msg)
        return actual_msg == message

    @Base.take_screenshot
    def validate_welcome_img_presence(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_welcome_img_css).is_displayed()

    @Base.take_screenshot
    def enter_query(self, query):
        print(query)
        self.driver.find_element(By.ID, self._msg_query_id).send_keys(query)
        self.driver.find_element(By.ID, self._msg_query_id).send_keys(Keys.ENTER)

    @Base.take_screenshot
    def validate_last_agent_msg(self, message):
        actual_msg = self.driver.find_element(By.XPATH, self._latest_agent_msg_xpath).text
        print(actual_msg)
        return actual_msg == message

    @Base.take_screenshot
    def select_pizza_type(self, pizza_type):
        print(pizza_type)
        self.driver.find_element(By.CSS_SELECTOR, f"[title='{pizza_type}']").click()

    @Base.take_screenshot
    def select_toppings(self, topping):
        if topping == "bacon":
            self.driver.find_element(By.CSS_SELECTOR, self._bacon_topping_css).click()
        if topping == "Pepperoni":
            self.driver.find_element(By.CSS_SELECTOR, self._pepperoni_topping_css).click()

    @Base.take_screenshot
    def submit_request(self):
        self.driver.find_element(By.XPATH, self._submit_btn_xpath).click()
