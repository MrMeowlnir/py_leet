class CharPoint:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False


class WordSearch:
    def __init__(self):
        self.root = CharPoint()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = CharPoint()
            node = node.children[char]
        node.isEndofWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = set()

        def trace(row, col, parent, path):
            letter = board[row][col]
            cur_point = parent.children[letter]

            path += letter
            if cur_point.isEndofWord:
                result.add(path)
                cur_point.isEndofWord = False

            board[row][col] = '*'
            for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < len(board) and  0 <= new_col < len(board[0]):
                    if board[new_row][new_col] in cur_point.children:
                        trace(new_row, new_col, cur_point, path)

            board[row][col] = letter
            if not cur_point.children:
                parent.children.pop(letter)

        seeker = WordSearch()
        for word in words:
            seeker.insert(word)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in seeker.root.children:
                    trace(row, col, seeker.root, '')

        return list(result)


if __name__ == '__main__':
    solution = Solution()
    cases = [dict({'board': [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]],
                   'words': ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]}),
             dict({'board': [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                   'words': ["oath", "pea", "eat", "rain", "hklf", "hf"]}),
             dict({'board': [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                   'words': ["oath", "pea", "eat", "rain"]}),
             dict({'board': [["a", "b"], ["c", "d"]],
                   'words': ["abcb"]}),
             dict({'board': [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
                   'words': ["oa", "oaa"]}),
             dict({'board': [["a", "a"]],
                   'words': ["aa"]}),

             ]
    for case in cases:
        print(solution.findWords(**case))
