import allure
import pytest


@pytest.mark.usefixtures("setup", "capture_screenshot")
class Base:
    def take_screenshot(func):
        def wrapper(self, *args, **kwargs):
            val = func(self, *args, **kwargs)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=func.__name__.replace("_", " ").capitalize(),
                attachment_type=allure.attachment_type.PNG)
            return val

        return wrapper
