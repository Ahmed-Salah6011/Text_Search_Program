class Node:
    def __init__(self,key=None,value=None):
        if(key == None):
            self.key=None
        else:
            self.key=key
        ###
        if (value == None):
            self.value = None
        else:
            self.value = value

    def __str__(self):
        return """({}:{})""".format(self.key,self.value)

    def __repr__(self):
        return """({}:{})""".format(self.key,self.value)


############################

class Series:
    def __init__(self,Nodes_list=None):
        if(Nodes_list== None):
            self.N_list=list()
        else:
            self.N_list=list(Nodes_list)


    def find(self,key):
        """search the elements & return the index of the list"""
        if(self.is_empty()):
            return None
        else:
            low=0
            high=len(self.N_list)-1
            while(low<high):
                mid=(low+high)//2
                if(self.N_list[mid].key == key):
                    return mid

                elif (key > self.N_list[mid].key ):
                    low=mid+1

                else:
                    high=mid-1

            return None


    def binary_search(self,key):
        """find the element with the given key & return val if the key exist and
        if not exist return None"""

    def sort(self):
        """sort the elements by key"""

    def insert_order(self,key,val):
        """take key & value
        first check if the key existed or not
        if existed : update the value of existed key with (val)
        if not existed : create new node with the key & val then insert the node (in order) in the N_list"""
        ind=self.find(key)
        if(ind != None): ##key exist
            self.N_list[ind].value=val
        else:
            n=Node(key,val)
            if (self.is_empty()):
                self.N_list.append(n)
            else:
                for i in range(len(self.N_list)):
                    if self.N_list[i].key > key:
                        self.N_list.insert(i,n)
                        break




    def insert(self,key,val):
        """take key & value
        first check if the key existed or not
        if existed : update the value of existed key with (val)
        if not existed : create new node with the key & val then insert the node in the N_list"""


    def delete(self,key):
        """delete the element with the given key from the N_list"""
        if (self.is_empty()):
            return -1
        else:
            ind=self.find(key)
            if(ind != None):
                del self.N_list[ind]
                return 1
            else:
                return -1

    def keys(self):
        """get list of all keys"""

    def values(self):
        """get list of all values"""

    def size(self):
        """get the length of the list"""
        return len(self.N_list)

    def is_empty(self):
        """check if the series is empty"""
        return self.size()==0

    def items(self):
        """return list for traversing through it"""
        return self.N_list



s=Series()
s.insert_order('x',5)
s.insert_order('a',5)
s.insert_order('x',4)
for node in s.items():
    print(node)