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

    def _navigate_to_store(self):
        """метод для перехода на страницу магазина"""
        self.driver.get(self.BASE_URL)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def adding_to_cart(self):
        """Тест добавления товара в корзину и проверки количества"""
        GAME_CARD_SELECTOR = (
            ".carousel_items.store_capsule_container a[href*='/app/' ]"
        )
        games = self.wait.until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR, GAME_CARD_SELECTOR))
        )
        if games:
            games[0].click()  # первая игра
        else:
            print("Игры не найдены")

        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='В корзину']/parent::a")
            )
        )
        button.click()

        # нажатие кнопки "открыть корзину"
        self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, (
                        ".DialogButton._DialogLayout.Primary.Focusable"))
                )
            ).click()
        element = self.wait.until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ".bCGAC51za6R_thjPd7_vw"))
            )
        actual_text = element.text
        expected_text = "Ваша корзина (товаров: 1)"
        assert actual_text == expected_text

    def clear_basket(self):
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(text(), 'Удалить')]")
            )
        )
        element.click()
        self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Ваша корзина пуста')]"))
            )

    def search_by_name(self):
        """Тест поиска товара по названию"""
        search = self.driver.find_element(
            By.XPATH, '//input[@placeholder="Поиск по магазину"]'
        )
        search.click()
        search.send_keys("Baldur's Gate 3")

    def total_cost(self):
        """Тест расчета общей стоимости корзины"""
        # Поиск и добавление первой игры
        search = self.driver.find_element(
            By.XPATH, '//input[@placeholder="Поиск по магазину"]'
        )
        search.click()
        search.clear()
        search.send_keys("Baldur's Gate 3")
        element = self.wait.until(
         EC.element_to_be_clickable(
             (By.CSS_SELECTOR, 'a[href*="app/1086940"]')
         )
        )
        # element.click()
        # Вместо element.click() используем JavaScript
        self.driver.execute_script("arguments[0].click();", element)

        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='В корзину']/parent::a")
            )
        )
        button.click()

        next_btn = self.wait.until(
            EC.element_to_be_clickable(
               (By.CSS_SELECTOR,
                '.DialogButton._DialogLayout.Secondary.Focusable')
                )
        )
        next_btn.click()

        # Поиск и добавление второй игры
        search = self.driver.find_element(
            By.XPATH, '//input[@placeholder="Поиск по магазину"]'
        )
        search.click()
        search.clear()
        search.send_keys("Gothic 1 Remake")
        element2 = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href*="app/1297900"]')
                )
        )
        element2.click()
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='В корзину']/parent::a")
            )
        )
        button.click()
        # Открытие корзины и проверка суммы
        kor = self.wait.until(
            EC.element_to_be_clickable(
             (By.CSS_SELECTOR, ".DialogButton._DialogLayout.Primary.Focusable")
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
        assert sumc.text == "4698 руб"
