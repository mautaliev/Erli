from unittest import TestCase
from rule import Rule


class TestRule(TestCase):
    def test_init(self):
        first_example = 'S::=aQb | accb'
        second_example = 'S::=ab'
        self.assertEqual('S::=aQb|accb', str(Rule(first_example)))
        self.assertEqual("NT=S, RB=['aQb', 'accb']", repr(Rule(first_example)))
        self.assertEqual('S::=ab', str(Rule(second_example)))
        self.assertEqual("NT=S, RB=['ab']", repr(Rule(second_example)))
