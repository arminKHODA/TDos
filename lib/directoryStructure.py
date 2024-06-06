import os

def print_directory_tree(path, indent=0):
    items = os.listdir(path)
    items.sort()
    
    for item in items:
        item_path = os.path.join(path, item)
        prefix = '    ' * indent + '|-- '
        print(prefix + item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path, indent + 1)

def main():
    user_path = input("Enter the directory path: ")
    if not os.path.exists(user_path):
        print("Path does not exist.")
        return

    print_directory_tree(user_path)
    input()

if __name__ == "__main__":
    main()
