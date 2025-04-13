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

def load_dictionary(tree, filename="EN-US-Dictionary.txt"):
    try:
        with open(filename, 'r') as f:
            for line in f:
                word = line.strip()
                if word:
                    tree.insert(word)
    except FileNotFoundError:
        open(filename, 'w').close() 

def update_dictionary_file(word, filename="EN-US-Dictionary.txt"):
    with open(filename, 'a') as f:
        f.write(word + '\n')


def dictionary_app():
    rbt = RedBlackTree()
    load_dictionary(rbt)

    while True:
        print("\nDictionary Menu:")
        print("1. Insert Word")
        print("2. Look-up Word")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            word = input("Enter word to insert: ").strip()
            rbt.insert(word)
            update_dictionary_file(word)
            print("Word inserted.")
            print(f"Tree size: {rbt.get_size()}")
            print(f"Tree height: {rbt.get_height()}")
            print(f"Black height: {rbt.get_black_height()}")
        elif choice == '2':
            word = input("Enter word to look up: ").strip()
            print("YES" if rbt.search(word) else "NO")
        elif choice == '3':
            print("Exiting Dictionary App.")
            break
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    pass
       