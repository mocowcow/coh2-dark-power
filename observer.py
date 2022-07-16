import namelist
import live_game


def check_players():
    players = live_game.get_in_game_players()
    res = []
    for steam_id, race_id in players:
        if steam_id in id_list:
            alias = mp[steam_id]
            res.append([alias, race[race_id]])
    return res


def check_teams():
    teams = live_game.get_in_game_teams()
    res = []
    for players in teams:
        valid_id = []
        for steam_id, race_id in players:
            if steam_id in id_list:
                print(steam_id, mp[steam_id])
                valid_id.append(mp[steam_id])
        if valid_id:
            team_name = ' & '.join(valid_id)
            team_side= side[race_id]
            ppl = len(players)
            res.append([team_name, team_side,ppl])
    return res


id_list = namelist.get_list()
mp = namelist.get_name_map()
race = {
    0: 'ostheer',
    1: 'soviet',
    2: 'okw',
    3: 'usf',
    4: 'british'
}
side = {
    0: 'AXIS',
    1: 'ALLIES',
    2: 'AXIS',
    3: 'ALLIES',
    4: 'ALLIES'
}


if __name__ == '__main__':
    while True:
        print('1 check certain players')
        print('2 check certain teams')
        ip = input()
        print('------------')
        try:
            if ip == '1':
                print(check_players())
            elif ip == '2':
                print(check_teams())
            else:
                break
        except Exception as e:
            print(e)
        print('------------')
