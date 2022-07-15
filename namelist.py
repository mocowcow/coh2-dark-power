
namelist = set()
alias_map = {}


def load_namelist_from_file():
    with open('./lists/blacklist.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        for i in range(len(lines)//2):
            id = lines[i*2]
            alias = lines[i*2+1]
            add(id, alias)


def add(id, alias):
    namelist.add(id)
    alias_map[id] = alias


def get_list():
    load_namelist_from_file()
    return namelist


def get_name_map():
    return alias_map
