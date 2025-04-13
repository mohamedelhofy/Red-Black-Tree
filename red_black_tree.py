import math
import random
class Node :
    def __init__(self, val=None, color= "Red"):
        self.val=val
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

    def get_black_height(self) :
        node =self.root
        black_count = 0
        while node != self.NIL :
            if node.color == "Black" : 
                black_count+=1
            node = node.left

        return  black_count    

    def insert(self, val) :
        node = Node(val=val)
        node.left = self.NIL
        node.right = self.NIL

        current = self.root
        parent = None
        if current == self.NIL:
            node.color = "Black"
            node.parent = None
            self.root = node
            self.size += 1
            return
        

        while current != self.NIL :
            parent = current
            if val == current.val :
                print("ERROR: Word already in the dictionary!")
                return
            elif val < current.val :
                current = current.left
            else :
                current = current.right

        node.parent = parent
        if val < parent.val :    
            parent.left = node
        else :
            parent.right = node
        
        self.size += 1
        self.fix_insert(node)

    def fix_insert(self, node) :
        while node.parent!= None and node.parent.color == "Red" :
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:
                break 
            
            if grandparent.left == parent :
                uncle =  grandparent.right
                if uncle.color == "Red" :
                    parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent
                else : 
                    if parent.right == node:
                        self.left_rotate(parent)
                        node = parent
                        parent = node.parent
                    parent.color = "Black"
                    grandparent.color = "Red"
                    self.right_rotate(grandparent)
            else :         
                uncle =  grandparent.left 
                if uncle.color == "Red" :
                    parent.color = "Black"
                    uncle.color = "Black"
                    grandparent.color = "Red"
                    node = grandparent
                else : 
                    if parent.left == node :
                        self.right_rotate(parent)
                        node = parent 
                        parent = node.parent
                    parent.color = "Black"
                    grandparent.color = "Red"
                    self.left_rotate(grandparent)

        self.root.color = "Black"      

    def right_rotate(self, node):
        old_parent =node
        new_parent = node.left
        old_parent.left = new_parent.right
        if new_parent.right!= self.NIL  :
            new_parent.right.parent = old_parent

        new_parent.parent = old_parent.parent
        if old_parent.parent == None :
            self.root = new_parent
        elif  old_parent.parent.left == old_parent :
               old_parent.parent.left = new_parent
        else :
                old_parent.parent.right = new_parent

        new_parent.right =  old_parent
        old_parent.parent = new_parent

    def left_rotate(self, node) :
        old_parent =node
        new_parent = node.right
        old_parent.right = new_parent.left
        if new_parent.left!= self.NIL :
            new_parent.left.parent = old_parent

        new_parent.parent = old_parent.parent
        if old_parent.parent == None :
            self.root = new_parent
        elif  old_parent.parent.right == old_parent :
               old_parent.parent.right = new_parent
        else :
                old_parent.parent.left = new_parent

        new_parent.left =  old_parent
        old_parent.parent = new_parent

    def __print_helper(self,node, indent="", last=True):
        if node is not None:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "

            color = "B" if node.color == "Black" else "R"
            print(f"{node.val}({color})")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "", True) 

    def mix(self, node):
        while node.right != self.NIL :
            node = node.right

        return node

    def min(self, node):
        while node.left != self.NIL :
            node = node.left

        return node
    
    def predecessor(self,node):
        if node.left!=self.NIL:
            return self.mix(node.left)
        parent = node.parent

        while parent != self.NIL and parent.left == node :
            parent= parent.parent
            node= node.parent

        return parent
    
    def successor(self,node):
        if node.right!=self.NIL:
            return self.min(node.right)
        parent = node.parent

        while parent != self.NIL and parent.right == node :
            parent= parent.parent
            node= node.parent

        return parent
         

if __name__ == "__main__":
    rbt= RedBlackTree()
    for i in [20, 10, 30, 5, 15, 25, 35] :
        rbt.insert(i)

    target = rbt.search( 20)
    pred = rbt.predecessor(target)
    succ = rbt.successor(target)

    print("Node:", target.val)
    print("Predecessor:", pred.val if pred else "None")
    print("Successor:", succ.val if succ else "None")
 

