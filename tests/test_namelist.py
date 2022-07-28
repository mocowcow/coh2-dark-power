from unittest import TestCase
from unittest.mock import patch
from package import namelist
from unittest.mock import MagicMock, mock_open


class testLoadNameListFromFile(TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='AAAA\n')
    def test_uneven_list_throws_exception(self, mock_builtin_open):
        self.assertRaises(ValueError, namelist.load_namelist_from_file)
        try:
            namelist.load_namelist_from_file()
        except ValueError as e:
            self.assertEqual(e.args[0], 'list should be even lines')

    @patch('builtins.open', new_callable=mock_open, read_data='AAAA\nBBBB\n')
    def test_invalid_steam_id_throws_exception(self, mock_builtin_open):
        self.assertRaises(ValueError, namelist.load_namelist_from_file)
        try:
            namelist.load_namelist_from_file()
        except ValueError as e:
            self.assertEqual(e.args[0], 'invalid steam_id')
