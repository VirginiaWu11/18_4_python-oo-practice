"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    def __init__(self,f_ext):
        self.f_ext = f_ext
        file = open(self.f_ext,'r')
        line_arr =[line for line in file]
        print(f'{len(line_arr)} words read')
    def random(self):
        file = open(self.f_ext,'r')
        line_arr =[line.strip() for line in file]
        print(choice(line_arr))
class SpecialWordFinder(WordFinder):
    def __init__ (self,f_ext):
        super().__init__(f_ext)
    def random(self):
        file = open(self.f_ext,'r')
        line_arr =[line.strip() for line in file if line!= '\n' and not line.startswith('#')]
        print(choice(line_arr))
    