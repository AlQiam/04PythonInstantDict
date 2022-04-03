import pandas as pd


df = pd.read_csv('data.csv')


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        definitions = tuple(df.loc[df['word'] == self.term]['definition'])
        print(f'Definitions for {self.term} are:')
        for index, definition in enumerate(definitions):
            print(f'{index+1}- {definition}')


term = input("Search for: ")
define = Definition(term)
define.get()
