from typing import List
from structure.constants import LAMBDA

class WordKeeper:
    '''
        ex of a WordKeeper
        [#, aa, aaaa, aaaaaa]
    '''
    def __init__(self):
        self.word_list = []

    def get_word_list(self) -> List:
        return self.word_list
    
    def insert_word(self, word : str):
        if word == '':
            word == LAMBDA
        if not (word in self.word_list):
            self.word_list.append(word)

    def __repr__(self) -> str:
        string = ''
        for word in self.word_list:
            string += f'{word}'+'\n'
        return string
        
    def __str__(self) -> str:
        string = ''
        for word in self.word_list:
            string += f'{word}'+'\n'
        return string