from erli import ErliAlgorithm
from rule import Rule


def main():
    word = input('Введите слово: ')
    if not word.islower():
        raise ValueError('Некорректное слово!')

    rules = []
    while True:
        rule = input('Введите правило: ')
        if not rule:
            break
        rules.append(Rule(rule))
    erli_algorithm = ErliAlgorithm(word, rules)
    flag = erli_algorithm.calculate()
    erli_algorithm.print_lists()
    print('Цепочка {} выводима'.format('' if flag else 'не'))


if __name__ == '__main__':
    main()
