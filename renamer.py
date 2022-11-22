import os
import sys

def rename(fol, fil):
    with open(fil, 'r') as file:
        lines = file.readlines()
    for file_count, name in enumerate(os.listdir(fol)):
        pass
    if (file_count+1 != len(lines)):
        print("Number of files in folder does not match the number of lines in the corresponding file.")
        print("Please make sure the numbers match (there should not be an empty line at the bottom of the names file).")
        exit()
    for count, filename in enumerate(os.listdir(fol)):
        original = f"{fol}/{filename}"
        new_name = f"{fol}/{lines[count].rstrip()}"
        os.rename(original, new_name)


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("Please run this as 'renamer.py path_to_folder path_to_file_with_names")
    else:
        rename(args[0], args[1])

if __name__ == "__main__":
    main()