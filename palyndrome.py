def palyndrome(word):
    #terminale
    if len(word) <= 1:
        return True
    else:
        return (word[0] == word[-1] and
                palyndrome(word[1:-1]))

def palyndrome_banale(word):
    return word[::-1] == word #prende tutta la parola ma al contrario

if __name__ == '__main__':
    print(palyndrome('casa'))
    print(palyndrome('civic'))

    print(palyndrome_banale('casa'))
    print(palyndrome_banale('civic'))
    #ok