import os

def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for filename in file_list:
            with open(filename, 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n")

def main():
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    output = 'merged_output.txt'
    merge_files(files, output)
    print(f"Files merged into {output}")

if __name__ == '__main__':
    main()
