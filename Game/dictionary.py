import unicodedata

with open('dictionary.txt', 'r', encoding='utf-8') as file:
    word_list = set (word.strip().lower() for word in file)
class Dictionary:
    def accents(self, word):
        word = ''.join(x for x in unicodedata.normalize('NFKD', word) if not unicodedata.combining(x))
        return word
    def verify_word(self,word):
        word = word.lower()
        return word in word_list