import requests
import json
from collections import defaultdict


# race_id
# 0=ostheer
# 1=soviet
# 2=okw
# 3=usf
# 4=uk

def get_in_game_teams():
    games = get_live_games()
    res = []
    # group by rank_id
    for g in games:
        d = defaultdict(list)
        for p in g['players']:
            steam_id = p['player_profile']['steamid']
            race_id = p['rece_id']
            rank_id = p["unknown3"]
            d[rank_id].append([steam_id, race_id])
    # frequency greater than 1 means team
    for players in d.values():
        if len(players) > 1:
            res.append(players)
    return res


def get_in_game_players():
    games = get_live_games()
    res = []
    for g in games:
        for p in g['players']:
            steam_id = p['player_profile']['steamid']
            race_id = p['rece_id']
            res.add([steam_id, race_id])
    return res


def get_live_games():
    url = 'https://us-east4-coh2-ladders-prod.cloudfunctions.net/getLiveGamesHttp?playerGroup=4&start=0&count=50&sortOrder=0&apiKey=kmLw58rYG2CWBLQr'
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('failed to fetch data')
    res.encoding = ('utf-8')
    games = json.loads(res.text)
    return games
