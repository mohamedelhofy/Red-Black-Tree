from red_black_tree import RedBlackTree



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
    dictionary_app()
       