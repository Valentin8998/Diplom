from selenium import webdriver
from game_page import GamePage
from mainpage import MainPage
from news_center import NewsCenter
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_steam():
    """Главная функция для запуска всех тестов Steam"""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    # Тесты для корзины
    mainpage = MainPage(driver)
    mainpage.adding_to_cart()
    mainpage.clear_basket()
    mainpage.search_by_name()
    mainpage.total_cost()
    # Тесты для новостного центра
    news = NewsCenter(driver)
    news.game_news()
    # Тесты для страницы игры
    game = GamePage(driver)
    game.open_news()

    driver.quit()
