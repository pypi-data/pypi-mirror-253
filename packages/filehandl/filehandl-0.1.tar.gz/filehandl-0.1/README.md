# fileutil

A Python module for simplifying common file handling operations.

## Functions

### `read_file(file_path)`

Read the content of a file.

**Parameters:**

- `file_path` (str): The path to the file.

**Returns:**

- str: The content of the file.

### `write_file(file_path, content)`

Write content to a file.

**Parameters:**

- `file_path` (str): The path to the file.
- `content` (str): The content to be written.

### `copy_file(source_path, destination_path)`

Copy a file from the source path to the destination path.

**Parameters:**

- `source_path` (str): The path of the source file.
- `destination_path` (str): The path of the destination file.

### `move_file(source_path, destination_path)`

Move a file from the source path to the destination path.

**Parameters:**

- `source_path` (str): The path of the source file.
- `destination_path` (str): The path of the destination file.

### `delete_file(file_path)`

Delete a file specified by its path.

**Parameters:**

- `file_path` (str): The path of the file to be deleted.

### `create_directory(directory_path)`

Create a directory specified by its path.

**Parameters:**

- `directory_path` (str): The path of the directory to be created.
