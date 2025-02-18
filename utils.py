import subprocess, glob, os, sys

def remove_word_from_file(directory_path, words):
    file_paths = glob.glob(
        directory_path + "/*.mhtml"
    )
    if not file_paths:
        return print("No lectures found")
    for file_path in file_paths:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read the contents of the file
            contents = file.read()
        for word in words:
            # Replace the target string
            contents = contents.replace(word, "")
        # Open the file in write mode
        with open(file_path, "w") as file:
            # Write the modified contents back into the file
            file.write(contents)

def create_env_file():
    file_path = '.env'
    if not checkFileExists(file_path):
        env_variables = {
                'EMAIL': '"Your email"',
                'PWD': '"Your password"',
                'WORDS_TO_REMOVE': 'Word1, Word2, Word3, Word4'
            }
        with open(file_path, 'w') as env_file:
            for key, value in env_variables.items():
                env_file.write(f"{key} = {value}\n")

def print_progress_bar(progress, finalNumber):
    bar_length = 50
    filled_length = int(progress * bar_length // finalNumber)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {progress}/{finalNumber} {progress*100/finalNumber:.2f}%')
    sys.stdout.flush()
    if progress == finalNumber:
        print("\n")

#region Folder and file checks
def checkFolderExists(folder_path):
    fullPath = os.getcwd() + folder_path
    return os.path.exists(fullPath) and os.path.isdir(fullPath)

def checkFileExists(file_path):
    fullPath = os.getcwd() + file_path
    return os.path.isfile(fullPath) or os.path.exists(file_path)

def createFolder(path):
    if not checkFolderExists(path):
        subprocess.run('mkdir "{}"'.format(path[1:]), shell=True)

def checkIfExtesionExists(directory, extension):
    return any(file.endswith(extension) for file in os.listdir(directory))
#endregion