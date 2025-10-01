"""
Week Assignment: File Handling and Exception Handling
"""

def file_read_write():
    """Reads a file and writes a modified version to a new file."""
    try:
        # Ask user for the input filename
        input_file = input("Enter the name of the file to read: ")
        
        with open(input_file, "r") as f:
            content = f.read()
        
        # Example modification: convert content to uppercase
        modified_content = content.upper()
        
        # Write to new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)
        
        print(f"✅ File successfully modified and saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    file_read_write()
