from unittest import TestCase
from unittest.mock import patch
from package import observer
from unittest.mock import MagicMock


def get_mock_in_game_players():
    return [['0000', 0],  ['2222', 4], ['3333', 3],  ['5555', 1], ['6666', 1], ['987987', 2], ['114514', 3]]


def get_mock_in_game_teams():
    return [[['1111', 0], ['2222', 0], ['456546', 2], ['114514', 2]]]


def get_mock_namelist():
    return {'1111', '2222', '3333', '4444'}


def get_mock_namemap():
    return {'1111': 'man1111', '2222': 'man2222', '3333': 'man3333', '4444': 'man4444'}


class testCheckPlayers(TestCase):

    @patch('package.live_game.get_in_game_players')
    def test_2_players_in_game(self, mock_get_games):
        observer.id_list = get_mock_namelist()
        observer.mp = get_mock_namemap()
        mock_get_games.return_value = get_mock_in_game_players()
        expect = [['man2222', 'british'], ['man3333', 'usf']]
        self.assertListEqual(observer.check_players(), expect)


class testCheckTeams(TestCase):

    @patch('package.live_game.get_in_game_teams')
    def test_2_players_in_team_of_4(self, mock_get_teams):
        observer.id_list = get_mock_namelist()
        observer.mp = get_mock_namemap()
        mock_get_teams.return_value = get_mock_in_game_teams()
        expect = [['man1111 & man2222', 'AXIS', 'team of 4']]
        self.assertListEqual(observer.check_teams(), expect)
