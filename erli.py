"""
Алгоритм Эрли
"""

from rule import Rule
from situation import Situation


class ErliAlgorithm:
    def __init__(self, word: str, rules: [Rule]):
        self.word = word
        self.current_pos = None
        self.rules = rules
        self.axiom = rules[0]
        self.lists = []
        self.check_grammar()

    def calculate(self):
        """
        Рассчитать, выводимо ли слово в текущей грамматике
        :return:
        """
        self.first_instruction()
        for list_index, list_ in enumerate(self.lists):
            for index, situation in enumerate(list_):
                if list_index > len(self.word):
                    return False
                if self.check_end(situation, list_index):
                    return True
                if self.second_instruction(situation, list_index):
                    continue
                if self.third_instruction(situation, list_index):
                    continue
                if self.fourth_instruction(situation, list_index):
                    continue
                if self.fifth_instruction(situation, list_index):
                    continue
                if self.sixth_instruction(situation, list_index):
                    continue
        return False

    def print_lists(self):
        """
        Вывести списки
        :return:
        """
        for list_index, list_ in enumerate(self.lists):
            print(f'Список {list_index}: ')
            for situation in list_:
                print(f'\n{situation}')

    def first_instruction(self) -> bool:
        """
        S::=a e P=> [S->?a, 0] e I_0
        :return:
        """
        first_list = [Situation(non_terminal=self.axiom.non_terminal,
                                current_pos=0,
                                body=body,
                                list_index=0) for body in self.axiom.rule_body]
        self.lists.append(first_list)
        return True

    def second_instruction(self, situation: Situation, current_list_index) -> bool:
        """
        [B -> y?, 0] e I_0   [A->a?Bb, 0] e I_0 => [A-> aB?b, 0] e I_0
        :param situation: рассматриваемая ситуация
        :param current_list_index:
        :return:
        """
        # если это не первый список
        if current_list_index:
            return False
        # если после маркера что-то есть
        if situation.after_marker:
            return False
        for situation_to_show in self.lists[0]:
            if situation_to_show.after_marker == situation.non_terminal:
                self.lists[0].append(Situation(non_terminal=situation_to_show.non_terminal,
                                               current_pos=situation_to_show.current_pos+1,
                                               body=situation_to_show.body,
                                               list_index=0))
        return True

    def third_instruction(self, situation, current_list_index):
        """
        [A-> a?Bb, 0] e I_0, => B::= y e P(G); [B->?y, 0]
        :param situation:
        :param current_list_index:
        :return:
        """
        # если это не первый список
        if current_list_index:
            return False
        if situation.after_marker and not situation.is_terminal(situation.after_marker):
            rules = [rule_ for rule_ in self.rules if rule_.non_terminal == situation.after_marker]
            rule = rules[0]
            for rule_body in rule.rule_body:
                self.lists[0].append(Situation(non_terminal=rule.non_terminal,
                                               current_pos=0,
                                               body=rule_body,
                                               list_index=0))
            return True
        return False

    def fourth_instruction(self, situation, current_list_index):
        """
        [B->a?ab,i] e I_(j-1) => [B-> aa>b, i]
        :param situation:
        :param current_list_index:
        :return:
        """
        if situation.after_marker and situation.is_terminal(situation.after_marker):
            if len(self.lists) == current_list_index+1:
                self.lists.append([])
            self.lists[current_list_index+1].append(Situation(non_terminal=situation.non_terminal,
                                                              current_pos=situation.current_pos+1,
                                                              body=situation.body,
                                                              list_index=situation.list_index))
            return True
        return False

    def fifth_instruction(self, situation, current_list_index):
        """
        [A->a?,i] e I_j => [B -> y?Ab, k] e I_k,=> [B->yA?b, k] e I_k
        :param situation:
        :param current_list_index:
        :return:
        """
        if not situation.after_marker:
            for situation_to_show in self.lists[situation.list_index]:
                self.lists[current_list_index].append(Situation(non_terminal=situation_to_show.non_terminal,
                                                                current_pos=situation_to_show.current_pos+1,
                                                                body=situation_to_show.body,
                                                                list_index=situation_to_show.list_index))
            return True
        return False

    def sixth_instruction(self, situation, current_list_index):
        """
        [A->a?Bb, i] e I_j => B::y e P(G); [B->?y,j] e I_j
        :param situation:
        :param current_list_index:
        :return:
        """
        if situation.after_marker and not situation.is_terminal(situation.after_marker):
            rules = [rule_ for rule_ in self.rules if rule_.non_terminal == situation.after_marker]
            rule = rules[0]
            for rule_body in rule.rule_body:
                self.lists[current_list_index].append(Situation(non_terminal=rule.non_terminal,
                                                                current_pos=0,
                                                                body=rule_body,
                                                                list_index=current_list_index))
            return True

    def check_grammar(self):
        """
        Проверить грамматику
        :return:
        """
        non_terminals = [rule.non_terminal for rule in self.rules]
        non_terminals_set = set(non_terminals)
        if len(non_terminals_set) != len(non_terminals):
            raise ValueError('Неправильно задана грамматика')

    def check_end(self, situation, current_list_index) -> bool:
        """
        Нужно ли проверять ограничения
        :return:
        """
        if current_list_index == len(self.word):
            if not situation.list_index and not situation.after_marker\
                    and situation.is_terminal(situation.before_marker):
                return True
        return False
