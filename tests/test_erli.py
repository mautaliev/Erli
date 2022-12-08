from unittest import TestCase
from erli import ErliAlgorithm
from rule import Rule


class TestErli(TestCase):
    def test_init(self):
        word = 'acacbcb'
        rules_str = ['S::=aQb|accb', 'Q::=cSc']
        rules = [Rule(rule_) for rule_ in rules_str]
        erli = ErliAlgorithm(word, rules)
        self.assertTrue(erli)
