class Node :
    def __init__(self, key=None, color= "Red"):
        self.val=key
        self.color=color
        self.left = None
        self.right = None
        self.parent = None
        

class RedBlackTree :
    def __init__(self):
        self.NIL= Node(color="Black")
        self.root= self.NIL
        self.size= 0

    def get_size(self) :
        return self.size
    
    def get_root(self):
        return self.root
    
    def search(self, key):
        node= self.root
        
        while node != self.NIL :
            if key == node.val :
                return node 
            elif key < node.val :
                node = node.left
            else :
                node = node.right

        return None         
    
    def get_height(self, node=None) :
        if node == None :
            node = self.root

        if node == self.NIL:
            return 0
        else :
            return 1 + max(self.get_height(node.left),self.get_height(node.right)) 

    def get_balck_height(self) :
        node =self.root
        black_count = -1
        while node != self.NIL :
            if node.color == "Black" : 
                black_count+=1
            node = node.left

        return  black_count    
