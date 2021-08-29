class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char: str):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 1
