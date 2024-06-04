import os


def merge_txt_files(directory_path, output_file):
    # Check if the provided directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

    # If no text files found
    if not files:
        print(f"No text files found in '{directory_path}'.")
        return

    # Open output file in append mode
    with open(output_file, 'w') as outfile:
        # Iterate over each text file
        for file in files:
            file_path = os.path.join(directory_path, file)
            # Open each text file and append its content to the output file
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
            # Add a newline character to separate contents of different files
            outfile.write('\n')


# Example usage
merge_txt_files('../testRuns', 'merged_output.csv')
