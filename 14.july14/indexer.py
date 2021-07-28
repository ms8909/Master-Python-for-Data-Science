import pickle

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

class Pindex(Index):
    def __init__(self, filename):
        super().__init__(filename)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_file()

    def load_file(self):
        dic={}
        lines=open(self.name,'r').readlines()
        # This for loop to store the poems in dictionary according to there roman no as key name
        for L in lines:
            if(self.checkRoman(L[:-2])==True):
                key=L[:-2]
                dic[key]=[]
            elif(L!='\n'):
                dic[key].append(L)
        # This for loop to convert dictionaries key and values into single string to store in self.msgs
        for key in dic.keys():
            strr=key+' '
            for k in dic[key]:
                strr=strr+k
            self.add_msg_and_indexing(strr)

    # Added extra function too check the Roman entries
    def checkRoman(self,arr):
        for key in self.int2roman:
            if(arr==self.int2roman[key]):
                return True
        return False

        
    def get_poem(self, p):
        poem = []
        poem=self.msgs[p-1]
        # Just Used split and for loop to print poem according to Question paper
        poem=poem.split(' ')
        print(poem[0])
        for i in range(1,len(poem)):
           print(poem[i],end=' ')
    

obj=Pindex('AllSonnets.txt')
obj.get_poem(2)