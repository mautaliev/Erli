from dataclasses import dataclass


@dataclass
class Situation:
    non_terminal: str
    current_pos: int
    body: str
    list_index: int

    @property
    def before_marker(self):
        """
        Получаем терминал/нетерминал перед маркером
        :return:
        """
        if not self.current_pos:
            return None
        return self.body[self.current_pos-1]

    @property
    def after_marker(self):
        """
        Получаем терминал/нетерминал после маркера
        :return:
        """
        if self.current_pos < len(self.body):
            return self.body[self.current_pos]
        return None

    @classmethod
    def is_terminal(cls, word) -> bool:
        """
        Терминальный ли элемент
        :param word: элемент для проверки на то, терминальный ли он или нетерминальный
        :return:
        """
        return word.islower()

    def __str__(self):
        return f'[{self.non_terminal} -> {self.body[:self.current_pos]} ? {self.body[self.current_pos:]},' \
               f' {self.list_index}]'
