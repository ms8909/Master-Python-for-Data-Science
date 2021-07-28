import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self, n):
        return self.msgs[n]
        
    # implement
    def add_msg(self, m):
        return
        
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs + 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        return m

    # implement: query interface
# '''
# return a list of tuples. If we index the first sonnet (p1.txt), then
# calling this function with term 'thy' will return the following:
# [(7, " Feed'st thy light's flame with self-substantial fuel,"),
#  (9, ' Thy self thy foe, to thy sweet self too cruel:'),
#  (9, ' Thy self thy foe, to thy sweet self too cruel:'),
#  (12, ' Within thine own bud buriest thy content,')]          
# '''                      
    def search(self, term):
        msgs = []
        return msgs


my_idx = Index('hahaha')
my_idx.add_msg_and_index('what is this thing called?')




#
# Lab Marh 13

#class PIndex(Index):
#    def __init__(self, name):
#        super().__init__(name)
#        roman_int_f = open('roman.txt.pk', 'rb')
#        self.int2roman = pickle.load(roman_int_f)
#        roman_int_f.close()
#        self.load_poems()
#
#        # Implement: 1) open the file for reading, then call
#        # the base class's add_msg_and_index
#    def load_poems(self):
#       return
#
#        # Implement: p is an integer, get_poem(1) returns a list,
#        # each item is one line of the 1st sonnet
#    def get_poem(self, p):
#        poem = []
#        return poem
#
#if __name__ == "__main__":
#    # The next three lines are just for testing
#    # You are encouraged to add to this and create your own tests!
#    # Call your functions as you implement them and see if they work
#    sonnets = PIndex("AllSonnets.txt")
#    p3 = sonnets.get_poem(3)
#    s_love = sonnets.search("love")
