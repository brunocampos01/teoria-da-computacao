# A suffix automaton is a powerful data structure
#  that allows solving many string-related problems.

# Python program for add and search
# operation in a Trie
 

# prefix tree
# Trie é provavelmente a estrutura de dados baseada em árvore mais básica e intuitiva projetada para usar com strings.
# algoritmo famoso de Ukkonen
    
from trie_node import TrieNode


class Trie:     
    def __init__(self):
        self.root = TrieNode("")
 
    def insert(self, word):
        node = self.root

        for char in word:
            # Check if there is no child containing the character,
            # create a new child for the current node
            if char in node.children:
                node = node.children[char]
                node.counter += 1
            else:
                # If a character is not found, create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                # print(f'creating node = {char}')

        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix): 
        """Depth-first traversal of the trie
        
        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def search(self, word: str):
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in word:
            print(node.children.keys())

            if char in node.children:
                node = node.children[char]
            else:
                return []
 
        # Traverse the trie to get all candidates
        self.dfs(node, word[:-1])

        # Sort the results in reverse order and return
        # return sorted(self.output, key=lambda x: x[1], reverse=True), node.counter

    def avg_of_keystrokes(self, word: str) -> int:
        self.search(word=word)



#   int count_keys(const char *s) {
#     int state = 0;
#     int ans = 0;
#     for(; *s; ++s){ # ponteiro para "s"
#       int c = 0;
#       if(*(s+1)) // is not $
#         for(int k = 0 ; k < 27 ; ++k)
#           if(g[state][k] != -1) c++;
#       if(c > 1 or (c == 1 and state == 0)) ans++;
#       int next = (*s == '$')? 26 : (*s - 'a'); // $ == not found
#       state = g[state][next];
#     }
#     return ans;
#   }


def main():
    list_words = ['hello', 'hell', 'heaven']
    tree = Trie()
    tree.insert("hello")
    print()
    tree.insert("hell")
    print()
    tree.insert("heaven")
    print()

    # print(tree.search("h")) # 1 typing
    # print(tree.search("he")) # 2 typing
    # print(tree.search("hea")) # 3 typing

    for word in list_words:
        print(word)
        tree.avg_of_keystrokes(word)


if __name__ == '__main__':
    main()
