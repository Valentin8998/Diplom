from selenium import webdriver
from game_page import GamePage
from mainpage import MainPage
from news_center import NewsCenter
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
import time


@pytest.fixture
def driver():
    """Фикстура для создания драйвера"""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@pytest.mark.u
@allure.title("Добавление игры в корзину")
@allure.story("Корзина")
def test_adding_to_cart(driver):
    mainpage = MainPage(driver)
    with allure.step("Ввести в поле 'Поиск по магазине' название игры"):
        mainpage.search("Baldur's Gate 3", "app/1086940")
        time.sleep(2)
    with allure.step("Нажать кнопку 'В корзину'"):
        mainpage.adding()
        time.sleep(2)
    with allure.step("Нажать кнопку 'Открыть корзину'"):
        mainpage.basket()
        time.sleep(2)
    with allure.step("Проверить что товаров в корзине 1"):
        mainpage.asert_product()
        time.sleep(2)


@pytest.mark.ui
@allure.title("Поиск по магазину")
@allure.story("Поиск")
def test_search_by_name(driver):
    mainpage = MainPage(driver)
    with allure.step("Ввести в поле 'Поиск по магазине' название игры"):
        mainpage.search("Baldur's Gate 3", "app/1086940")


@pytest.mark.ui
@allure.title("Итоговая стоймость 2 игр")
@allure.story("Корзина")
def test_total_cost(driver):
    mainpage = MainPage(driver)
    with allure.step("Ввести в поле 'Поиск по магазине' название игры"):
        mainpage.search("Baldur's Gate 3", "app/1086940")
    with allure.step("Нажать кнопку 'В корзину"):
        mainpage.adding()
    with allure.step("Нажать кнопку 'Продолжить покупки'"):
        mainpage.continue_shopping()
    with allure.step("Ввести в поле 'Поиск по магазине' название игры"):
        mainpage.search("Gothic 1 Remake", "app/1297900")
    with allure.step("Нажать кнопку 'В корзину"):
        mainpage.adding()
    with allure.step(
         "открыть корзину и проверить что итоговая стоймость =4698"):
        mainpage.assert_basket()


@pytest.mark.ui
@allure.title("Открытие новостей с страницы игры")
@allure.story("Новости")
def test_open_news(driver):
    gamepage = GamePage(driver)
    with allure.step("Открытить новости с страницы игры"):
        gamepage.open_news()


@pytest.mark.ui
@allure.title("Поиск новостей по названию игры")
@allure.story("Новости")
def test_game_news(driver):
    newscenter = NewsCenter(driver)
    with allure.step("Поиск новостей по названию игры"):
        newscenter.game_news("Path of Exile 2")
