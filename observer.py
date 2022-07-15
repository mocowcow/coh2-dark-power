import namelist
import live_game


def check_players():
    players = live_game.get_in_game_players()
    res = []
    for steam_id, race_id in players:
        if steam_id in id_list:
            alias = mp[steam_id]
            res.append([alias, race_id])
    return res


def check_teams():
    pass


id_list = namelist.get_list()
mp = namelist.get_name_map()


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
