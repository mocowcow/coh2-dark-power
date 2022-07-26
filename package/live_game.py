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
            if 'player_profile' not in p:
                continue
            steam_id = p['player_profile']['steamid']
            race_id = p['race_id']
            rank_id = p['unknown3']
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
            if 'player_profile' not in p:
                continue
            steam_id = p['player_profile']['steamid']
            race_id = p['race_id']
            res.append([steam_id, race_id])
    return res


def get_live_games(start=0, count=100):
    url = f'https://us-east4-coh2-ladders-prod.cloudfunctions.net/getLiveGamesHttp?playerGroup=4&start={start}&count={count}&sortOrder=0&apiKey=kmLw58rYG2CWBLQr'
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('failed to fetch data')
    res.encoding = ('utf-8')
    games = json.loads(res.text)
    if len(games) == count:
        games += get_live_games(start=start+count, count=count)
    return games
