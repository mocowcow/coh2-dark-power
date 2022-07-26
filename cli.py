from package import observer

while True:
    print('1 check certain players')
    print('2 check certain teams')
    ip = input()
    print('------------')
    try:
        if ip == '1':
            print(observer.check_players())
        elif ip == '2':
            print(observer.check_teams())
        else:
            break
    except Exception as e:
        print(e)
    print('------------')
