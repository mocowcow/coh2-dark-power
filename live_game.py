import requests
import json


# race_id
# 0=ostheer
# 1=soviet
# 2=okw
# 3=usf
# 4=uk

def get_in_game_teams():
    pass


def get_in_game_players():
    pass


def get_live_games():
    url = 'https://us-east4-coh2-ladders-prod.cloudfunctions.net/getLiveGamesHttp?playerGroup=4&start=0&count=50&sortOrder=0&apiKey=kmLw58rYG2CWBLQr'
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('failed to fetch data')
    res.encoding = ('utf-8')
    games = json.loads(res.text)
    return games
