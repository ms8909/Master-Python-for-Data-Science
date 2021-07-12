# import pickle

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
        
    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1
        arr = m.split(" ")       
        count = len(arr)         
        self.total_words += count
        
        
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):    
        arr = m.split(" ")
        for i in range(len(arr)):     
            x = 0
            for g in self.index.keys():    
                if arr[i] == g:     
                    x = 1
                    self.index[g].append(l)
                    break

            if x == 0:
                self.index[arr[i]] = []
                self.index[arr[i]].append(l)

        

        

    # implement: query interface

    def search(self, term):
        msgs = []
        for g in self.index.keys():
            if g == term:
                for i in range(len(self.index[g])):
                    t1 = (self.index[g][i], self.msgs[self.index[g][i]])
                    msgs.append(t1)
        return msgs





ind = Index("Tehreem")
ind.add_msg_and_index("she is a good girl")
ind.add_msg_and_index("she is lovely")
ind.add_msg_and_index("she is good at sports")
ind.add_msg_and_index("she likes movies")

answer = ind.search("is")

print(answer)
