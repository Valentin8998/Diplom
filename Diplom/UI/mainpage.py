from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Класс для тестирования с главной страницы магазина"""
    BASE_URL = 'https://store.steampowered.com/'

    def __init__(self, driver):
        """Конструктор класса MainPage"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._navigate_to_store()

    def _navigate_to_store(self) -> None:
        """метод для перехода на страницу магазина"""
        self.driver.get(self.BASE_URL)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def search(self, game_name: str, game_app: str) -> None:
        """Поиск в магазине"""
        search = self.driver.find_element(
         By.XPATH, '//input[@placeholder="Поиск по магазину"]'
                )
        search.click()
        search.clear()
        search.send_keys(game_name)
        element = self.wait.until(
         EC.element_to_be_clickable(
          (By.CSS_SELECTOR, f'a[href*="{game_app}"]')
            )
                )
        self.driver.execute_script("arguments[0].click();", element)

    def adding(self) -> None:
        """Добавление игры в корзину"""
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='В корзину']/parent::a")
            )
        )
        button.click()

    def continue_shopping(self) -> None:
        """Нажатие кнопки 'продолжить покупки'"""
        next_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                    '.DialogButton._DialogLayout.Secondary.Focusable')
                    )
        )
        next_btn.click()

    def basket(self) -> None:
        """переход в корзину"""
        kor = self.wait.until(
            EC.element_to_be_clickable(
             (By.CSS_SELECTOR, ".DialogButton._DialogLayout.Primary.Focusable")
            )
        )
        kor.click()

    def assert_basket(self) -> None:
        """Открытие корзины и проверка суммы
        строго после добавление товаров в корзину"""

        kor = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 ".DialogButton._DialogLayout.Primary.Focusable")
                )
            )
        kor.click()

        def get_second_element_with_text(driver):
            elements = driver.find_elements(
                By.CSS_SELECTOR, '._2WLaY5TxjBGVyuWe_6KS3N'
            )
            if len(elements) >= 2 and elements[1].text != '':
                return elements[1]
            return False

        sumc = self.wait.until(get_second_element_with_text)

        print(f"Текст: '{sumc.text}'")

        # Сравниваем с ЛАТИНИЦЕЙ!
        assert sumc.text == "4098 руб"

    def asert_product(self) -> None:
        """проверка кол-ва товаров"""
        element = self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".bCGAC51za6R_thjPd7_vw"))
            )
        actual_text = element.text
        expected_text = "Ваша корзина (товаров: 1)"
        assert actual_text == expected_text
