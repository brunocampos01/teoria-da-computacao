if __name__ == '__main__':
    n = 4
    list_words = ['hello', 'hell', 'heaven', 'goodbye'] # vector<string> words(n);
    test_word = 'goodbye'

    for word in list_words:
        # print(word)
        for letter in word:
            print(letter)

            if letter in test_word:
                print(f'contain {letter} in {word}')
        