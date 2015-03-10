import sys

dictfile = "dictionary.txt"

def get_words(text):
    """ Return a list of dict words """
    return text.split()
    
def get_possible_words(words,jword):
    jword_length = len(jword)
    for word in words:
        jumbled_word = jword
        if len(word) == jword_length:
            letters = list(word)
            for letter in letters:
                if jumbled_word.find(letter) != -1:
                    jumbled_word = jumbled_word.replace(letter,'',1)
            if not jumbled_word:
                return word 
    
    
if __name__ == '__main__':
    words = get_words(file(dictfile).read())
    scrambled = raw_input('The code: ')
    scrambled_split = scrambled.split(';')
    for item in scrambled_split:
	    solution = get_possible_words(words,item)
	    sys.stdout.write(str(solution) + ";")
print " "