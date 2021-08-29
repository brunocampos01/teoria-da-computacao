from typing import Tuple


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.is_end = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root

    print(f'word = {word}')
    for char in word:
        print(f'char = {char}')
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # print(f'child.char == char = {child.counter}')

                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break

        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            print(new_node)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.is_end = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter


def avg_of_keystrokes():
    pass



if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hello")
    print()
    add(root, 'heaven')
    print()
    add(root, 'goodbye')
    print(79 * '*')

    print(find_prefix(root, 'h')) # 1
    print(find_prefix(root, 'he')) # 1 + 1
    print(find_prefix(root, 'hel')) # 1 + 1 + 1
    print(find_prefix(root, 'hell'))  # incluirá um segundo "l" + "o" automaticamente
    print(find_prefix(root, 'hello'))
    # print(find_prefix(root, 'heaven'))

    print(79 * '*')
    print(find_prefix(root, 'g'))
    print(find_prefix(root, 'goodbye'))
    # print(find_prefix(root, 'ha'))

    print(root.char)
    print(root.__dict__)
