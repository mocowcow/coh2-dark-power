import namelist
import live_game


def check_players():
    pass


def check_teams():
    pass


if __name__ == '__main__':
    while True:
        print('1 check certain players')
        print('2 check certain teams')
        ip = input()
        print('------------')
        try:
            if ip == '1':
                check_players()
            elif ip == '2':
                check_teams()
            else:
                break
        except Exception as e:
            print(e)
        print('------------')
