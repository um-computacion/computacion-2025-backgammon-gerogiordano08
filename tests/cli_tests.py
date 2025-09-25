from core.cli import CLI
from core.game import Game
from core.board import Board
import unittest
from unittest.mock import Mock, patch
class CLITests(unittest.TestCase):
    def setUp(self) -> CLI:
        cli = CLI()
        cli.set_contador(1)
        return cli
    def test_do_play_winner_p1(self):
        cli = self.setUp()
        ng = Game('a', 'b')
        b = Board()
        b.put_checker(1, 'o')
        ng.set_board(b)
        cli.set_game(ng)
        self.assertEqual(cli.do_play(self), 'a')
    def test_do_play_winner_p2(self):
        cli = self.setUp()
        ng = Game('a', 'b')
        b = Board()
        b.put_checker(1, 'x')
        ng.set_board(b)
        cli.set_game(ng)
        self.assertEqual(cli.do_play(self), 'b')
