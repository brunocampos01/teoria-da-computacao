class TrieNode:
    """Um nó na estrutura trie"""

    def __init__(self, char: str):
        # a letra armazenada neste nó
        self.char = char
        # pode ser o fim de uma palavra
        self.is_end = False
        # um dicionário de nós filhos onde chaves são caracteres e os valores são nós
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # Verifica se o nó filho contem o caractere da word
            if char in node.children:
                node = node.children[char]
            else:
                # se não encontrado, cria o novo nó na trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def get_total_keystrokes_by_word(self, word: str) -> int:
        """
        Obtém o total de teclas digitadas
        """
        node = self.root
        total_keystrokes = 0

        for char in word:
            total_child = len(node.children.keys())

            # se o nó da trie é final ou se total_child é maior do q 1, então conta mais uma tecla
            if total_child > 1 or node.is_end is True:
                # print(f'typing   {node.children.keys()}')
                total_keystrokes += 1

            # próximo node da trie
            node = node.children[char]

        return total_keystrokes


tree = Trie()


def main():
    # list_words = ['hello', 'hell', 'heaven', 'goodbye']
    # tree.insert("hello")
    # tree.insert("hell")
    # tree.insert("heaven")
    # tree.insert("goodbye")
    #
    # list_words = ['hi', 'he', 'h']
    # tree.insert("hi")
    # tree.insert("he")
    # tree.insert("h")

    list_words = ['structure', 'structures', 'ride', 'riders', 'stress', 'solstice', 'ridiculous']
    tree.insert("structure")
    tree.insert("structures")
    tree.insert("ride")
    tree.insert("riders")
    tree.insert("stress")
    tree.insert("solstice")
    tree.insert("ridiculous")

    ans = float()
    for i in list_words:
        ans += tree.get_total_keystrokes_by_word(word=i)

    # média de pressionamentos de tecla por dicionário
    a = ans / float(len(list_words))
    print(round(a, 2)) # 35%


if __name__ == '__main__':
    main()
