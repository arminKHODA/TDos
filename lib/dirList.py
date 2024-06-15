import os

def list_directories(directory):
    """Prints the full path of all directories and subdirectories in the specified directory."""
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            print(os.path.join(root, dir))

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_directories(path)
