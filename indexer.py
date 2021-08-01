

class Index:
    def __init__(self,name):
        self.name=name
        self.msgs=[]
        self.index={}
        self.total_msgs=0
        self.total_words=0

    def get_total_words(self):
        return self.total_words
    
    def get_total_msgs(self):
        return self.total_msgs

    def get_msg(self,n):
        return self.msgs[n]

    def add_msg(self,msg):
        self.msgs.append(msg)
        self.total_msgs+=1
        arr=msg.split()
        wordsCount=len(arr)
        self.total_words+=wordsCount

    def add_msg_and_indexing(self,msg_2):
        self.add_msg(msg_2)
        lineNo=self.total_msgs-1
        self.indexing(msg_2,lineNo)

    def indexing(self,msg_3,LineNo):
        arr=msg_3.split(' ')
        for i in range (len(arr)):
            j=0
            for key in self.index.keys():
                if(arr[i]==key):
                    self.index[key].append(LineNo)
                    j=1
                    break
            if(j!=1):
                self.index[arr[i]]=[]
                self.index[arr[i]].append(LineNo) 

    
    def search(self,term):
        msgs=[]
        for key in self.index.keys():
            if(key==term):
                for z in range(len(self.index[key])):
                    tup=(self.index[key][z],self.msgs[self.index[key][z]])
                    msgs.append(tup)
        return msgs

        


obj=Index('Hello')

obj.add_msg_and_indexing('What is this thing')
obj.add_msg_and_indexing('who is who?')

ans=obj.search('who')

print(ans)
