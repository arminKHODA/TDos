import os

def list_files(directory):
    """Prints the full path of all files in the specified directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_files(path)

