import os

def find_empty_folders(root_path):
    empty_folders = []
    for foldername, subfolders, filenames in os.walk(root_path, topdown=False):
        if not os.listdir(foldername):
            empty_folders.append(foldername)
    return empty_folders

def remove_folders(folders):
    for folder in folders:
        os.rmdir(folder)
        print(f"{folder} has been removed.")
    print("All empty folders have been removed.")

def main():
    root_path = input("Please enter the root path: ")
    if not os.path.isdir(root_path):
        print("The provided path is not a valid directory.")
        return

    empty_folders = find_empty_folders(root_path)
    
    if not empty_folders:
        print("No empty folders found.")
        return
    
    print("Empty folders found:")
    for folder in empty_folders:
        print(folder)
        
    user_input = input("Do you want to remove these folders? (yes/no): ").lower()
    if user_input == 'yes':
        remove_folders(empty_folders)
    else:
        print("No folders were removed.")

if __name__ == "__main__":
    main()
