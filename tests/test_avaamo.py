import allure
import pytest
from pytest_check import check
from selenium.common import NoSuchFrameException

from pages.base import Base
from pages.home import Home


class TestAvaamo(Base):
    @allure.story("Avaamo AI agent")
    @allure.title("Tests basic AI agent details input.")
    @allure.description(
        "This test attempts to log into the website, click on the AI agent button.\n\n"
        "Enter basic details.")
    @pytest.mark.smoke
    def test_login_screen(self):
        home_obj = Home(self.driver)
        home_obj.open_chat_agent()

        try:
            home_obj.validate_welcome_msg("Welcome to Pizza Shoppe")
            home_obj.click_get_started_btn()
        except NoSuchFrameException as e:
            print("No welcome message.")
        finally:
            home_obj.switch_to_agent_frame()

        with check:
            assert home_obj.validate_agent_screen_msg("Please enter your details to proceed")
        home_obj.enter_email("abc@gmail.com")
        home_obj.enter_first_name("Avaamo AI")
        home_obj.click_next_button()
        # assert False, "Failing the test intentionally."
