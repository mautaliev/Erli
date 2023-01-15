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

    def test_index_out(self):
        word = 'abab'
        rules_str = ['S::=AB', 'A::=aAb|ab', 'B::=cBd|cd']
        rules = [Rule(rule_) for rule_ in rules_str]
        erli = ErliAlgorithm(word, rules)
        self.assertTrue(erli.calculate())
        
    # def test_1(self):
    #     word = 'aabbcd'
    #     rules_str = ['S::=AB', 'A::=aAb|ab', 'B::=cBd|cd']
    #     rules = [Rule(rule_) for rule_ in rules_str]
    #     erli = ErliAlgorithm(word, rules)
    #     self.assertTrue(erli.calculate())

    def test_2(self):
        word = 'a'