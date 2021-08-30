class TrieNode:
    """A node in the trie structure"""

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

    # list_words = ['hi', 'he', 'h']
    # tree.insert("hi")
    # tree.insert("he")
    # tree.insert("h")

    # list_words = ['structure', 'structures', 'ride', 'riders', 'stress', 'solstice', 'ridiculous']
    # tree.insert("structure")
    # tree.insert("structures")
    # tree.insert("ride")
    # tree.insert("riders")
    # tree.insert("stress")
    # tree.insert("solstice")
    # tree.insert("ridiculous")

    # ans = 0
    # for i in list_words:
    #     print(i)
    #     ans += tree.get_total_keystrokes_by_word(word=i)
    #
    # print(round(ans / len(list_words), 2))

    n = int(input())
    while 1 <= n <= 10 * 5:
        list_words = []
        word = str(input())[:80]  # contém uma string não vazia de no máximo 80 letras minúsculas
        list_words.append(word)
        tree.insert(word)

        # obtem uma quantidade de teclas digitadas a partir de um dicionário de palavras
        ans = sum(
            tree.get_total_keystrokes_by_word(word=word)
            for word in list_words
        )

        # média de pressionamentos de tecla por dicionário
        print(round(ans / len(list_words), 2))

        # a soma dos comprimentos de todas as palavras é no máximo 10 ^ 6
        total_len = [len(w) for w in list_words][0]
        if total_len >= 10 * 6:
            break


if __name__ == '__main__':
    main()
