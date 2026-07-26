import requests
from config import key, steamId, steamIds
import pytest
import allure
baseUrl = 'https://api.steampowered.com/'


@pytest.mark.api
@allure.title("информация о пользователе")
def test_inf_user() -> None:
    url = 'ISteamUser/GetPlayerSummaries/v2/?'
    resp = requests.get(baseUrl+url+key+steamIds)
    assert resp.status_code == 200


@pytest.mark.api
@allure.title("список игр")
def test_list_game() -> None:
    url = 'IPlayerService/GetOwnedGames/v1/?'
    resp = requests.get(baseUrl+url+key+steamId)
    assert resp.status_code == 200


@pytest.mark.api
@allure.title("игровые новости")
def test_game_news() -> None:
    url = 'ISteamNews/GetNewsForApp/v2/?'
    appid = "appid= 730"
    resp = requests.get(baseUrl+url+appid)
    assert resp.status_code == 200


@pytest.mark.api
@allure.title("не валидный key")
def test_empty_value() -> None:
    resp = requests.get(baseUrl+'IPlayerService/GetOwnedGames/v1/?key=')
    assert resp.status_code == 401


@pytest.mark.api
@allure.title("не валидный appid")
def test_invalid_appid() -> None:
    resp = requests.get(baseUrl+'ISteamNews/GetNewsForApp/v2/?appid=000')
    assert resp.status_code == 403
