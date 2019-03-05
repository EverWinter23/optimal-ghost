'''
5th march 2019 tuesday
optimal ghost
'''
import gzip
import string
import random
from trie import Trie

def main():
    user_turn = True
    file_name = 'WORD.LST.gz'
    game = OptimalGhost(file_name)
    while True:
        game.play()
        ans = input('play again? [y/n]>> ')
        if ans == 'y':continue
        else: break


class OptimalGhost:
    def __init__(self, file_name):
        self.trie = Trie()
        self.load_words(file_name)

    def play(self):
        turn = 0
        word = ''

        while True:
            if turn % 2 == 0:
                letter = input('enter letter [a-z]>> ').strip()
                while letter not in string.ascii_lowercase:
                    letter = input('enter letter [a-z]>> ')
                word += letter
            
            else:
                letter = self.make_move(turn, word)
                word += letter        
                print('bot chose \'{}\'>> {}'.format(letter, word))                
            
            turn += 1

            possible_moves = self.trie.keys_with_prefix(word)

            # check invalid word-- cannot advance
            if possible_moves is None:
                loser = 'human' if turn % 2 == 1 else 'bot'
                print('{} loses --invalid word[{}]'.format(loser, word))
                break


            # check valid word
            if possible_moves[0] == word:
                loser = 'human' if turn % 2 == 1 else 'bot'
                print('{} loses --valid word[{}]'.format(loser, word))
                break
                                
    def make_move(self, turn, word):
        choice_words = self.trie.keys_with_prefix(word)
        odd_words = [word for word in choice_words if len(word) % 2 == 1]
        even_words = [word for word in choice_words if len(word) % 2 == 0]
        
        if len(odd_words) >= 1:
            bot_word = random.choice(odd_words)
        elif len(even_words) >= 1:
            even_words.sort(key = len, reverse=True)
            bot_word = even_words[0]
        else:
            bot_word = random.choice(string.ascii_lowercase)
        
        if len(bot_word) > 1:
            print(bot_word, turn)
            letter = bot_word[turn]
        else:
            letter = bot_word 
        
        print('bot is building towards [{}]'.format(bot_word))
        
        return letter
        
    def load_words(self, file_name):
        
        with gzip.open(file_name, 'r') as f:
            word_count = 0
            for line in f.readlines():
                line = line.strip().decode()
                if len(line) >= 4:
                    word_count += 1
                    self.trie.put(line, word_count)
            
        '''
        words = 'she sells sea shells on the sea shore'.split(' ')
        for idx, word in enumerate(words):
            self.trie.put(word, idx)
        print(self.trie.keys_with_prefix(''))
        '''

if __name__ == '__main__':
    main()