from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewsCenter:
    """Класс для тестирования новостного центра Steam"""

    BASE_URL = 'https://store.steampowered.com/news/'

    def __init__(self, driver):
        """Конструктор класса NewsCenter"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Инициализация wait
        self._navigate_to_news()

    def _navigate_to_news(self):
        """метод для перехода на страницу новостей"""
        self.driver.get(self.BASE_URL)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".DialogInput"))
            )

    def game_news(self):
        """Тест поиска новостей по названию игры"""
        selector = (
            '.DialogInput.DialogInputPlaceholder.DialogTextInputBase.Focusable'
        )
        search = self.driver.find_element(By.CSS_SELECTOR, selector)
        search.click()
        search.send_keys('Path of Exile 2')
        fin = self.wait.until(
         EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), 'Path of Exile 2')]")
            )
        )
        fin.click()
