import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = [];
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self, n):
        return self.msgs[n]
        
    # implement'


    def add_msg(self, m):
        self.total_msgs+=1
        self.msgs.append(m)

        print(self.msgs)
        return self.msgs

  
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        
        self.index.update(l=m)
        print (self.index)
        return self.index

    # implement: query interface
    
    def search(self, term):
        msgs = []
       
        # for item in self.index:
        #     # print(item)


myindex=Index ("practise")
myindex.add_msg_and_index("What is this thing")
myindex.add_msg_and_index("Who Knows Who")
myindex.search("Who")




    


