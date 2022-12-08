class Rule:
    def __init__(self, rule):
        non_terminal, rule_body = self.parse_rule(rule)
        self.non_terminal = non_terminal
        self.rule_body = rule_body

    @staticmethod
    def parse_rule(rule):
        """
        Распарсить правило
        :param rule: входная строка вида правила, например: S::=aQb|accb
        :return:
        """
        if not rule:
            raise ValueError('Правило не объявлено')
        parsed_rule = rule.split('::=')
        if len(parsed_rule) != 2:
            raise ValueError("В правиле не один '::='")
        non_terminal = parsed_rule[0].strip()
        rule_body = parsed_rule[1].split('|')
        rule_body = [item.strip() for item in rule_body]
        return non_terminal, rule_body

    def __str__(self):
        return f'{self.non_terminal}::={"|".join(self.rule_body)}'

    def __repr__(self):
        return f'NT={self.non_terminal}, RB={self.rule_body}'
