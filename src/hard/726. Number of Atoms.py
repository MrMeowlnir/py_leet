from src.tests import *
from src.bcolor import bcolors


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Given a string formula representing a chemical formula, return the count of each atom.

        The atomic element always starts with an uppercase character,
        then zero or more lowercase letters, representing the name.

        One or more digits representing that element's count may follow if the count is greater than 1.
        If the count is 1, no digits will follow.

        For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
        Two formulas are concatenated together to produce another formula.

        For example, "H2O2He3Mg4" is also a formula.
        A formula placed in parentheses, and a count (optionally added) is also a formula.

        For example, "(H2O2)" and "(H2O2)3" are formulas.
        Return the count of all elements as a string in the following form: the first name (in sorted order),
        followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed
        by its count (if that count is more than 1), and so on.

        The test cases are generated so that all the values in the output fit in a 32-bit integer.
        """
        n = len(formula)
        stack = []
        i = 0
        while i < n:
            if formula[i] == '(':
                stack.append((formula[i], 0))
                i += 1
            elif formula[i] == ')':
                i += 1
                mult_num = 0
                while i < n and formula[i].isdigit():
                    mult_num = mult_num * 10 + int(formula[i])
                    i += 1
                if mult_num == 0:
                    mult_num = 1

                temp = []
                while stack and stack[-1][0] != '(':
                    name, count = stack.pop()
                    count *= mult_num
                    temp.append((name, count))
                stack.pop()

                for name, count in temp:
                    stack.append((name, count))
            else:
                if i + 1 < n and formula[i + 1].islower():
                    name = formula[i] + formula[i + 1]
                    i += 2
                else:
                    name = formula[i]
                    i += 1

                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if count == 0:
                    count = 1

                stack.append((name, count))

        atoms = dict()
        for name, count in stack:
            atoms[name] = atoms.get(name, 0) + count

        result = ''
        for name, count in sorted(atoms.items()):
            result += name
            if count > 1:
                result += str(count)
        return result


if __name__ == '__main__':
    solution = Solution()
    func_test = solution.countOfAtoms
    cases = [
        {'data':
            {
                'formula': 'H2O',
            },
            'result': 'H2O'},
        {'data':
            {
                'formula': 'Mg(OH)2',
            },
            'result': 'H2MgO2'},
        {'data':
            {
                'formula': 'K4(ON(SO3)2)2',
            },
            'result': 'K4N2O14S4'},
    ]
    failed = []
    for case in cases:
        fail = print_tests(func_test, case['data'], case['result'])
        if fail:
            failed.append(fail)

    if failed:
        print(f'{bcolors.WARNING}Total failed {len(failed)} of test cases{bcolors.ENDC}')
    for fail in failed:
        print(f'{fail["Case"]}: '
              f'Expected: {bcolors.OKGREEN}{fail["Expected"]}{bcolors.ENDC}, '
              f'Actual: {bcolors.FAIL}{fail["Actual"]}{bcolors.ENDC}')
