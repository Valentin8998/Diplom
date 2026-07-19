from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GamePage:
    """Класс для тестирования страницы игры в Steam"""

    BASE_URL = 'https://store.steampowered.com/app/1297900/Gothic_1_Remake/'

    def __init__(self, driver):
        """Конструктор класса GamePage"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._navigate_to_game()

    def _navigate_to_game(self):
        """метод для перехода на страницу игры"""
        self.driver.get(self.BASE_URL)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )

    def open_news(self):
        """Тест открытия новостей со страницы игры"""
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Показать все')]")
            )
        )
        element.click()
