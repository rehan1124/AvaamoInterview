from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from app_exceptions.UserDefinedExceptions import InvalidToppings, InvalidCrustSelected
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
    _topping_success_msg_css = "button[class='btn default_card_submit success']"
    _thin_crust_css = "img[alt='Thin Crust']"
    _thick_crust_css = "img[alt='Thick Crust']"
    _send_btn_xpath = "//button[text()='Send']"

    @Base.take_screenshot
    def open_chat_agent(self):
        self.driver.find_element(By.CSS_SELECTOR, self._chat_agent_btn_css).click()

    @Base.take_screenshot
    def validate_welcome_msg(self, message):
        retrieved_msg = self.driver.find_element(By.CSS_SELECTOR, self._welcome_msg_text).text
        print(f"Validate message `{retrieved_msg}` is displayed")
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
        print(f"Validate message `{retrieved_msg}` is displayed")
        return retrieved_msg == message

    @Base.take_screenshot
    def enter_first_name(self, firstname):
        print(f"Enter name `{firstname}`")
        self.driver.find_element(By.ID, self._first_name_id).send_keys(firstname)

    @Base.take_screenshot
    def enter_email(self, email):
        print(f"Enter email `{email}`")
        self.driver.find_element(By.ID, self._email_id).send_keys(email)

    @Base.take_screenshot
    def click_next_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self._next_btn).click()

    @Base.take_screenshot
    def validate_success_message_after_login(self, message):
        actual_msg = self.driver.find_element(By.CSS_SELECTOR, self._login_success_msg_css).text
        print(f"Validate success message `{message}` is displayed")
        return actual_msg == message

    @Base.take_screenshot
    def validate_welcome_img_presence(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._login_welcome_img_css).is_displayed()

    @Base.take_screenshot
    def enter_query(self, query):
        print(f"Enter query `{query}`")
        self.driver.find_element(By.ID, self._msg_query_id).send_keys(query)
        self.driver.find_element(By.ID, self._msg_query_id).send_keys(Keys.ENTER)

    @Base.take_screenshot
    def validate_last_agent_msg(self, message):
        actual_msg = self.driver.find_element(By.XPATH, self._latest_agent_msg_xpath).text
        print(f"Validate message `{message}` is displayed")
        return actual_msg == message

    @Base.take_screenshot
    def select_pizza_type(self, pizza_type):
        print(f"Select `{pizza_type}` pizza")
        self.driver.find_element(By.CSS_SELECTOR, f"[title='{pizza_type}']").click()

    @Base.take_screenshot
    def select_toppings(self, topping):
        print(f"Select `{topping}` topping")
        if topping == "bacon":
            self.driver.find_element(By.CSS_SELECTOR, self._bacon_topping_css).click()
        elif topping == "Pepperoni":
            self.driver.find_element(By.CSS_SELECTOR, self._pepperoni_topping_css).click()
        else:
            raise InvalidToppings("Invalid topping selected.")

    @Base.take_screenshot
    def submit_request(self):
        self.driver.find_element(By.XPATH, self._submit_btn_xpath).click()

    @Base.take_screenshot
    def topping_success_msg(self, expected_msg):
        actual_msg = self.driver.find_element(By.CSS_SELECTOR, self._topping_success_msg_css).text
        return actual_msg == expected_msg

    @Base.take_screenshot
    def choose_crust(self, crust_type):
        if crust_type == "Thin":
            self.driver.find_element(By.CSS_SELECTOR, self._thin_crust_css).click()
        elif crust_type == "Thick":
            self.driver.find_element(By.CSS_SELECTOR, self._thick_crust_css).click()
        else:
            raise InvalidCrustSelected("Please select `Thin` or `Thick`.")

    @Base.take_screenshot
    def click_send_button(self):
        self.driver.find_element(By.XPATH, self._send_btn_xpath).click()

    @Base.take_screenshot
    def validate_chat_msg(self, message):
        return self.driver.find_element(By.XPATH, f"//p[text()='{message}']").is_displayed()
