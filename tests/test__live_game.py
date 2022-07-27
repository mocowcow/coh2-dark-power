from unittest import TestCase
from unittest.mock import patch
from package import live_game
from unittest.mock import MagicMock


class testGetLiveGames(TestCase):

    @patch('requests.get')
    def test_get_live_games_not_200_throws_exception(self, mock_get):
        mock_res = MagicMock()
        mock_res.status_code = 404
        mock_get.return_value = mock_res
        self.assertRaises(Exception, live_game.get_live_games)
        try:
            live_game.get_live_games()
        except Exception as e:
            self.assertEqual(e.args[0], 'failed to fetch data')

    @patch('requests.get')
    def test_get_live_games_is_200_return_json(self, mock_get):
        mock_res = MagicMock()
        mock_res.status_code = 200
        mock_res.text = '[]'
        mock_get.return_value = mock_res
        self.assertEqual(type(live_game.get_live_games()), list)


def get_mock_live_games():
    # 1 game, 2players, team of 2
    # player1: "race_id":4, steamid:"2222", rankid=5555
    # player2: "race_id":3, steamid:"3333", rankid=5555
    return [{"players": [{"unknown3": 5555, "race_id": 4, "player_profile": {"steamid": "2222"}}, {"unknown3": 5555, "race_id": 3, "player_profile": {"steamid": "3333"}}]}]


def get_broken_player_data():
    # no steam profile players
    return [{"players": [{"unknown3": 5555, "race_id": 4}, {"unknown3": 5555, "race_id": 3}]}]


class testGetInGamePlayers(TestCase):
    @patch('package.live_game.get_live_games')
    def test_get_in_game_players(self, mock_get):
        mock_get.return_value = get_mock_live_games()
        expect = [["2222", 4], ["3333", 3]]
        self.assertListEqual(live_game.get_in_game_players(), expect)

    @patch('package.live_game.get_live_games')
    def test_get_in_game_players_ignore_broken_player(self, mock_get):
        mock_get.return_value = get_broken_player_data()
        expect = []
        self.assertListEqual(live_game.get_in_game_players(), expect)


class testGetInGameTeams(TestCase):

    @patch('package.live_game.get_live_games')
    def test_get_in_game_teams(self, mock_get):
        mock_get.return_value = get_mock_live_games()
        expect = [[["2222", 4], ["3333", 3]]]
        self.assertListEqual(live_game.get_in_game_teams(), expect)

    @patch('package.live_game.get_live_games')
    def test_get_in_game_teams_ignore_broken_player(self, mock_get):
        mock_get.return_value = get_broken_player_data()
        expect = []
        self.assertListEqual(live_game.get_in_game_players(), expect)
