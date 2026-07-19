import requests
from config import key, steamId, steamIds
baseUrl = 'https://api.steampowered.com/'


def test_inf_user():
    url = 'ISteamUser/GetPlayerSummaries/v2/?'
    resp = requests.get(baseUrl+url+key+steamIds)
    assert resp.status_code == 200


def test_list_game():
    url = 'IPlayerService/GetOwnedGames/v1/?'
    resp = requests.get(baseUrl+url+key+steamId)
    assert resp.status_code == 200


def test_game_news():
    url = 'ISteamNews/GetNewsForApp/v2/?'
    appid = "appid= 730"
    resp = requests.get(baseUrl+url+appid)
    assert resp.status_code == 200


def test_empty_value():
    resp = requests.get(baseUrl+'IPlayerService/GetOwnedGames/v1/?key=')
    assert resp.status_code == 401


def test_invalid_appid():
    resp = requests.get(baseUrl+'ISteamNews/GetNewsForApp/v2/?appid=000')
    assert resp.status_code == 403
