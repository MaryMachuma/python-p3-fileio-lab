def write_file(file_name, file_content):
    """Writes content to a new .txt file, overwriting if it exists."""
    with open(f"{file_name}.txt", "w") as file:
              file.write(file_content)

def append_file(file_name, append_content):
    """
    Append content to an existing text file.
    
    Args:
        file_name (str): The name of the file (without extension)
        append_content (str): The content to append to the file
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)
 

def read_file(file_name):
    """Reads and returns the content of a .txt file."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
    
  # Add this at the end of lib/file_io.py
if __name__ == "__main__":
    # Write initial content to the file
    write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")
    
    # Append additional content to the file
    append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")
    
    # Read and display the file content
    content = read_file(file_name="logfile")
    print(content)