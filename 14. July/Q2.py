import pickle
import Q1

class PIndex(Q1.Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

    def load_poems(self):
        lines = open('{}.txt'.format(self.name), 'r').readlines()
        for line in lines:
            self.add_msg_and_index(line)

    def get_poem(self, p):
        poem = []
        condition = 0
        self.load_poems()

        for i in range(len(self.msgs)):
            if '{}.'.format(self.int2roman[p]) in self.msgs[i]:
                condition = 1
            elif '{}.'.format(self.int2roman[p + 1]) in self.msgs[i]:
                condition = 2

            if condition == 1:
                poem.append(self.msgs[i])
            elif condition == 2:
                break

        return poem
