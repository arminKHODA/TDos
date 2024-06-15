# TD Package

This package includes a set of Python scripts for managing and analyzing directory structures. The package currently contains the following scripts:

1. `TDmaster.py`
2. `cleanEmptyDIR.py`
3. `directoryStructure.py`
4. `fileList.py`

## Features

- Remove empty directories from a specified path.
- Create a JSON representation of the directory structure.
- Generate a list of all files within a directory and save it to a text file.

## Requirements

- Python 3.10

## Usage

1. **TDmaster.py**
    - This is the main script that integrates the functionalities of the other scripts.
    - It performs the following tasks:
        1. Cleans empty directories.
        2. Creates a directory structure JSON file.
        3. Generates a file list text file.

    ### Running TDmaster.py
    ```bash
    python TDmaster.py
    or run the VBS file
    ```

    This will execute all the functions on the current working directory and save the outputs in an `output` directory within the current working directory.

2. **cleanEmptyDIR.py**
    - Removes empty directories from the specified path.

    ### Function
    ```python
    clean_empty_directories(path)
    ```
    - `path`: The path where empty directories need to be removed.

3. **directoryStructure.py**
    - Creates a JSON file representing the directory structure.

    ### Function
    ```python
    create_directory_structure(base_path, output_path)
    ```
    - `base_path`: The base directory to analyze.
    - `output_path`: The directory where the output JSON file will be saved.

4. **fileList.py**
    - Generates a text file containing a list of all files within the specified directory.

    ### Function
    ```python
    generate_file_list(base_path, output_path)
    ```
    - `base_path`: The base directory to analyze.
    - `output_path`: The directory where the output text file will be saved.

## Example Usage

### Running each script individually

1. **Remove empty directories**
    ```python
    from cleanEmptyDIR import clean_empty_directories
    clean_empty_directories('/path/to/directory')
    ```

2. **Create directory structure JSON**
    ```python
    from directoryStructure import create_directory_structure
    create_directory_structure('/path/to/base_directory', '/path/to/output_directory')
    ```

3. **Generate file list**
    ```python
    from fileList import generate_file_list
    generate_file_list('/path/to/base_directory', '/path/to/output_directory')
    ```

## License

free to use.
