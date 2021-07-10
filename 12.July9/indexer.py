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
        
   def add_msg(self, msg):
      self.msgs.append(msg)
      self.total_msgs+=1
      arr=msg.split()
      wordsCount=len(arr)
      self.total_words+=wordsCount

        
   def add_msg_and_indexing(self, msg_2):
      self.add_msg(msg_2)
      Line_No = self.total_msgs - 1
      self.indexing(msg_2, Line_No)

  
   def indexing(self, msg_3, Line_No):
      self.index[Line_No]=msg_3

   def search(self, term):
      msgs = []
      for i in range(self.total_msgs):
         arr=self.index[i].split()
         for z in (arr):
            if (z==term):
               msgs.append((i,self.index[i]))
               break
      return msgs

obj=Index("Hello")
obj.add_msg_and_indexing("she is a teacher")
obj.add_msg_and_indexing("she is a good girl")
obj.add_msg_and_indexing("who is she?")

ans=obj.search("she")
print(ans)


