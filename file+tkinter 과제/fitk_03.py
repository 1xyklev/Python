import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file1_path = os.path.join(BASE_DIR, "file1.txt")
file2_path = os.path.join(BASE_DIR, "file2.txt")
output_file_path = os.path.join(BASE_DIR, "output.txt")

def merge_files(file1_path, file2_path, output_file_path):

    with open(file1_path, 'r',  encoding='utf-8') as file1:
        file1_content = file1.read()

    with open(file2_path, 'r',  encoding='utf-8') as file2:
        file2_content = file2.read()

    merged_content = file1_content + file2_content

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(merged_content)

merge_files(file1_path, file2_path, output_file_path)