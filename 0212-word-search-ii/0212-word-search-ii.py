class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicates

            # Mark visited
            board[r][c] = "#"

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            # Restore character
            board[r][c] = char

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result